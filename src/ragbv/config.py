"""Đường dẫn dự án, biến môi trường và manifest tài liệu."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"
PARSED = DATA / "parsed"
CACHE = DATA / "cache"
GOLDEN = DATA / "golden"
REPORTS = ROOT / "reports"

load_dotenv(ROOT / ".env")


def env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)


@dataclass
class DocMeta:
    doc_id: str
    file: str
    product: str
    insurer: str
    doc_type: str
    page_layout: str
    page_ranges: dict = field(default_factory=dict)
    extra: dict = field(default_factory=dict)

    @property
    def path(self) -> Path:
        return DATA / self.file


def load_manifest() -> dict[str, DocMeta]:
    raw = yaml.safe_load((DATA / "manifest.yaml").read_text(encoding="utf-8"))
    docs = {}
    for d in raw["documents"]:
        known = {k: d.pop(k) for k in
                 ("doc_id", "file", "product", "insurer", "doc_type", "page_layout", "page_ranges")}
        docs[known["doc_id"]] = DocMeta(**known, extra=d)
    return docs
