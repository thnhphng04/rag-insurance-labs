"""Trace từng bước của pipeline RAG.

Nếu LangFuse self-host (infra/langfuse) đang chạy và có key trong .env -> gửi trace lên LangFuse.
Nếu không -> ghi JSONL cục bộ vào data/traces/ (cùng cấu trúc: trace -> các span có input/output/thời gian).
"""
from __future__ import annotations

import json
import time
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone

from .config import DATA, env

TRACES = DATA / "traces"


def langfuse_available(timeout: float = 2.0) -> bool:
    host, pk = env("LANGFUSE_HOST"), env("LANGFUSE_PUBLIC_KEY")
    if not host or not pk:
        return False
    try:
        import urllib.request

        with urllib.request.urlopen(f"{host}/api/public/health", timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


class Tracer:
    """tracer.trace(name, input) -> Trace; trace.span(name, input) là context manager ghi output và thời gian."""

    def __init__(self, run_name: str, force_local: bool = False):
        self.run_name = run_name
        self.backend = "local" if force_local or not langfuse_available() else "langfuse"
        self._lf = None
        if self.backend == "langfuse":
            from langfuse import get_client

            self._lf = get_client()
        TRACES.mkdir(parents=True, exist_ok=True)
        self.path = TRACES / f"{run_name}.jsonl"
        self.path.write_text("", encoding="utf-8")

    @contextmanager
    def trace(self, name: str, input: dict, metadata: dict | None = None):
        t = _Trace(self, name, input, metadata or {})
        try:
            yield t
        finally:
            t.close()

    def flush(self) -> None:
        if self._lf is not None:
            self._lf.flush()


class _Trace:
    def __init__(self, tracer: Tracer, name: str, input: dict, metadata: dict):
        self.tracer, self.name, self.input, self.metadata = tracer, name, input, metadata
        self.id = uuid.uuid4().hex
        self.spans: list[dict] = []
        self.output = None
        self.scores: dict[str, float] = {}
        self.t0 = time.perf_counter()
        self._lf_ctx = None
        if tracer._lf is not None:  # LangFuse SDK v3+ (OpenTelemetry): observation gốc cho cả trace
            lf = tracer._lf
            start = getattr(lf, "start_as_current_observation", None) or getattr(lf, "start_as_current_span")
            self._lf_ctx = start(name=name, input=input, metadata=metadata)
            self._lf_root = self._lf_ctx.__enter__()

    @contextmanager
    def span(self, name: str, input=None):
        rec = {"name": name, "input": input, "start": time.perf_counter()}
        lf_ctx = None
        if self.tracer._lf is not None:
            lf = self.tracer._lf
            start = getattr(lf, "start_as_current_observation", None) or getattr(lf, "start_as_current_span")
            lf_ctx = start(name=name, input=input)
            lf_span = lf_ctx.__enter__()
        try:
            yield rec
        finally:
            rec["duration_ms"] = round((time.perf_counter() - rec.pop("start")) * 1000, 1)
            self.spans.append(rec)
            if lf_ctx is not None:
                lf_span.update(output=rec.get("output"), metadata={"duration_ms": rec["duration_ms"]})
                lf_ctx.__exit__(None, None, None)

    def score(self, name: str, value: float) -> None:
        self.scores[name] = value

    def close(self) -> None:
        total = round((time.perf_counter() - self.t0) * 1000, 1)
        rec = {"trace_id": self.id, "run": self.tracer.run_name, "name": self.name,
               "time": datetime.now(timezone.utc).isoformat(), "input": self.input, "output": self.output,
               "metadata": self.metadata, "duration_ms": total, "spans": self.spans, "scores": self.scores}
        with self.tracer.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        if self._lf_ctx is not None:
            self._lf_root.update(output=self.output)
            for k, v in self.scores.items():
                score = getattr(self._lf_root, "score_trace", None) or getattr(self._lf_root, "score", None)
                if score:
                    score(name=k, value=v)
            self._lf_ctx.__exit__(None, None, None)
