# RAG & Agentic RAG Labs – Bảo hiểm tiếng Việt

7 lab thực hành RAG trên quy tắc bảo hiểm công khai (Bảo Việt, Bảo Việt Nhân thọ, Manulife, Dai-ichi), bám theo kế hoạch ôn tập trong `Kế hoạch ôn tập 2 ngày…md`.

| Lab | Chủ đề | Trạng thái |
|---|---|---|
| 1 | Parsing (PyMuPDF vs Docling) | ✅ [`reports/lab1.md`](reports/lab1.md) |
| – | Golden set (20 câu + 5 ngoài phạm vi) | ✅ [`data/golden/golden_set_review.md`](data/golden/golden_set_review.md) |
| 2 | Chunking (fixed / recursive / cấu trúc + breadcrumb / contextual) | ✅ [`reports/lab2.md`](reports/lab2.md) |
| 3 | Hybrid search + rerank (pgvector, BM25 có/không dấu, RRF, bge-reranker, lọc sản phẩm, rewrite) | ✅ [`reports/lab3.md`](reports/lab3.md) |
| 4 | Generation có trích dẫn, từ chối, hậu kiểm trích dẫn | ✅ [`reports/lab4.md`](reports/lab4.md) |
| 5 | Eval: RAGAS, LLM-as-judge đối chiếu nhãn người, tracing (LangFuse chưa bật, xem issues) | ✅ [`reports/lab5.md`](reports/lab5.md) |
| 6 | CRAG-lite bằng LangGraph (grade, transform, grounding, tách câu con theo sản phẩm) | ✅ [`reports/lab6.md`](reports/lab6.md) |
| 7 | Prompt injection qua tài liệu: 3 payload × 3 prompt, output guard, quét khi nạp | ✅ [`reports/lab7.md`](reports/lab7.md) |

**Vấn đề hiện hữu của cả 7 lab và các quyết định cần duyệt: [`reports/issues.md`](reports/issues.md)**

## Cấu trúc
```
data/raw/        PDF gốc (đổi tên)        data/manifest.yaml  metadata + doc_id + aliases
data/parsed/     output Lab 1             src/ragbv/          code dùng chung
data/golden/     golden set               data/chunks/        chunk Lab 2
data/runs/       câu trả lời Lab 4        data/traces/        trace JSONL (Lab 5)
notebooks/       1 notebook / lab         reports/            kết quả từng lab + issues.md
infra/langfuse/  LangFuse self-host       docker-compose.yml  pgvector (port 5433)
```

## Cài đặt
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
# torch CUDA cài SAU (docling kéo về bản CPU) – xem ghi chú đầu requirements.txt
.\.venv\Scripts\python.exe -m pip install --force-reinstall --no-deps torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/cu126
.\.venv\Scripts\python.exe -m ipykernel install --user --name ragbv
copy .env.example .env   # điền OPENAI_API_KEY
```
LangFuse: tạo `infra/langfuse/.env` (secret + `LANGFUSE_INIT_*`), rồi `docker compose up -d` trong thư mục đó; UI ở http://localhost:3000.
