"""Lab 1: đo chất lượng parsing bằng ground truth chép tay từ ảnh trang PDF."""
from __future__ import annotations

import re
import unicodedata

from .parsing import CONTROL_CHARS, Page, count_non_nfc

# Biểu phí An Gia (trang in 26), đơn vị VND/người/năm: Đồng, Bạc, Vàng, Bạch Kim, Kim Cương.
# 9 dòng đầu = điều khoản chính (nội trú), 9 dòng sau = ngoại trú (cùng nhãn tuổi).
_AGES = ["Từ 1 đến 3 tuổi", "Từ 4 đến 6 tuổi", "Từ 7 đến 9 tuổi", "Từ 10 đến 18 tuổi", "Từ 19 đến 30 tuổi",
         "Từ 31 đến 40 tuổi", "Từ 41 đến 50 tuổi", "Từ 51 đến 60 tuổi", "Từ 61 đến 65 tuổi"]
_ANGIA_MAIN = [
    "2.585.000 3.707.000 5.616.000 7.582.000 9.267.000",
    "1.450.000 2.081.000 3.153.000 4.257.000 5.203.000",
    "1.320.000 1.900.000 2.867.000 3.870.000 4.730.000",
    "1.255.800 1.801.800 2.730.000 3.685.500 4.504.500",
    "1.196.000 1.716.000 2.600.000 3.510.000 4.290.000",
    "1.315.600 1.887.600 2.860.000 3.861.000 4.719.000",
    "1.375.400 1.973.400 2.990.000 4.036.500 4.933.500",
    "1.435.200 2.059.200 3.120.000 4.212.000 5.148.000",
    "1.554.800 2.230.800 3.380.000 4.563.000 5.577.000",
]
_ANGIA_OUT = [
    "3.370.000 3.370.000 3.370.000 5.516.000 8.424.000",
    "1.900.000 1.900.000 1.900.000 3.153.000 4.730.000",
    "1.720.000 1.720.000 1.720.000 2.867.000 4.300.000",
    "1.638.000 1.638.000 1.638.000 2.730.000 4.095.000",
    "1.560.000 1.560.000 1.560.000 2.600.000 3.900.000",
    "1.716.000 1.716.000 1.716.000 2.860.000 4.290.000",
    "1.794.000 1.794.000 1.794.000 2.990.000 4.485.000",
    "1.872.000 1.872.000 1.872.000 3.120.000 4.680.000",
    "2.028.000 2.028.000 2.028.000 3.380.000 5.070.000",
]
# Biểu phí Tâm An (trang in 21): Phúc, Lộc, Thọ.
_TAMAN = [
    "2.635.000 5.716.000 7.832.000", "1.500.000 3.253.000 4.507.000", "1.370.000 2.967.000 4.120.000",
    "1.305.800 2.830.000 3.935.500", "1.246.000 2.700.000 3.760.000", "1.365.600 2.960.000 4.111.000",
    "1.425.400 3.090.000 4.286.500", "1.485.200 3.220.000 4.462.000", "1.604.800 3.480.000 4.813.000",
]
# Bảng quyền lợi An Gia (trang in 24-25, bảng trải ngang trang đôi), theo thứ tự xuất hiện.
_ANGIA_BENEFIT = [
    ("xe cứu thương", "5.000.000 5.000.000 10.000.000 10.000.000 10.000.000"),
    ("phẫu thuật (không", "40.000.000 60.000.000 100.000.000 150.000.000 200.000.000"),
    ("phục hồi chức năng", "4.000.000 6.000.000 10.000.000 15.000.000 20.000.000"),
    ("trợ cấp bệnh viện công", "80.000 120.000 200.000 300.000 400.000"),
    ("thai sản", "21.000.000 31.500.000"),
]

TABLE_TESTS = {
    "angia_bieu_phi": {
        "doc_id": "bv-angia-2016", "page_label": "26",
        "rows": [(a, v) for a, v in zip(_AGES, _ANGIA_MAIN)] + [(a, v) for a, v in zip(_AGES, _ANGIA_OUT)],
    },
    "taman_bieu_phi": {
        "doc_id": "bv-taman-2019", "page_label": "21",
        "rows": list(zip(_AGES, _TAMAN)),
    },
    "angia_quyen_loi": {
        "doc_id": "bv-angia-2016", "page_label": "24-25",
        "rows": _ANGIA_BENEFIT,
    },
}

# Định nghĩa An Gia, trang in 4-5, bố cục 2 cột mỗi trang. Thứ tự đúng = 1..21.
ANGIA_DEFINITIONS = [
    "Công ty Bảo hiểm", "Người được bảo hiểm", "Người yêu cầu bảo hiểm", "Người phụ thuộc", "Người thụ hưởng",
    "Tuổi được bảo hiểm", "Hợp đồng bảo hiểm", "Bảng quyền lợi bảo hiểm", "Tổng hạn mức", "Giới hạn phụ",
    "Ngày hiệu lực bảo hiểm", "Thời hạn bảo hiểm", "Thời gian chờ", "Phạm vi lãnh thổ", "Tai nạn",
    "Thương tật thân thể", "Thương tật bộ phận", "Thương tật/tàn tật toàn bộ", "Ốm đau, bệnh tật",
    "Bệnh/thương tật có sẵn", "Bệnh đặc biệt",
]


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower()
    return re.sub(r"\s+", " ", s.replace("|", " ").replace("*", " ")).strip()


def _page(pages: list[Page], label: str) -> Page | None:
    return next((p for p in pages if p.page_label == label), None)


def _rows_from_text(text: str) -> list[str]:
    """Một 'dòng' của bảng = một dòng văn bản (Markdown: '| a | b |', text thô: một dòng)."""
    return [_norm(l) for l in text.splitlines() if l.strip()]


def _values_in_order(row: str, values: list[str]) -> int:
    """Số giá trị khớp theo đúng thứ tự cột trong cùng một dòng."""
    pos, hit = 0, 0
    for v in values:
        i = row.find(v, pos)
        if i >= 0:
            hit, pos = hit + 1, i + len(v)
    return hit


def _squash(s: str) -> str:
    """Bỏ mọi khoảng trắng và dấu chấm: '2.585.000' ~ '2585000\\n. .', 'Từ 1 đến 3 tuổi' ~ 'Từ1đến3tuổi'."""
    return re.sub(r"[\s.]", "", _norm(s))


def score_table(rows_text: list[str], gt_rows: list[tuple[str, str]], page_text: str,
                lenient: bool = False) -> dict:
    """
    value_recall : tỉ lệ ô số xuất hiện ở đâu đó trên trang (text có được trích ra không).
    row_integrity: tỉ lệ ô nằm đúng dòng và đúng thứ tự cột (cấu trúc bảng có giữ được không).
    lenient      : so khớp sau khi bỏ khoảng trắng/dấu chấm -> chỉ đo cấu trúc, bỏ qua lỗi ký tự trong ô.
    """
    f = _squash if lenient else _norm
    flat = f(page_text)
    rows_text = [f(r) for r in rows_text]
    total = sum(len(v.split()) for _, v in gt_rows)
    present = sum(1 for _, v in gt_rows for x in v.split() if f(x) in flat)
    in_row, ptr = 0, 0
    for label, vals in gt_rows:
        key, values = f(label), [f(v) for v in vals.split()]
        for j in range(ptr, len(rows_text)):
            if key in rows_text[j]:
                in_row += _values_in_order(rows_text[j], values)
                ptr = j + 1
                break
    return {"cells": total, "value_recall": round(present / total, 3), "row_integrity": round(in_row / total, 3)}


def table_report(pages: list[Page], test: str) -> dict:
    t = TABLE_TESTS[test]
    p = _page(pages, t["page_label"])
    if p is None:
        return {"cells": 0, "value_recall": 0.0, "row_integrity": 0.0, "note": f"không có trang {t['page_label']}"}
    return score_table(_rows_from_text(p.text), t["rows"], p.text)


def table_report_rows(rows: list[list[str]], test: str, page_text: str, lenient: bool = False) -> dict:
    """Cho output dạng list-of-cells (vd. PyMuPDF find_tables)."""
    rows_text = [" ".join(c or "" for c in r) for r in rows]
    return score_table(rows_text, TABLE_TESTS[test]["rows"], page_text, lenient)


def reading_order(pages: list[Page], labels=("4", "5"), titles=ANGIA_DEFINITIONS) -> dict:
    """Tìm vị trí 'n. <tiêu đề>' trong văn bản; điểm = độ dài dãy con tăng dài nhất / số tiêu đề."""
    text = _norm("\n".join(p.text for p in pages if p.page_label in labels))
    positions = []
    for n, title in enumerate(titles, 1):
        m = re.search(rf"(?<!\d){n}\s*\.\s*{re.escape(_norm(title))}", text)
        positions.append(m.start() if m else None)
    found = [p for p in positions if p is not None]
    lis = _lis_len(found)
    return {"found": f"{len(found)}/{len(titles)}", "in_order": round(lis / len(titles), 3),
            "order": [i + 1 for i, _ in sorted(((i, p) for i, p in enumerate(positions) if p is not None),
                                               key=lambda x: x[1])]}


def _lis_len(xs: list[int]) -> int:
    import bisect
    tails: list[int] = []
    for x in xs:
        k = bisect.bisect_left(tails, x)
        tails[k:k + 1] = [x]
    return len(tails)


VI_PROBES = ["bảo hiểm", "người được bảo hiểm", "quyền lợi", "điều trị", "thời gian chờ"]


def text_quality(pages: list[Page], raw: list[Page] | None = None) -> dict:
    """Kiểm tra dấu tiếng Việt: ký tự lỗi, ký tự chưa NFC, tần suất cụm từ khóa."""
    text = "\n".join(p.text for p in pages)
    low = unicodedata.normalize("NFC", text).lower()
    return {
        "chars": len(text),
        "replacement_chars": text.count("�"),
        "private_use_chars": sum(1 for c in text if 0xE000 <= ord(c) <= 0xF8FF),
        "non_nfc_marks": count_non_nfc(text),
        "control_chars_before_clean": sum(len(CONTROL_CHARS.findall(p.text)) for p in raw) if raw else None,
        **{f"'{w}'": low.count(w) for w in VI_PROBES[:3]},
        "empty_pages": sum(1 for p in pages if len(p.text.strip()) < 30),
    }
