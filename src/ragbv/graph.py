"""Lab 6: CRAG-lite bằng LangGraph.

prepare -> retrieve -> grade_documents -┬-(có tài liệu liên quan)-> generate -> check_grounding -┬-> finish -> END
                ^                        ├-(không, còn lượt)-> transform_query -┬-> retrieve      ├-(không đạt, chưa sinh lại)-> regenerate -> check_grounding
                |________________________|______________________________________|              └-(vẫn không đạt)-> fallback -> END
                                         |                                      └-(truy vấn lặp lại)-> fallback
                                         └-(không, hết lượt)-> fallback -> END

- prepare: viết lại câu hỏi (thêm dấu, mở rộng viết tắt); câu nêu >= 2 sản phẩm thì tách câu con theo sản phẩm.
- grade_documents: LLM chấm từng chunk có giúp trả lời không (CRAG: Correct/Incorrect).
- check_grounding: LLM kiểm tra từng ý của câu trả lời có được tài liệu hỗ trợ không (kiểu ISSUP của Self-RAG).
"""
from __future__ import annotations

import hashlib
import json
from typing import TypedDict

from .chunking import Chunk
from .config import CACHE, DocMeta, env
from . import generation as G, retrieval as R

LLM_CACHE = CACHE / "graph_llm"
MAX_TRANSFORMS = 2
FALLBACK = ("Hiện tài liệu quy tắc, điều khoản chưa có đủ thông tin để trả lời chính xác câu hỏi này. "
            "Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.")


def _llm_json(prompt: str, model: str | None = None) -> tuple[dict, dict]:
    """Gọi LLM trả JSON, có cache. Trả về (kết quả, usage)."""
    model = model or env("GRADER_MODEL", "gpt-4.1-mini")
    LLM_CACHE.mkdir(parents=True, exist_ok=True)
    f = LLM_CACHE / (hashlib.sha1(f"{model}|{prompt}".encode()).hexdigest() + ".json")
    if f.exists():
        d = json.loads(f.read_text(encoding="utf-8"))
        return d["out"], {**d["usage"], "cached": True}
    from openai import OpenAI

    resp = OpenAI(api_key=env("OPENAI_API_KEY")).chat.completions.create(
        model=model, temperature=0, response_format={"type": "json_object"},
        messages=[{"role": "user", "content": prompt}])
    out = json.loads(resp.choices[0].message.content)
    usage = {"prompt_tokens": resp.usage.prompt_tokens, "completion_tokens": resp.usage.completion_tokens}
    f.write_text(json.dumps({"out": out, "usage": usage}, ensure_ascii=False), encoding="utf-8")
    return out, {**usage, "cached": False}


GRADE_PROMPT = """Bạn chấm mức liên quan của các đoạn tài liệu bảo hiểm với câu hỏi của khách hàng.
Một đoạn là "co" nếu nó chứa thông tin giúp trả lời TRỰC TIẾP ít nhất một phần câu hỏi (đúng sản phẩm được hỏi, đúng nội dung).
Một đoạn là "khong" nếu nó chỉ cùng chủ đề chung chung, thuộc sản phẩm khác sản phẩm được hỏi, hoặc không chứa số liệu/quy định cần thiết.

Câu hỏi: {question}

{docs}

Trả về JSON: {{"grades": [{{"id": "D1", "relevant": "co" | "khong"}}, ...]}}"""

TRANSFORM_PROMPT = """Câu hỏi sau chưa tìm được đoạn tài liệu quy tắc bảo hiểm phù hợp.
Hãy viết lại thành MỘT câu truy vấn tìm kiếm khác: dùng thuật ngữ hay xuất hiện trong quy tắc, điều khoản bảo hiểm
(ví dụ "Thời hạn bảo hiểm", "Thời gian chờ", "Người được bảo hiểm", "Bên mua bảo hiểm", "Điều khoản loại trừ"),
giữ tên sản phẩm, bỏ phần không cần thiết. Không trả lời câu hỏi.

Câu hỏi gốc: {question}
Các truy vấn đã thử: {tried}

Trả về JSON: {{"query": "..."}}"""

GROUNDING_PROMPT = """Kiểm tra câu trả lời của chatbot bảo hiểm có được các đoạn tài liệu hỗ trợ hay không.
Tách câu trả lời thành các ý. Một ý "duoc_ho_tro" nếu tài liệu nói rõ điều đó (không cần suy luận thêm).
Một ý "khong" nếu tài liệu không nói, nói khác, hoặc ý đó ghép các quy định khác nhau thành kết luận mới.

{docs}

Câu trả lời: {answer}

Trả về JSON: {{"claims": [{{"claim": "...", "verdict": "duoc_ho_tro" | "khong"}}], "grounded": true | false}}
("grounded" = true khi và chỉ khi mọi ý đều được hỗ trợ.)"""

PARTIAL_RULES = """Với câu hỏi gồm nhiều phần hoặc so sánh nhiều sản phẩm: trả lời từng phần có thông tin trong tài liệu,
và nói rõ phần nào tài liệu chưa có. Chỉ đặt status = "khong_du_thong_tin" khi KHÔNG phần nào trả lời được."""

REGENERATE_RULES = """Lần trả lời trước có ý không được tài liệu hỗ trợ: {unsupported}
Hãy trả lời lại: chỉ nêu những gì tài liệu nói rõ; phần nào câu hỏi hỏi mà tài liệu không có thì nói rõ là tài liệu chưa có thông tin đó.
Nếu không còn ý nào trả lời được, đặt status = "khong_du_thong_tin"."""


def _docs_block(chunks: list[Chunk], prefix: str = "D") -> str:
    """Kèm breadcrumb (muc): chunk là phần sau của một Điều dài không có tiêu đề Điều trong text."""
    return "\n\n".join(f'<doan id="{prefix}{i}" san_pham="{G.product_name(c)}" muc="{c.section}">\n{c.text}\n</doan>'
                       for i, c in enumerate(chunks, 1))


class State(TypedDict, total=False):
    question: str
    queries: list[dict]          # [{query, doc_ids}] (câu con theo sản phẩm hoặc 1 câu)
    tried: list[str]
    documents: list[Chunk]
    relevant: list[Chunk]
    transforms: int
    answer: dict
    grounding: dict
    regenerated: bool
    final: dict
    log: list[dict]


def build_graph(ret: R.Retriever, docs: dict[str, DocMeta], k_per_query: int = 5, max_docs: int = 8):
    from langgraph.graph import END, START, StateGraph

    def log(state, node, **info):
        return state.get("log", []) + [{"node": node, **info}]

    def prepare(state: State) -> State:
        q = state["question"]
        rewritten = R.rewrite(q)
        found = R.product_filter(q, docs) or []
        products: dict[str, list[str]] = {}
        for d in found:  # gom doc theo sản phẩm (AVSK có 2 doc: QTĐK + tóm tắt)
            products.setdefault(docs[d].product.split(" - ")[0], []).append(d)
        if len(products) >= 2:
            queries = [{"query": f"{rewritten} (chỉ xét sản phẩm {name})", "doc_ids": ids} for name, ids in products.items()]
        else:
            queries = [{"query": rewritten, "doc_ids": found or None}]
        return {"queries": queries, "tried": [x["query"] for x in queries], "transforms": 0, "regenerated": False,
                "log": log(state, "prepare", rewritten=rewritten, sub_queries=len(queries))}

    def retrieve(state: State) -> State:
        seen, out = set(), []
        for q in state["queries"]:
            for c in ret.run(q["query"], "hybrid3+rerank", k=k_per_query, n_cand=20, doc_ids=q["doc_ids"]):
                if c.chunk_id not in seen:
                    seen.add(c.chunk_id)
                    out.append(c)
        return {"documents": out[:max_docs], "log": log(state, "retrieve", n=len(out[:max_docs]))}

    def grade_documents(state: State) -> State:
        d = state["documents"]
        res, usage = _llm_json(GRADE_PROMPT.format(question=state["question"], docs=_docs_block(d)))
        keep = {g["id"] for g in res.get("grades", []) if g.get("relevant") == "co"}
        rel = [c for i, c in enumerate(d, 1) if f"D{i}" in keep]
        return {"relevant": rel, "log": log(state, "grade_documents", kept=len(rel), of=len(d), usage=usage)}

    def after_grade(state: State) -> str:
        if state["relevant"]:
            return "generate"
        return "transform_query" if state["transforms"] < MAX_TRANSFORMS else "fallback"

    def transform_query(state: State) -> State:
        res, usage = _llm_json(TRANSFORM_PROMPT.format(question=state["question"], tried=state["tried"]))
        q = res.get("query") or state["question"]
        doc_ids = R.product_filter(state["question"], docs)
        repeated = q in state["tried"]  # truy vấn lặp lại -> tìm lại cũng vô ích, đi thẳng fallback
        return {"queries": [{"query": q, "doc_ids": doc_ids}], "tried": state["tried"] + [q],
                "transforms": MAX_TRANSFORMS if repeated else state["transforms"] + 1,
                "relevant": [], "log": log(state, "transform_query", query=q, repeated=repeated, usage=usage)}

    def after_transform(state: State) -> str:
        return "fallback" if state["log"][-1].get("repeated") else "retrieve"

    def generate(state: State) -> State:
        out = G.generate(state["question"], state["relevant"], "basic", extra_rules=PARTIAL_RULES)
        return {"answer": out, "log": log(state, "generate", status=out["status"], usage=out["usage"])}

    def check_grounding(state: State) -> State:
        a = state["answer"]
        if a["status"] == "khong_du_thong_tin":
            return {"grounding": {"grounded": True, "claims": []}, "log": log(state, "check_grounding", skipped="tu_choi")}
        res, usage = _llm_json(GROUNDING_PROMPT.format(docs=_docs_block(state["relevant"], "C"), answer=a["answer"]),
                               model=env("GROUNDING_MODEL", "gpt-4.1"))
        res["grounded"] = bool(res.get("grounded")) and all(c.get("verdict") == "duoc_ho_tro" for c in res.get("claims", []))
        return {"grounding": res, "log": log(state, "check_grounding", grounded=res["grounded"],
                                             unsupported=[c["claim"] for c in res.get("claims", []) if c.get("verdict") != "duoc_ho_tro"],
                                             usage=usage)}

    def after_check(state: State) -> str:
        if state["grounding"]["grounded"]:
            return "finish"
        return "fallback" if state["regenerated"] else "regenerate"

    def regenerate(state: State) -> State:
        bad = [c["claim"] for c in state["grounding"].get("claims", []) if c.get("verdict") != "duoc_ho_tro"]
        out = G.generate(state["question"], state["relevant"], "basic",
                         extra_rules=PARTIAL_RULES + "\n\n" + REGENERATE_RULES.format(unsupported=bad))
        return {"answer": out, "regenerated": True, "log": log(state, "regenerate", status=out["status"], usage=out["usage"])}

    def finish(state: State) -> State:
        return {"final": {**state["answer"], "route": "answer", "contexts": state["relevant"]}, "log": log(state, "finish")}

    def fallback(state: State) -> State:
        return {"final": {"status": "khong_du_thong_tin", "answer": FALLBACK, "citations": [], "route": "fallback",
                          "contexts": state.get("relevant", [])}, "log": log(state, "fallback")}

    g = StateGraph(State)
    for name, fn in [("prepare", prepare), ("retrieve", retrieve), ("grade_documents", grade_documents),
                     ("transform_query", transform_query), ("generate", generate), ("check_grounding", check_grounding),
                     ("regenerate", regenerate), ("finish", finish), ("fallback", fallback)]:
        g.add_node(name, fn)
    g.add_edge(START, "prepare")
    g.add_edge("prepare", "retrieve")
    g.add_edge("retrieve", "grade_documents")
    g.add_conditional_edges("grade_documents", after_grade, ["generate", "transform_query", "fallback"])
    g.add_conditional_edges("transform_query", after_transform, ["retrieve", "fallback"])
    g.add_edge("generate", "check_grounding")
    g.add_conditional_edges("check_grounding", after_check, ["finish", "regenerate", "fallback"])
    g.add_edge("regenerate", "check_grounding")
    g.add_edge("finish", END)
    g.add_edge("fallback", END)
    return g.compile()
