# RAG & Agentic RAG Labs – Bảo hiểm tiếng Việt

7 lab thực hành RAG trên quy tắc bảo hiểm công khai (Bảo Việt, Bảo Việt Nhân thọ, Manulife, Dai-ichi), bám theo kế hoạch ôn tập trong `Kế hoạch ôn tập 2 ngày…md`.

| Lab | Chủ đề | Trạng thái |
|---|---|---|
| 1 | Parsing (PyMuPDF vs Docling) | ✅ [`reports/lab1.md`](reports/lab1.md) |
| – | Golden set (20 câu + 5 ngoài phạm vi) | ✅ [`data/golden/golden_set_review.md`](data/golden/golden_set_review.md) |
| 2 | Chunking (fixed / recursive / cấu trúc + breadcrumb / contextual) | ✅ [`reports/lab2.md`](reports/lab2.md) |
| 3 | Hybrid search + rerank (pgvector, BM25 có/không dấu, RRF, bge-reranker, lọc sản phẩm, rewrite) | ✅ [`reports/lab3.md`](reports/lab3.md) |
| 4 | Generation có trích dẫn | ⏳ |
| 5 | Eval (RAGAS + LangFuse) | ⏳ |
| 6 | CRAG-lite (LangGraph) | ⏳ |
| 7 | Prompt injection | ⏳ |

## Cấu trúc
```
data/raw/        PDF gốc (đổi tên)        data/manifest.yaml  metadata + doc_id
data/parsed/     output Lab 1             src/ragbv/          code dùng chung
notebooks/       1 notebook / lab         reports/            kết quả từng lab
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
