"""Contextual Retrieval (Anthropic, 2024): LLM viết 1-2 câu ngữ cảnh cho mỗi chunk, gắn vào trước khi embed.

Toàn văn tài liệu đặt ở đầu prompt (giống nhau cho mọi chunk của cùng tài liệu) để tận dụng
prompt caching tự động của OpenAI (giảm giá phần input lặp lại).
"""
from __future__ import annotations

import hashlib
import json

from .chunking import Chunk
from .config import CACHE, env

CTX_CACHE = CACHE / "contextual"

PROMPT_DOC = """<tai_lieu>
{doc}
</tai_lieu>"""

PROMPT_CHUNK = """Đây là một đoạn trích từ tài liệu trên:
<doan_trich>
{chunk}
</doan_trich>
Hãy viết 1-2 câu tiếng Việt ngắn gọn đặt đoạn trích vào ngữ cảnh của toàn bộ tài liệu để cải thiện việc tìm kiếm:
nêu tên sản phẩm, công ty, đoạn này thuộc chương/điều/phần nào và nói về nội dung gì.
Chỉ trả lời bằng câu ngữ cảnh, không thêm gì khác."""


def _client():
    from openai import OpenAI

    return OpenAI(api_key=env("OPENAI_API_KEY"))


def contextualize(chunks: list[Chunk], doc_text: str, model: str | None = None) -> tuple[list[Chunk], dict]:
    """Trả về chunk mới có embed_text = ngữ cảnh + nội dung, và thống kê token/cache."""
    model = model or env("LLM_MODEL", "gpt-4.1-mini")
    CTX_CACHE.mkdir(parents=True, exist_ok=True)
    client = None
    stats = {"calls": 0, "cached_calls": 0, "prompt_tokens": 0, "cached_prompt_tokens": 0, "completion_tokens": 0}
    out = []
    for c in chunks:
        key = hashlib.sha1(f"{model}|{hashlib.sha1(doc_text.encode()).hexdigest()}|{c.text}".encode()).hexdigest()
        f = CTX_CACHE / f"{key}.json"
        if f.exists():
            ctx = json.loads(f.read_text(encoding="utf-8"))["context"]
            stats["cached_calls"] += 1
        else:
            client = client or _client()
            resp = client.chat.completions.create(
                model=model, temperature=0,
                messages=[{"role": "user", "content": PROMPT_DOC.format(doc=doc_text) + "\n\n"
                           + PROMPT_CHUNK.format(chunk=c.text)}])
            ctx = resp.choices[0].message.content.strip()
            u = resp.usage
            stats["calls"] += 1
            stats["prompt_tokens"] += u.prompt_tokens
            stats["completion_tokens"] += u.completion_tokens
            details = getattr(u, "prompt_tokens_details", None)
            stats["cached_prompt_tokens"] += (getattr(details, "cached_tokens", 0) or 0) if details else 0
            f.write_text(json.dumps({"context": ctx, "chunk_id": c.chunk_id}, ensure_ascii=False), encoding="utf-8")
        new = Chunk(**{**c.__dict__, "strategy": c.strategy + "+ctx", "embed_text": f"{ctx}\n{c.embed_text}",
                       "meta": {**c.meta, "context": ctx}})
        out.append(new)
    return out, stats
