"""BGE-M3 dense embedding (fp16 trên GPU) có cache theo nội dung."""
from __future__ import annotations

import hashlib

import numpy as np

from .config import CACHE

EMB_CACHE = CACHE / "emb"
_model = None


def model(name: str = "BAAI/bge-m3"):
    global _model
    if _model is None:
        from FlagEmbedding import BGEM3FlagModel

        _model = BGEM3FlagModel(name, use_fp16=True)
    return _model


def encode(texts: list[str], batch_size: int = 8, max_length: int = 1024) -> np.ndarray:
    """Vector dense đã chuẩn hoá L2 (cosine = tích vô hướng). Cache theo hash từng văn bản."""
    EMB_CACHE.mkdir(parents=True, exist_ok=True)
    keys = [hashlib.sha1(f"bge-m3|{max_length}|{t}".encode()).hexdigest() for t in texts]
    out = np.zeros((len(texts), 1024), dtype=np.float32)
    todo = []
    for i, k in enumerate(keys):
        f = EMB_CACHE / f"{k}.npy"
        if f.exists():
            out[i] = np.load(f)
        else:
            todo.append(i)
    if todo:
        vecs = model().encode([texts[i] for i in todo], batch_size=batch_size, max_length=max_length)["dense_vecs"]
        for i, v in zip(todo, vecs):
            out[i] = v
            np.save(EMB_CACHE / f"{keys[i]}.npy", v.astype(np.float32))
    return out


def search(query_vecs: np.ndarray, doc_vecs: np.ndarray, k: int = 10) -> np.ndarray:
    """Chỉ số top-k theo cosine cho mỗi query, shape (n_query, k)."""
    scores = query_vecs @ doc_vecs.T
    return np.argsort(-scores, axis=1)[:, :k]
