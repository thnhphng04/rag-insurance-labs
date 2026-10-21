"""pgvector: lưu chunk + vector, HNSW cosine, truy vấn có/không lọc metadata."""
from __future__ import annotations

import numpy as np
import psycopg
from pgvector.psycopg import register_vector

from .chunking import Chunk
from .config import env

SCHEMA = """
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id    text NOT NULL,
    strategy    text NOT NULL,
    doc_id      text NOT NULL,
    page_labels text[] NOT NULL,
    section     text,
    kind        text,
    text        text NOT NULL,
    embed_text  text NOT NULL,
    embedding   vector(1024) NOT NULL,
    PRIMARY KEY (strategy, chunk_id)
);
-- Tham số mặc định của pgvector, ghi rõ để dễ thí nghiệm
CREATE INDEX IF NOT EXISTS chunks_hnsw ON chunks
    USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);
CREATE INDEX IF NOT EXISTS chunks_doc ON chunks (strategy, doc_id);
"""


def connect() -> psycopg.Connection:
    conn = psycopg.connect(env("PG_DSN"), autocommit=True)
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    register_vector(conn)
    return conn


def init(conn: psycopg.Connection) -> None:
    conn.execute(SCHEMA)


def upsert(conn: psycopg.Connection, chunks: list[Chunk], vecs: np.ndarray) -> int:
    """Ghi đè theo (strategy, chunk_id); xoá chunk cũ của cùng strategy+doc không còn trong danh sách."""
    with conn.cursor() as cur:
        cur.executemany(
            """INSERT INTO chunks (chunk_id, strategy, doc_id, page_labels, section, kind, text, embed_text, embedding)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
               ON CONFLICT (strategy, chunk_id) DO UPDATE SET
                 page_labels = EXCLUDED.page_labels, section = EXCLUDED.section, kind = EXCLUDED.kind,
                 text = EXCLUDED.text, embed_text = EXCLUDED.embed_text, embedding = EXCLUDED.embedding""",
            [(c.chunk_id, c.strategy, c.doc_id, c.page_labels, c.section, c.kind, c.text, c.embed_text, v)
             for c, v in zip(chunks, vecs)])
        keep = {(c.strategy, c.chunk_id) for c in chunks}
        for strategy, doc_id in {(c.strategy, c.doc_id) for c in chunks}:
            ids = [cid for s, cid in keep if s == strategy]
            cur.execute("DELETE FROM chunks WHERE strategy = %s AND doc_id = %s AND NOT (chunk_id = ANY(%s))",
                        (strategy, doc_id, ids))
    return len(chunks)


def search(conn: psycopg.Connection, qvec: np.ndarray, strategy: str, k: int = 10,
           doc_ids: list[str] | None = None, ef_search: int = 40, iterative: str = "off",
           force_index: bool = False) -> list[tuple[str, float]]:
    """Top-k theo cosine. Trả về [(chunk_id, similarity)].

    iterative: "off" | "relaxed_order" | "strict_order" (pgvector >= 0.8). Khi lọc doc_ids,
    "off" có thể trả về ít hơn k dòng vì WHERE được áp SAU khi duyệt ef_search ứng viên.
    force_index: bảng nhỏ thì planner chọn quét + sắp xếp chính xác thay vì HNSW; bật để buộc dùng HNSW
    (mô phỏng hành vi ở quy mô lớn).
    """
    with conn.transaction():
        conn.execute(f"SET LOCAL hnsw.ef_search = {int(ef_search)}")
        conn.execute(f"SET LOCAL hnsw.iterative_scan = {iterative}")
        if force_index:
            for s in ("enable_seqscan", "enable_bitmapscan", "enable_sort"):
                conn.execute(f"SET LOCAL {s} = off")
        where, params = "strategy = %s", [strategy]
        if doc_ids:
            where += " AND doc_id = ANY(%s)"
            params.append(doc_ids)
        rows = conn.execute(
            f"SELECT chunk_id, 1 - (embedding <=> %s) FROM chunks WHERE {where} "
            f"ORDER BY embedding <=> %s LIMIT {int(k)}",
            [qvec, *params, qvec]).fetchall()
    return [(r[0], float(r[1])) for r in rows]
