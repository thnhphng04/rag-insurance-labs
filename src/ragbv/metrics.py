"""Metric truy xuất trên golden set, chấm bằng golden.is_relevant (không phụ thuộc cách chunk)."""
from __future__ import annotations

import re

from .chunking import Chunk
from .golden import Item, is_relevant


def evidence_ranks(item: Item, ranked: list[Chunk]) -> list[int | None]:
    """Hạng (1-based) của chunk đầu tiên khớp từng bằng chứng; None nếu không có trong danh sách."""
    out = []
    for ev in item.evidence:
        out.append(next((r for r, c in enumerate(ranked, 1) if is_relevant(c.text, c.doc_id, ev)), None))
    return out


def score_item(item: Item, ranked: list[Chunk], ks=(1, 3, 5, 10)) -> dict:
    """
    hit@k    : có ít nhất 1 bằng chứng trong top-k
    recall@k : tỉ lệ bằng chứng có trong top-k (câu so sánh cần đủ mọi bằng chứng)
    mrr      : 1/hạng của chunk đúng đầu tiên
    Bằng chứng cùng `group` là thay thế nhau (cùng nội dung ở 2 chỗ): chỉ cần 1 trong nhóm.
    """
    ranks = evidence_ranks(item, ranked)
    groups = _groups(item, ranks)
    res = {"id": item.id, "type": item.type}
    for k in ks:
        res[f"hit@{k}"] = float(any(r is not None and r <= k for g in groups for r in g))
        res[f"recall@{k}"] = sum(any(r is not None and r <= k for r in g) for g in groups) / len(groups)
    first = min((r for g in groups for r in g if r is not None), default=None)
    res["mrr"] = 1 / first if first else 0.0
    res["ranks"] = ranks
    return res


def details_markdown(items: list[Item], ranked: dict[str, list[list[Chunk]]], title: str,
                     k_show: int = 5, snippet: int = 160) -> str:
    """Báo cáo đọc được: mỗi câu golden, mỗi chiến lược, top-k chunk trả về và chunk nào đúng.

    ranked[strategy][i] = danh sách chunk đã xếp hạng (top-10) cho items[i].
    """
    def one_line(s: str) -> str:
        s = re.sub(r"-{4,}", "---", " ".join(s.split()))  # đường kẻ bảng Markdown dài chiếm hết đoạn trích
        return (s[:snippet] + "…" if len(s) > snippet else s).replace("|", "\\|")

    lines = [f"# {title}", "",
             "Sinh tự động. ✅ = chunk chứa đủ đoạn trích của bằng chứng (E1, E2… theo thứ tự trong golden set). "
             f"Hiển thị top-{k_show}; hạng của bằng chứng tính đến top-10 (`—` = ngoài top-10).", ""]
    for i, item in enumerate(items):
        lines += [f"## {item.id} · {item.type}", "", f"**Câu hỏi:** {item.question}", "",
                  f"**Đáp án chuẩn:** {item.answer}", ""]
        for j, ev in enumerate(item.evidence, 1):
            alt = f" (nhóm thay thế `{ev.group}`)" if ev.group else ""
            lines.append(f"- **E{j}**{alt}: `{ev.doc_id}` · {ev.section} · tr.{ev.page_label} · "
                         f"cần chứa: {', '.join(repr(s) for s in ev.must_contain)}")
        lines += ["", "| Chiến lược | Hạng bằng chứng | recall@5 |", "|---|---|---|"]
        for name, per_item in ranked.items():
            r = score_item(item, per_item[i])
            ranks = ", ".join(f"E{j}: {x if x else '—'}" for j, x in enumerate(r["ranks"], 1))
            lines.append(f"| {name} | {ranks} | {r['recall@5']:.2f} |")
        lines.append("")
        for name, per_item in ranked.items():
            lines += [f"<details><summary>{name}: top-{k_show}</summary>", "",
                      "| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |", "|---|---|---|---|---|"]
            for rank, c in enumerate(per_item[i][:k_show], 1):
                hits = [f"E{j}" for j, ev in enumerate(item.evidence, 1) if is_relevant(c.text, c.doc_id, ev)]
                mark = "✅ " + ",".join(hits) if hits else ""
                lines.append(f"| {rank} | {mark} | `{c.doc_id}` · {','.join(c.page_labels)} | "
                             f"{one_line(c.section) if c.section else ''} | {one_line(c.text)} |")
            lines += ["", "</details>", ""]
    return "\n".join(lines) + "\n"


def _groups(item: Item, ranks: list) -> list[list]:
    groups: dict[str, list] = {}
    for i, (ev, r) in enumerate(zip(item.evidence, ranks)):
        groups.setdefault(ev.group or f"#{i}", []).append(r)
    return list(groups.values())
