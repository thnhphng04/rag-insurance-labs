"""Lab 3: dense (pgvector) + BM25 -> RRF -> rerank (cross-encoder), lọc theo sản phẩm, viết lại câu hỏi."""
from __future__ import annotations

import hashlib
import json
import re
import time
from collections import defaultdict

from .bm25 import BM25Index, strip_diacritics
from .chunking import Chunk
from .config import CACHE, DocMeta, env
from . import embedding as EMB, store


def rrf(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    """Reciprocal Rank Fusion (Cormack et al., SIGIR 2009): score(d) = Σ 1/(k + rank_i(d)).

    Chỉ dùng thứ hạng, không dùng điểm số -> không cần chuẩn hoá giữa cosine và BM25.
    """
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, cid in enumerate(ranking, 1):
            scores[cid] += 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda x: -x[1])


# ---------- nhận diện sản phẩm trong câu hỏi -> lọc doc_id ----------

def product_filter(query: str, docs: dict[str, DocMeta]) -> list[str] | None:
    """Khớp alias (đã bỏ dấu, theo ranh giới từ) trong manifest. Không khớp gì -> None (không lọc)."""
    q = " " + re.sub(r"[^a-z0-9]+", " ", strip_diacritics(query.lower())) + " "
    hits = []
    for doc_id, meta in docs.items():
        for alias in meta.extra.get("aliases", []):
            a = " " + re.sub(r"[^a-z0-9]+", " ", strip_diacritics(alias.lower())).strip() + " "
            if a in q:
                hits.append(doc_id)
                break
    return hits or None


# ---------- viết lại câu hỏi bằng LLM ----------

REWRITE_CACHE = CACHE / "rewrite"
REWRITE_PROMPT = """Bạn chuẩn hoá câu hỏi của khách hàng về bảo hiểm trước khi tìm kiếm trong tài liệu quy tắc, điều khoản.
- Thêm dấu tiếng Việt nếu câu hỏi gõ không dấu.
- Mở rộng viết tắt: NĐBH/NDBH = Người được bảo hiểm, BMBH = Bên mua bảo hiểm, STBH = Số tiền bảo hiểm,
  HĐBH = Hợp đồng bảo hiểm, QTĐK = Quy tắc và Điều khoản, BHNT = Bảo hiểm nhân thọ, AVSK = An Vui Sống Khỏe.
- Giữ nguyên tên sản phẩm, con số, ý hỏi. Không trả lời câu hỏi, không thêm thông tin.
Chỉ trả về câu hỏi đã chuẩn hoá.

Câu hỏi: {q}"""


def rewrite(query: str, model: str | None = None) -> str:
    model = model or env("LLM_MODEL", "gpt-4.1-mini")
    REWRITE_CACHE.mkdir(parents=True, exist_ok=True)
    f = REWRITE_CACHE / (hashlib.sha1(f"{model}|{REWRITE_PROMPT}|{query}".encode()).hexdigest() + ".json")
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))["rewritten"]
    from openai import OpenAI

    resp = OpenAI(api_key=env("OPENAI_API_KEY")).chat.completions.create(
        model=model, temperature=0, messages=[{"role": "user", "content": REWRITE_PROMPT.format(q=query)}])
    out = resp.choices[0].message.content.strip()
    f.write_text(json.dumps({"query": query, "rewritten": out}, ensure_ascii=False), encoding="utf-8")
    return out


# ---------- reranker ----------

_reranker = None


def reranker(name: str = "BAAI/bge-reranker-v2-m3"):
    global _reranker
    if _reranker is None:
        from FlagEmbedding import FlagReranker

        _reranker = FlagReranker(name, use_fp16=True)
    return _reranker


def rerank(query: str, cands: list[Chunk], max_length: int = 512) -> list[tuple[Chunk, float]]:
    """Cross-encoder đọc cặp (câu hỏi, breadcrumb + nội dung) cùng lúc."""
    if not cands:
        return []
    scores = reranker().compute_score([(query, c.embed_text) for c in cands], max_length=max_length, normalize=True)
    scores = [scores] if isinstance(scores, float) else scores
    return sorted(zip(cands, scores), key=lambda x: -x[1])


# ---------- pipeline ----------

class Retriever:
    """Giữ chunk, index BM25 và kết nối pgvector cho một chiến lược chunk."""

    def __init__(self, chunks: list[Chunk], docs: dict[str, DocMeta], conn, strategy: str):
        self.chunks = {c.chunk_id: c for c in chunks}
        self.docs, self.conn, self.strategy = docs, conn, strategy
        self.bm25 = {name: BM25Index(chunks, name) for name in ("bm25", "bm25_nd")}

    def run(self, query: str, method: str, k: int = 10, n_cand: int = 50, use_filter: bool = False,
            use_rewrite: bool = False, timings: dict | None = None, doc_ids: list[str] | None = None) -> list[Chunk]:
        """method: dense | bm25 | bm25_nd | hybrid (dense+bm25) | hybrid3 (dense+bm25+bm25_nd) | <hybrid*>+rerank

        doc_ids: chỉ định tập tài liệu (vd. câu con cho một sản phẩm); nếu có thì bỏ qua use_filter.
        """
        t = timings if timings is not None else {}
        q = query
        if use_rewrite:
            t0 = time.perf_counter()
            q = rewrite(query)
            t["rewrite"] = time.perf_counter() - t0
        if doc_ids is None:
            doc_ids = product_filter(query, self.docs) if use_filter else None
        base = method.replace("+rerank", "")
        parts = {"dense": ["dense"], "bm25": ["bm25"], "bm25_nd": ["bm25_nd"],
                 "hybrid": ["dense", "bm25"], "hybrid3": ["dense", "bm25", "bm25_nd"]}[base]
        depth = n_cand if (len(parts) > 1 or method.endswith("+rerank")) else k
        rankings = []
        for p in parts:
            t0 = time.perf_counter()
            if p == "dense":
                qv = EMB.encode([q])[0]
                hits = store.search(self.conn, qv, self.strategy, depth, doc_ids,
                                    iterative="relaxed_order" if doc_ids else "off")
            else:
                # Bản bỏ dấu luôn dùng câu gốc (người dùng gõ sao tìm vậy); bản có dấu dùng câu đã viết lại
                hits = self.bm25[p].search(query if p == "bm25_nd" else q, depth, doc_ids)
            t[p] = time.perf_counter() - t0
            rankings.append([cid for cid, _ in hits])
        fused = rrf(rankings) if len(rankings) > 1 else [(cid, 0.0) for cid in rankings[0]]
        cands = [self.chunks[cid] for cid, _ in fused[:depth]]
        if method.endswith("+rerank"):
            t0 = time.perf_counter()
            cands = [c for c, _ in rerank(q, cands)]
            t["rerank"] = time.perf_counter() - t0
        return cands[:k]
