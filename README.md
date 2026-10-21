# RAG & Agentic RAG Labs â€“ Báº£o hiá»ƒm tiáº¿ng Viá»‡t

7 lab thá»±c hÃ nh RAG trÃªn quy táº¯c báº£o hiá»ƒm cÃ´ng khai (Báº£o Viá»‡t, Báº£o Viá»‡t NhÃ¢n thá», Manulife, Dai-ichi), bÃ¡m theo káº¿ hoáº¡ch Ã´n táº­p trong `Káº¿ hoáº¡ch Ã´n táº­p 2 ngÃ yâ€¦md`.

| Lab | Chá»§ Ä‘á» | Tráº¡ng thÃ¡i |
|---|---|---|
| 1 | Parsing (PyMuPDF vs Docling) | âœ… [`reports/lab1.md`](reports/lab1.md) |
| â€“ | Golden set (20 cÃ¢u + 5 ngoÃ i pháº¡m vi) | âœ… [`data/golden/golden_set_review.md`](data/golden/golden_set_review.md) |
| 2 | Chunking (fixed / recursive / cáº¥u trÃºc + breadcrumb / contextual) | âœ… [`reports/lab2.md`](reports/lab2.md) |
| 3 | Hybrid search + rerank (pgvector, BM25 cÃ³/khÃ´ng dáº¥u, RRF, bge-reranker, lá»c sáº£n pháº©m, rewrite) | âœ… [`reports/lab3.md`](reports/lab3.md) |
| 4 | Generation cÃ³ trÃ­ch dáº«n | â³ |
| 5 | Eval (RAGAS + LangFuse) | â³ |
| 6 | CRAG-lite (LangGraph) | â³ |
| 7 | Prompt injection | â³ |

## Cáº¥u trÃºc
```
data/raw/        PDF gá»‘c (Ä‘á»•i tÃªn)        data/manifest.yaml  metadata + doc_id
data/parsed/     output Lab 1             src/ragbv/          code dÃ¹ng chung
notebooks/       1 notebook / lab         reports/            káº¿t quáº£ tá»«ng lab
infra/langfuse/  LangFuse self-host       docker-compose.yml  pgvector (port 5433)
```

## CÃ i Ä‘áº·t
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
# torch CUDA cÃ i SAU (docling kÃ©o vá» báº£n CPU) â€“ xem ghi chÃº Ä‘áº§u requirements.txt
.\.venv\Scripts\python.exe -m pip install --force-reinstall --no-deps torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/cu126
.\.venv\Scripts\python.exe -m ipykernel install --user --name ragbv
copy .env.example .env   # Ä‘iá»n OPENAI_API_KEY
```
LangFuse: táº¡o `infra/langfuse/.env` (secret + `LANGFUSE_INIT_*`), rá»“i `docker compose up -d` trong thÆ° má»¥c Ä‘Ã³; UI á»Ÿ http://localhost:3000.
