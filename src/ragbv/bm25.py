"""BM25 tiếng Việt: bản có dấu (tách từ pyvi, "bảo_hiểm" là 1 từ) và bản bỏ dấu (theo âm tiết)."""
from __future__ import annotations

import re
import unicodedata

import numpy as np
from rank_bm25 import BM25Okapi

from .chunking import Chunk

_WORD = re.compile(r"\w+", re.UNICODE)


def strip_diacritics(text: str) -> str:
    """'Bảo hiểm Đồng' -> 'Bao hiem Dong'. Dùng cho người dùng gõ không dấu."""
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return text.replace("đ", "d").replace("Đ", "D")


def tokenize_vi(text: str) -> list[str]:
    """Tách từ tiếng Việt bằng pyvi: 'người được bảo hiểm' -> ['người', 'được', 'bảo_hiểm']."""
    from pyvi import ViTokenizer

    text = unicodedata.normalize("NFC", text.lower())
    return [t for t in ViTokenizer.tokenize(text).split() if _WORD.search(t)]


def tokenize_nodiac(text: str) -> list[str]:
    """Bỏ dấu rồi tách theo âm tiết: khớp được câu hỏi gõ không dấu."""
    return _WORD.findall(strip_diacritics(text.lower()))


TOKENIZERS = {"bm25": tokenize_vi, "bm25_nd": tokenize_nodiac}


class BM25Index:
    def __init__(self, chunks: list[Chunk], tokenizer: str = "bm25", field: str = "embed_text"):
        self.chunks = chunks
        self.tok = TOKENIZERS[tokenizer]
        self.bm25 = BM25Okapi([self.tok(getattr(c, field)) for c in chunks])

    def search(self, query: str, k: int = 10, doc_ids: list[str] | None = None) -> list[tuple[str, float]]:
        scores = self.bm25.get_scores(self.tok(query))
        if doc_ids:
            scores = np.where([c.doc_id in doc_ids for c in self.chunks], scores, -np.inf)
        top = np.argsort(-scores)[:k]
        return [(self.chunks[i].chunk_id, float(scores[i])) for i in top if np.isfinite(scores[i]) and scores[i] > 0]
