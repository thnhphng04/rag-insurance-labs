"""Trích bảng từ DoclingDocument thành bản ghi JSON (mỗi dòng dữ liệu = 1 record).

Khác với Markdown, ô gộp (span) không bị chép lặp: dòng có một ô trải hết bề ngang là
tiêu đề nhóm và trở thành trường `section` của các dòng bên dưới.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .config import PARSED
from .parsing import normalize

TABLES = PARSED / "tables"

# Số mục "N. Chữ hoa" nằm GIỮA nhãn dòng -> dấu hiệu ranh giới dòng bị cắt sai,
# vd. "Điều trị viêm nướu, viêm nha chu 5. Bảo hiểm Thai sản".
_EMBEDDED_ITEM = re.compile(r"^(?P<prefix>.*\S)\s+(?P<num>\d{1,2})\.\s+(?P<rest>\S.*)$")
_STRUCTURE_WORD = re.compile(r"\b(điều|chương|khoản|mục|phần)$", re.IGNORECASE)  # "Điều 2." là số Điều
_PAGE_NUMBER = re.compile(r"^[.\s…]*(trang\s*)?\d{1,3}$", re.IGNORECASE)
_LEADING_ITEM = re.compile(r"^(\d{1,2})\.\s")
_DATA_LIKE = re.compile(r"\d")
# Nhãn kết thúc bằng từ nối -> ô bị cắt dở sang dòng khác (vd. "Từ 1 đến" | "... 18 tuổi").
_DANGLING = re.compile(r"\b(đến|từ|và|hoặc|của|cho|với)$", re.IGNORECASE)


@dataclass
class Record:
    row: int
    section: list[str]
    label: str
    values: dict[str, str]
    note: str | None = None


@dataclass
class Table:
    doc_id: str
    table_id: int
    page_label: str
    columns: list[str]
    label_columns: list[int]
    continued_from: int | None
    records: list[Record] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)


def _grid(t) -> list[list]:
    """Lưới num_rows x num_cols; ô gộp được tham chiếu ở mọi vị trí nó phủ (cùng object)."""
    d = t.data
    g = [[None] * d.num_cols for _ in range(d.num_rows)]
    for c in d.table_cells:
        for r in range(c.start_row_offset_idx, c.end_row_offset_idx):
            for k in range(c.start_col_offset_idx, c.end_col_offset_idx):
                g[r][k] = c
    return g


def _full_width(row: list, ncols: int) -> bool:
    cells = {id(c) for c in row if c is not None}
    return ncols > 1 and len(cells) == 1 and row[0] is not None and \
        row[0].end_col_offset_idx - row[0].start_col_offset_idx == ncols


def _text(cell) -> str:
    """Text ô đã chuẩn hóa NFC, bỏ ký tự điều khiển (DoclingDocument giữ nguyên \\x07 của PDF)."""
    return normalize(cell.text).replace("\n", " ").strip() if cell is not None else ""


def _row_texts(row: list, cols: range) -> list[str]:
    """Text các ô trong cols, mỗi ô gộp chỉ lấy một lần."""
    seen, out = set(), []
    for k in cols:
        c = row[k]
        if c is not None and id(c) not in seen:
            seen.add(id(c))
            out.append(_text(c))
    return [t for t in out if t]


def _header_rows(g: list[list]) -> int:
    n = 0
    for row in g:
        if any(c is not None and c.column_header for c in row) and not _full_width(row, len(row)):
            n += 1
        else:
            break
    return n


def _columns(g: list[list], n_header: int) -> list[str]:
    ncols = len(g[0])
    names = []
    for k in range(ncols):
        parts = []
        for r in range(n_header):
            t = _text(g[r][k])
            if t and t not in parts:
                parts.append(t)
        names.append(" / ".join(parts) or f"col{k}")
    return names


def _label_columns(g: list[list], n_header: int) -> list[int]:
    """Các cột nằm dưới ô header đầu tiên (vd. 'CHƯƠNG TRÌNH BẢO HIỂM' gộp 2 cột)."""
    if n_header and g[0][0] is not None:
        c = g[0][0]
        return list(range(c.start_col_offset_idx, c.end_col_offset_idx))
    return [0]


def extract_tables(doc, doc_id: str, page_labels: dict[int, str]) -> list[Table]:
    """page_labels: page_no của Docling (1-based, theo PDF đã tách trang đôi) -> nhãn trang in."""
    out: list[Table] = []
    prev: Table | None = None
    prev_page = None
    for i, t in enumerate(doc.tables):
        if t.data.num_cols < 2 or t.data.num_rows < 2:
            continue  # mục lục / danh sách bị nhận nhầm là bảng
        page_no = t.prov[0].page_no
        g = _grid(t)
        n_header = _header_rows(g)

        # Bảng nối trang: cùng số cột, ngay trang sau, và "header" trông như dữ liệu (chứa số)
        header_text = " ".join(_row_texts(g[0], range(len(g[0])))) if n_header else ""
        continues = (prev is not None and prev_page == page_no - 1 and len(prev.columns) == t.data.num_cols
                     and (n_header == 0 or _DATA_LIKE.search(header_text)))
        if continues:
            n_header, columns, label_cols = 0, prev.columns, prev.label_columns
        else:
            columns, label_cols = _columns(g, n_header), _label_columns(g, n_header)

        table = Table(doc_id, i, page_labels.get(page_no, str(page_no)), columns, label_cols,
                      prev.table_id if continues else None)
        value_cols = [k for k in range(len(columns)) if k not in label_cols]
        section = list(prev.records[-1].section[:1]) if continues and prev.records else []

        for r in range(n_header, len(g)):
            row = g[r]
            if _full_width(row, len(columns)):
                section = [_text(row[0])]
                continue
            label = " ".join(_row_texts(row, range(label_cols[0], label_cols[-1] + 1))).lstrip("• ").strip()
            label_cells = {id(row[k]) for k in label_cols if row[k] is not None}
            # Ô gộp phủ cả cột nhãn và cột giá trị (vd. "I - CHẾT" c0-2) chỉ tính là nhãn
            values = {columns[k]: _text(row[k]) for k in value_cols
                      if row[k] is not None and id(row[k]) not in label_cells}
            # Dòng tiêu đề phụ lặp lại tên cột, vd. "1. Điều trị ngoại trú | ĐỒNG | BẠC | ..."
            if values and all(v == k for k, v in values.items()):
                section = section[:1] + [label]
                continue
            # Mục đánh số mới ("2. BH Tai nạn…") kết thúc tiêu đề phụ đánh số trước đó
            if len(section) > 1 and _LEADING_ITEM.match(section[-1]) and _LEADING_ITEM.match(label):
                section = section[:1]
            if not label and not any(values.values()):
                continue
            table.records.append(Record(r, list(section), label, values))

        if _is_toc(table):
            continue  # mục lục: cột cuối là số trang
        _repair_labels(table)
        out.append(table)
        prev, prev_page = table, page_no
    return out


def _is_toc(table: Table) -> bool:
    last = [list(r.values.values())[-1] for r in table.records if r.values]
    return len(last) >= 3 and sum(bool(_PAGE_NUMBER.match(v)) for v in last) / len(last) >= 0.7


def _repair_labels(table: Table) -> None:
    """Sửa nhãn bị cắt sai ranh giới dòng: chuyển phần đầu sang dòng trước nếu dòng trước là mục N-1.

    Nhãn bị cắt dở (kết thúc bằng từ nối) chỉ được ghi vào issues, không tự sửa.
    """
    for rec in table.records:
        if _DANGLING.search(rec.label):
            table.issues.append(f"trang {table.page_label}, dòng {rec.row}: nhãn '{rec.label}' bị cắt dở"
                                " -> chưa sửa, cần kiểm tra tay")
        if rec.label and not any(rec.values.values()):
            # Thường do ô gộp dọc chỉ được gán cho một dòng (vd. Manulife 1.3 mục C.1-C.8, 1.4 dòng E, G).
            # Cũng có thể là dòng tiêu đề nhóm hợp lệ -> chỉ báo, không tự sửa.
            table.issues.append(f"trang {table.page_label}, dòng {rec.row}: '{rec.label[:60]}' không có giá trị"
                                " nào -> có thể mất ô gộp dọc, cần kiểm tra tay")
    for j in range(1, len(table.records)):
        rec, before = table.records[j], table.records[j - 1]
        m = _EMBEDDED_ITEM.match(rec.label)
        if not m or not m["rest"][0].isupper() or _STRUCTURE_WORD.search(m["prefix"]):
            continue
        lead = _LEADING_ITEM.match(before.label)
        msg = f"trang {table.page_label}, dòng {rec.row}: nhãn '{rec.label[:70]}' chứa mục {m['num']}. ở giữa"
        if lead and int(lead.group(1)) == int(m["num"]) - 1:
            before.label = f"{before.label} {m['prefix']}"
            before.note = f"đã nhận thêm '{m['prefix']}' từ dòng {rec.row}"
            rec.label = f"{m['num']}. {m['rest']}"
            rec.note = f"đã chuyển '{m['prefix']}' lên dòng {before.row}"
            table.issues.append(msg + " -> đã sửa")
        else:
            table.issues.append(msg + " -> chưa sửa (dòng trước không phải mục liền kề)")


def records_as_rows(table: Table) -> list[str]:
    """Mỗi record thành một dòng 'nhãn v1 v2 ...' để chấm bằng eval_parsing.score_table."""
    return [" ".join([r.label, *r.values.values()]) for r in table.records]


def save_tables(doc_id: str, tables: list[Table]) -> Path:
    TABLES.mkdir(parents=True, exist_ok=True)
    out = TABLES / f"{doc_id}.tables.json"
    out.write_text(json.dumps([asdict(t) for t in tables], ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def load_tables(doc_id: str) -> list[dict]:
    return json.loads((TABLES / f"{doc_id}.tables.json").read_text(encoding="utf-8"))
