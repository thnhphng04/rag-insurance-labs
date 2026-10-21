"""Golden set: câu hỏi + đáp án + bằng chứng (doc, trang, đoạn trích nguyên văn).

Một chunk được coi là "đúng" cho một bằng chứng nếu nó thuộc đúng doc_id và chứa đủ các đoạn
`must_contain` (so khớp sau chuẩn hóa). Cách chấm này không phụ thuộc chiến lược chunk, nên dùng
được để so sánh các cấu hình chunking ở Lab 2 và retrieval ở Lab 3.
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field

from .config import GOLDEN
from .parsing import Page, load_pages

GOLDEN_FILE = GOLDEN / "golden_set.jsonl"


@dataclass
class Evidence:
    doc_id: str
    section: str
    page_label: str
    must_contain: list[str]
    group: str | None = None  # các bằng chứng cùng group là thay thế nhau; không có group = bắt buộc riêng


@dataclass
class Item:
    id: str
    type: str
    question: str
    answer: str
    evidence: list[Evidence] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    notes: str = ""

    @property
    def in_scope(self) -> bool:
        return bool(self.evidence)


def load_golden() -> list[Item]:
    items = []
    for line in GOLDEN_FILE.read_text(encoding="utf-8").splitlines():
        if line.strip():
            d = json.loads(line)
            d["evidence"] = [Evidence(**e) for e in d.get("evidence", [])]
            items.append(Item(**d))
    return items


def norm(text: str) -> str:
    """NFC, chữ thường, bỏ ký hiệu Markdown bảng/nhấn mạnh, gộp khoảng trắng."""
    text = unicodedata.normalize("NFC", text).lower()
    text = re.sub(r"[|*#]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_all(text: str, snippets: list[str]) -> bool:
    t = norm(text)
    return all(norm(s) in t for s in snippets)


def is_relevant(chunk_text: str, chunk_doc_id: str, ev: Evidence) -> bool:
    return chunk_doc_id == ev.doc_id and contains_all(chunk_text, ev.must_contain)


def review_markdown(items: list[Item]) -> str:
    """Bản dễ đọc để người duyệt golden set (sinh từ JSONL, không sửa tay)."""
    lines = ["# Golden set – bản duyệt", "",
             "Sinh tự động từ `golden_set.jsonl` bằng `ragbv.golden.review_markdown`. Sửa ở file JSONL.", "",
             "| ID | Loại | Câu hỏi | Đáp án chuẩn | Bằng chứng (doc · mục · trang) | Ghi chú |",
             "|---|---|---|---|---|---|"]
    for i in items:
        ev = "<br>".join(f"`{e.doc_id}` · {e.section} · tr.{e.page_label}" for e in i.evidence) or "—"
        cells = [i.id, i.type, i.question, i.answer, ev, i.notes]
        lines.append("| " + " | ".join(c.replace("|", "\\|").replace("\n", " ") for c in cells) + " |")
    return "\n".join(lines) + "\n"


def validate(items: list[Item], parser: str = "docling") -> list[str]:
    """Mỗi đoạn trích phải có trong đúng trang đã parse; trả về danh sách lỗi (rỗng = hợp lệ)."""
    cache: dict[str, list[Page]] = {}
    problems = []
    ids = [i.id for i in items]
    problems += [f"trùng id: {x}" for x in sorted({x for x in ids if ids.count(x) > 1})]
    for item in items:
        if item.type != "out_of_scope" and not item.evidence:
            problems.append(f"{item.id}: thiếu evidence")
        for ev in item.evidence:
            pages = cache.setdefault(ev.doc_id, load_pages(ev.doc_id, parser))
            page = next((p for p in pages if p.page_label == ev.page_label), None)
            if page is None:
                problems.append(f"{item.id}: {ev.doc_id} không có trang {ev.page_label}")
                continue
            for s in ev.must_contain:
                if norm(s) not in norm(page.text):
                    where = [p.page_label for p in pages if norm(s) in norm(p.text)]
                    problems.append(f"{item.id}: '{s}' không có ở {ev.doc_id} trang {ev.page_label}"
                                    + (f" (thấy ở trang {where})" if where else " (không thấy trong tài liệu)"))
    return problems
