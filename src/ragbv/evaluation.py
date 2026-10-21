"""Lab 5: RAGAS + LLM-as-judge đối chiếu nhãn người."""
from __future__ import annotations

import hashlib
import json

import pandas as pd

from .config import CACHE, env

JUDGE_CACHE = CACHE / "judge"

RAGAS_METRICS = ["faithfulness", "answer_relevancy", "llm_context_precision_with_reference",
                 "context_recall", "factual_correctness(mode=f1)"]


def ragas_eval(rows: list[dict], model: str | None = None) -> pd.DataFrame:
    """rows: {question, answer, contexts, reference}. Trả về DataFrame điểm từng câu."""
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from ragas import EvaluationDataset, RunConfig, evaluate
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.llms import LangchainLLMWrapper
    from ragas.metrics import (FactualCorrectness, Faithfulness, LLMContextPrecisionWithReference,
                               LLMContextRecall, ResponseRelevancy)

    model = model or env("GRADER_MODEL", "gpt-4.1-mini")
    llm = LangchainLLMWrapper(ChatOpenAI(model=model, temperature=0, api_key=env("OPENAI_API_KEY")))
    emb = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small", api_key=env("OPENAI_API_KEY")))
    ds = EvaluationDataset.from_list([{"user_input": r["question"], "response": r["answer"],
                                       "retrieved_contexts": r["contexts"], "reference": r["reference"]} for r in rows])
    res = evaluate(ds, metrics=[Faithfulness(), ResponseRelevancy(), LLMContextPrecisionWithReference(),
                                LLMContextRecall(), FactualCorrectness()],
                   llm=llm, embeddings=emb, run_config=RunConfig(max_workers=8, timeout=180), show_progress=False)
    return res.to_pandas()


JUDGE_PROMPT = """Bạn chấm câu trả lời của chatbot bảo hiểm so với đáp án chuẩn do chuyên gia viết.
Chỉ so về NỘI DUNG (số liệu, điều kiện, kết luận), không chấm văn phong.

Câu hỏi: {question}
Đáp án chuẩn: {reference}
Câu trả lời của chatbot: {answer}

Chọn đúng một nhãn:
- "dung_du": đúng và đủ các ý chính của đáp án chuẩn (có thể thiếu chi tiết phụ không ảnh hưởng kết luận).
- "thieu_y": các ý nêu ra đều đúng nhưng thiếu ít nhất một ý quan trọng của đáp án chuẩn.
- "sai": có ít nhất một thông tin sai hoặc mâu thuẫn với đáp án chuẩn (số liệu, thời hạn, điều kiện).
- "tu_choi": chatbot từ chối hoặc nói không có thông tin.
Trả về JSON: {{"label": "...", "reason": "một câu giải thích"}}"""


def judge(question: str, reference: str, answer: str, model: str | None = None) -> dict:
    model = model or env("GRADER_MODEL", "gpt-4.1-mini")
    JUDGE_CACHE.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(json.dumps([model, JUDGE_PROMPT, question, reference, answer], ensure_ascii=False).encode()).hexdigest()
    f = JUDGE_CACHE / f"{key}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    from openai import OpenAI

    resp = OpenAI(api_key=env("OPENAI_API_KEY")).chat.completions.create(
        model=model, temperature=0, response_format={"type": "json_object"},
        messages=[{"role": "user", "content": JUDGE_PROMPT.format(question=question, reference=reference, answer=answer)}])
    out = json.loads(resp.choices[0].message.content)
    f.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    return out
