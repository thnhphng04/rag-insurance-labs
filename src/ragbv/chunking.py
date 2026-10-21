"""Lab 2: ba chiến lược chunk trên output Docling đã làm sạch.

- fixed     : cửa sổ N token (tokenizer BGE-M3), chồng lấp M token, không quan tâm cấu trúc
- recursive : RecursiveCharacterTextSplitter theo "\\n\\n" -> "\\n" -> câu -> từ, giới hạn theo token
- structure : cắt theo tiêu đề (Chương/Phần > Điều > mục), gắn breadcrumb "Sản phẩm › Chương › Điều";
              bảng dựng lại từ tables JSON (gom theo section, không lặp ô gộp); bỏ mục lục, trang biểu mẫu

Mọi chunk giữ `text` (nội dung gốc, dùng để chấm relevance) tách khỏi `embed_text` (thứ đem đi embed,
có thể kèm breadcrumb/ngữ cảnh) để so sánh công bằng giữa các chiến lược.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .config import DATA, DocMeta
from .parsing import Page
from .tables import load_tables

CHUNKS = DATA / "chunks"
_tokenizer = None


def tokenizer():
    global _tokenizer
    if _tokenizer is None:
        from transformers import AutoTokenizer

        _tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
    return _tokenizer


def n_tokens(text: str) -> int:
    return len(tokenizer()(text, add_special_tokens=False)["input_ids"])


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    strategy: str
    text: str
    embed_text: str
    page_labels: list[str]
    section: str = ""
    kind: str = "text"  # text | table
    n_tokens: int = 0
    meta: dict = field(default_factory=dict)


def _make(doc_id: str, strategy: str, text: str, pages: list[str], embed_text: str | None = None,
          section: str = "", kind: str = "text") -> Chunk:
    embed_text = embed_text or text
    cid = hashlib.sha1(f"{doc_id}|{strategy}|{embed_text}".encode()).hexdigest()[:12]
    return Chunk(cid, doc_id, strategy, text, embed_text, pages, section, kind, n_tokens(embed_text))


# ---------- văn bản liền mạch + ánh xạ vị trí -> trang ----------

_NOISE = re.compile(r"^\s*<!-- image -->\s*$", re.M)


def _doc_text(pages: list[Page]) -> tuple[str, list[tuple[int, str]]]:
    parts, starts, pos = [], [], 0
    for p in pages:
        t = _NOISE.sub("", p.text).strip()
        if not t:
            continue
        starts.append((pos, p.page_label))
        parts.append(t)
        pos += len(t) + 2
    return "\n\n".join(parts), starts


def _pages_for(start: int, end: int, starts: list[tuple[int, str]]) -> list[str]:
    out = []
    for i, (s, label) in enumerate(starts):
        e = starts[i + 1][0] if i + 1 < len(starts) else 10**12
        if s < end and start < e:
            out.append(label)
    return out


# ---------- 1. fixed ----------

def fixed_chunks(meta: DocMeta, pages: list[Page], size: int = 512, overlap: int = 64) -> list[Chunk]:
    text, starts = _doc_text(pages)
    enc = tokenizer()(text, add_special_tokens=False, return_offsets_mapping=True)
    offs = enc["offset_mapping"]
    out, i = [], 0
    while i < len(offs):
        j = min(i + size, len(offs))
        s, e = offs[i][0], offs[j - 1][1]
        out.append(_make(meta.doc_id, "fixed", text[s:e], _pages_for(s, e, starts)))
        if j == len(offs):
            break
        i = j - overlap
    return out


# ---------- 2. recursive ----------

def recursive_chunks(meta: DocMeta, pages: list[Page], size: int = 512, overlap: int = 64) -> list[Chunk]:
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    text, starts = _doc_text(pages)
    splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer(), chunk_size=size, chunk_overlap=overlap,
        separators=["\n\n", "\n", ". ", " ", ""], add_start_index=True)
    out = []
    for d in splitter.create_documents([text]):
        s = d.metadata["start_index"]
        out.append(_make(meta.doc_id, "recursive", d.page_content, _pages_for(s, s + len(d.page_content), starts)))
    return out


# ---------- 3. structure ----------

# "Chương"/"Phần" phải kèm số ("Chương II", "PHẦN I") -> không khớp "Chương trình Bảo hiểm".
# Bảng nằm trong một Điều (vd. "Bảng Giới hạn..." của AVSK Điều 4) là cấp 3, không phải cấp 1.
_L1 = re.compile(r"^(chương\s+[IVX\d]+|phần\s+[IVX\d]+|phụ lục|điều khoản bổ sung|bảng quyền lợi|biểu phí"
                 r"|bảng tỷ lệ)\b", re.I)
_L2 = re.compile(r"^(điều\s+\d+|[IVX]+\s*[.\-–]\s)", re.I)
_TOC = re.compile(r"^mục lục$", re.I)


def _level(heading: str) -> int:
    h = heading.strip()
    if _L1.match(h):
        return 1
    if _L2.match(h):
        return 2
    return 3


def _split_long(text: str, max_tokens: int) -> list[str]:
    if n_tokens(text) <= max_tokens:
        return [text]
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    sp = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer(), chunk_size=max_tokens, chunk_overlap=48, separators=["\n\n", "\n", ". ", " ", ""])
    return sp.split_text(text)


def _table_blocks(lines: list[str]) -> list[tuple[str, list[str]]]:
    """Tách trang thành các khối ('heading'|'table'|'text', lines)."""
    blocks: list[tuple[str, list[str]]] = []
    for line in lines:
        kind = "heading" if line.startswith("## ") else "table" if line.lstrip().startswith("|") else "text"
        if kind == "heading" or not blocks or blocks[-1][0] != kind:
            blocks.append((kind, [line]))
        else:
            blocks[-1][1].append(line)
    return blocks


def _match_table(block: str, candidates: list[dict], used: set[int]) -> dict | None:
    """Chọn bảng JSON cùng trang có nhiều nhãn dòng xuất hiện trong khối Markdown nhất."""
    best, best_score = None, 0
    for t in candidates:
        if t["table_id"] in used:
            continue
        score = sum(1 for r in t["records"] if r["label"] and r["label"][:30] in block)
        if score > best_score:
            best, best_score = t, score
    return best


def _table_chunks(table: dict, breadcrumb: list[str], product: str, max_tokens: int) -> list[tuple[str, str]]:
    """Gom các dòng cùng section thành chunk 'nhãn — cột: giá trị; ...'. Trả về [(path, text)].

    Chia nhóm dài theo ranh giới dòng, đo trên đúng thứ sẽ đem embed (breadcrumb + tiêu đề cột + các dòng),
    để chunk bảng không phải cắt lại lần nữa và phần nào cũng có tiêu đề cột. Một dòng dài hơn
    max_tokens vẫn giữ nguyên một chunk.
    """
    groups: dict[str, list[str]] = {}
    for r in table["records"]:
        sec = " › ".join(r["section"])
        vals = "; ".join(f"{k}: {v}" for k, v in r["values"].items() if v)
        groups.setdefault(sec, []).append(f"- {r['label']}" + (f" — {vals}" if vals else ""))
    # Chỉ liệt kê cột giá trị; ô gộp nhiều cột nhãn ("CHƯƠNG TRÌNH BẢO HIỂM" × 2) không lặp tên
    value_cols = [c for i, c in enumerate(table["columns"]) if i not in table["label_columns"]]
    header = f"Bảng ({', '.join(dict.fromkeys(value_cols))})"
    out = []
    for sec, rows in groups.items():
        path = " › ".join([product, *breadcrumb, *([sec] if sec else [])])
        size = lambda part: n_tokens(f"[{path}]\n{header}\n" + "\n".join(part))
        body, cur = [], []
        for row in rows:
            if cur and size(cur + [row]) > max_tokens:
                body.append(cur)
                cur = []
            cur.append(row)
        body.append(cur)
        for part in body:
            out.append((path, f"{header}\n" + "\n".join(part)))
    return out


def structure_chunks(meta: DocMeta, pages: list[Page], max_tokens: int = 400, min_tokens: int = 60) -> list[Chunk]:
    product = meta.product.split(" - ")[0]
    exclude = set(map(str, meta.extra.get("exclude_pages", [])))
    try:
        tables = load_tables(meta.doc_id)
    except FileNotFoundError:
        tables = []
    used: set[int] = set()
    stack: list[tuple[int, str]] = []          # (level, heading)
    sections: list[dict] = []                   # {path, heading, body[], pages{}}
    cur = None
    skip_toc = False

    def open_section(heading: str | None, page: str):
        nonlocal cur
        cur = {"path": [h for _, h in stack[:-1]] if heading else [h for _, h in stack],
               "heading": heading or "", "body": [], "pages": [page]}
        sections.append(cur)

    for p in pages:
        if p.page_label in exclude:
            continue
        for kind, lines in _table_blocks(_NOISE.sub("", p.text).splitlines()):
            if kind == "heading":
                h = lines[0][3:].strip()
                skip_toc = bool(_TOC.match(h))
                if skip_toc:
                    continue
                lvl = _level(h)
                while stack and stack[-1][0] >= lvl:
                    stack.pop()
                stack.append((lvl, h))
                open_section(h, p.page_label)
            elif skip_toc:
                continue
            elif kind == "table":
                block = "\n".join(lines)
                t = _match_table(block, [t for t in tables if t["page_label"] == p.page_label], used)
                if t is None:
                    continue  # mục lục/biểu mẫu/bảng không trích được: bỏ (đã có trong tables JSON nếu hợp lệ)
                used.add(t["table_id"])
                for path, text in _table_chunks(t, [h for _, h in stack], product, max_tokens):
                    sections.append({"table": True, "path_str": path, "text": text, "pages": [p.page_label]})
                cur = None  # văn bản sau bảng mở section mới cùng heading
            else:
                if cur is None or cur.get("table"):
                    open_section(None, p.page_label)
                cur["body"].extend(l for l in lines if l.strip())
                if p.page_label not in cur["pages"]:
                    cur["pages"].append(p.page_label)

    # Gộp section văn bản quá ngắn vào section kế tiếp cùng cha
    merged: list[dict] = []
    for s in sections:
        if s.get("table"):
            merged.append(s)
            continue
        if not s["body"]:
            continue  # tiêu đề không có nội dung riêng: đã nằm trong breadcrumb của các chunk con
        text = "\n".join(([s["heading"]] if s["heading"] else []) + s["body"]).strip()
        prev = merged[-1] if merged else None
        if (prev and not prev.get("table") and prev["path"] == s["path"]
                and n_tokens(prev["text"]) < min_tokens):
            prev["text"] += "\n" + text
            prev["pages"] += [x for x in s["pages"] if x not in prev["pages"]]
        else:
            merged.append({**s, "text": text})

    out = []
    for s in merged:
        if s.get("table"):
            # Chunk bảng đã được chia theo dòng trong _table_chunks: không cắt lại
            path, kind, pieces = s["path_str"], "table", [s["text"]]
        else:
            path, kind = " › ".join([product, *s["path"]]), "text"
            pieces = _split_long(s["text"], max_tokens)
        for piece in pieces:
            out.append(_make(meta.doc_id, "structure", piece, s["pages"], f"[{path}]\n{piece}", path, kind))
    return out


STRATEGIES = {"fixed": fixed_chunks, "recursive": recursive_chunks, "structure": structure_chunks}


def save_chunks(name: str, chunks: list[Chunk]) -> Path:
    CHUNKS.mkdir(parents=True, exist_ok=True)
    out = CHUNKS / f"{name}.jsonl"
    out.write_text("\n".join(json.dumps(asdict(c), ensure_ascii=False) for c in chunks) + "\n", encoding="utf-8")
    return out


def load_chunks(name: str) -> list[Chunk]:
    return [Chunk(**json.loads(l)) for l in (CHUNKS / f"{name}.jsonl").read_text(encoding="utf-8").splitlines() if l]
