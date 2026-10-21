"""Metric truy xuất trên golden set, chấm bằng golden.is_relevant (không phụ thuộc cách chunk)."""
from __future__ import annotations

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


def _groups(item: Item, ranks: list) -> list[list]:
    groups: dict[str, list] = {}
    for i, (ev, r) in enumerate(zip(item.evidence, ranks)):
        groups.setdefault(ev.group or f"#{i}", []).append(r)
    return list(groups.values())
