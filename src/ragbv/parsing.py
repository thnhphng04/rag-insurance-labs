"""Parse PDF quy tắc bảo hiểm: tách trang đôi, PyMuPDF / Docling, chuẩn hóa NFC, bỏ header/footer."""
from __future__ import annotations

import json
import re
import time
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

import pymupdf as fitz

from .config import CACHE, PARSED, DocMeta


@dataclass
class Page:
    idx: int         # thứ tự trang logic, 0-based
    pdf_page: int    # trang trong file PDF gốc, 1-based
    half: str        # "full" | "left" | "right"
    page_label: str  # số trang in, dùng để trích dẫn ("24-25" nếu giữ nguyên trang đôi)
    text: str


@dataclass
class LogicalPage:
    pdf_page: int
    half: str
    rect: fitz.Rect
    page_label: str


def logical_pages(pdf_path: Path, keep_spread: tuple[int, ...] = ()) -> list[LogicalPage]:
    """Trang ngang (rộng > 1.2 x cao) là trang đôi: chia thành nửa trái/phải.

    Số trang in được đánh tuần tự, khớp với số in ở chân trang của An Gia / Tâm An
    (PDF tr.13 -> in 24-25). Trang trong keep_spread (vd. bảng trải ngang 2 nửa)
    được giữ nguyên, nhãn "24-25".
    """
    out, label = [], 0
    with fitz.open(pdf_path) as doc:
        for i, p in enumerate(doc):
            r = p.rect
            if r.width > r.height * 1.2 and (i + 1) in keep_spread:
                out.append(LogicalPage(i + 1, "spread", r, f"{label + 1}-{label + 2}"))
                label += 2
            elif r.width > r.height * 1.2:
                mid = r.x0 + r.width / 2
                for half, rect in (("left", fitz.Rect(r.x0, r.y0, mid, r.y1)),
                                   ("right", fitz.Rect(mid, r.y0, r.x1, r.y1))):
                    label += 1
                    out.append(LogicalPage(i + 1, half, rect, str(label)))
            else:
                label += 1
                out.append(LogicalPage(i + 1, "full", r, str(label)))
    return out


def doc_logical_pages(meta: DocMeta, split: str = "manifest") -> list[LogicalPage]:
    """split: "manifest" = tách trừ keep_spread_pages; "all" = tách mọi trang đôi; "none" = không tách."""
    if split == "manifest":
        keep = tuple(meta.extra.get("keep_spread_pages", ()))
    elif split == "all":
        keep = ()
    elif split == "none":
        with fitz.open(meta.path) as doc:
            keep = tuple(range(1, len(doc) + 1))
    else:
        raise ValueError(split)
    return logical_pages(meta.path, keep)


def split_spreads(meta: DocMeta, split: str = "manifest") -> tuple[Path, list[LogicalPage]]:
    """Ghi một PDF mới, mỗi trang logic là một trang riêng (cho Docling)."""
    lps = doc_logical_pages(meta, split)
    if all(lp.half in ("full", "spread") for lp in lps):
        return meta.path, lps
    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f"{meta.doc_id}.split-{split}.pdf"
    with fitz.open(meta.path) as src, fitz.open() as dst:
        for lp in lps:
            page = dst.new_page(width=lp.rect.width, height=lp.rect.height)
            page.show_pdf_page(page.rect, src, lp.pdf_page - 1, clip=lp.rect)
        dst.save(out)
    return out, lps


# ---------- làm sạch ----------

CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\u00a0", " ").replace("\u00ad", "")
    text = CONTROL_CHARS.sub(" ", text)  # vd. \x07 ẩn giữa "9." và tiêu đề trong PDF An Gia
    text = re.sub(r"[ \t]+", " ", text)
    return "\n".join(line.rstrip() for line in text.splitlines())


def count_non_nfc(text: str) -> int:
    """Số ký tự tổ hợp (dấu rời) — khác 0 nghĩa là văn bản chưa ở dạng NFC."""
    return sum(1 for ch in text if unicodedata.combining(ch))


def _line_key(line: str) -> str:
    line = re.sub(r"^#+\s+", "", line.strip())  # Docling có thể nâng header chạy thành tiêu đề "## ..."
    return re.sub(r"\d+", "#", line.lower())


_NUMBERING_ONLY = re.compile(r"^[#.\s]*$")  # "1.16." đứng riêng một dòng là số mục, không phải header


def strip_repeated_lines(pages: list[Page], min_ratio: float = 0.4, max_len: int = 80,
                         extra: set[str] | None = None) -> tuple[list[Page], list[str]]:
    """Bỏ header/footer: dòng ngắn lặp lại (sau khi thay số bằng #) trên >= min_ratio số trang.

    extra: các key header/footer đã phát hiện từ parser khác (vd. lớp text PyMuPDF).
    """
    repeated = set(extra or ())
    if len(pages) >= 4:
        counts = Counter()
        for p in pages:
            counts.update({_line_key(l) for l in p.text.splitlines() if 0 < len(l.strip()) <= max_len})
        repeated |= {k for k, c in counts.items()
                     if c / len(pages) >= min_ratio and not _NUMBERING_ONLY.match(k)}
    if not repeated:
        return pages, []
    cleaned = []
    for p in pages:
        lines = [l for l in p.text.splitlines() if _line_key(l) not in repeated]
        cleaned.append(Page(**{**asdict(p), "text": "\n".join(lines).strip()}))
    return cleaned, sorted(repeated)


# ---------- parser ----------

def parse_pymupdf(meta: DocMeta, sort: bool = False, split: str = "manifest") -> list[Page]:
    """Text thô theo thứ tự content stream (sort=False) hoặc sắp theo vị trí (sort=True)."""
    pages = []
    with fitz.open(meta.path) as doc:
        for i, lp in enumerate(doc_logical_pages(meta, split)):
            text = doc[lp.pdf_page - 1].get_text("text", clip=lp.rect, sort=sort)
            pages.append(Page(i, lp.pdf_page, lp.half, lp.page_label, text))
    return pages


def pymupdf_tables(meta: DocMeta, page_label: str) -> list[list[list[str]]]:
    """Dùng find_tables() của PyMuPDF (phát hiện bảng theo đường kẻ) trên một trang logic."""
    lp = next(l for l in doc_logical_pages(meta) if l.page_label == page_label)
    pdf_page = lp.pdf_page
    with fitz.open(meta.path) as doc:
        tabs = doc[pdf_page - 1].find_tables(clip=lp.rect)
        return [t.extract() for t in tabs.tables]


_converter = None


def _docling_converter():
    global _converter
    if _converter is None:
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
        from docling.document_converter import DocumentConverter, PdfFormatOption

        opts = PdfPipelineOptions(do_ocr=False, do_table_structure=True)  # PDF có text layer, không cần OCR
        opts.table_structure_options.mode = TableFormerMode.ACCURATE
        _converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})
    return _converter


def parse_docling(meta: DocMeta, split: str = "manifest") -> list[Page]:
    """Markdown theo từng trang logic (bảng giữ ở dạng bảng Markdown)."""
    path, lps = split_spreads(meta, split)
    doc = _docling_converter().convert(path).document
    return [Page(i, lp.pdf_page, lp.half, lp.page_label, doc.export_to_markdown(page_no=i + 1))
            for i, lp in enumerate(lps)]


def run_parser(meta: DocMeta, parser: str, split: str = "manifest") -> tuple[list[Page], float]:
    t0 = time.perf_counter()
    if parser == "pymupdf":
        pages = parse_pymupdf(meta, split=split)
    elif parser == "pymupdf_sort":
        pages = parse_pymupdf(meta, sort=True, split=split)
    elif parser == "docling":
        pages = parse_docling(meta, split)
    else:
        raise ValueError(parser)
    return pages, time.perf_counter() - t0


def clean_pages(pages: list[Page], extra: set[str] | None = None) -> tuple[list[Page], list[str]]:
    pages = [Page(**{**asdict(p), "text": normalize(p.text)}) for p in pages]
    return strip_repeated_lines(pages, extra=extra)


# ---------- lưu / đọc ----------

def save_pages(doc_id: str, parser: str, pages: list[Page]) -> Path:
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / f"{doc_id}.{parser}.json"
    out.write_text(json.dumps([asdict(p) for p in pages], ensure_ascii=False, indent=1), encoding="utf-8")
    md = "\n\n".join(f"<!-- page {p.page_label} (pdf {p.pdf_page} {p.half}) -->\n{p.text}" for p in pages)
    (PARSED / f"{doc_id}.{parser}.md").write_text(md, encoding="utf-8")
    return out


def load_pages(doc_id: str, parser: str = "docling") -> list[Page]:
    data = json.loads((PARSED / f"{doc_id}.{parser}.json").read_text(encoding="utf-8"))
    return [Page(**d) for d in data]
