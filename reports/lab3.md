# Lab 3 – Hybrid search + Rerank

Notebook: `notebooks/lab3_hybrid_rerank.ipynb` · Code: `src/ragbv/store.py` (pgvector), `bm25.py`, `retrieval.py` · Số liệu thô: `reports/lab3_results.json` · Chi tiết từng câu: [`lab3_retrieval_details.md`](lab3_retrieval_details.md) (câu gốc), [`lab3_retrieval_details_nodiac.md`](lab3_retrieval_details_nodiac.md) (câu bỏ dấu)

## Thiết lập
- **Chunk:** `structure` của Lab 2 (398 chunk, breadcrumb + nội dung). Mọi phương pháp tìm trên `embed_text`.
- **Hạ tầng:** pgvector 0.8.7 (Docker, `pgvector/pgvector:pg16`, port 5433). Bảng `chunks` có index HNSW `vector_cosine_ops` (m=16, ef_construction=64, ef_search=40, tức tham số mặc định), cùng B-tree trên `(strategy, doc_id)`. Upsert theo `(strategy, chunk_id)`.
- **Golden set:** 20 câu có bằng chứng, chạy trên **2 bộ câu hỏi**:
  - câu gốc;
  - cùng 20 câu **đã bỏ dấu**, mô phỏng người dùng gõ không dấu ("Phi bao hiem … goi Bac cua Bao Viet An Gia…").
- Chấm điểm giống Lab 2: chunk đúng = đúng `doc_id` và chứa đủ đoạn trích `must_contain`.

| Thành phần | Cài đặt |
|---|---|
| `dense` | BGE-M3 dense (fp16), pgvector cosine |
| `bm25` | `rank_bm25` BM25Okapi. Tách từ tiếng Việt bằng **pyvi** (`người được bảo hiểm` thành `người`, `được`, `bảo_hiểm`). Chuẩn hoá NFC, chữ thường |
| `bm25_nd` | BM25 sau khi **bỏ dấu** cả văn bản lẫn câu hỏi (`đ`→`d`), tách theo âm tiết. Luôn dùng câu gốc của người dùng |
| `hybrid` | RRF(dense, bm25) |
| `hybrid3` | RRF(dense, bm25, bm25_nd) |
| RRF | `score(d) = Σ 1/(60 + rank_i(d))`, k=60 (Cormack và cộng sự, 2009). Chỉ dùng thứ hạng, không cần chuẩn hoá điểm cosine với BM25 |
| `+rerank` | 50 ứng viên đầu của RRF, chấm bằng cross-encoder **`BAAI/bge-reranker-v2-m3`** (fp16, max_length 512) trên cặp (câu hỏi, breadcrumb + nội dung) |
| `+filter` | Nhận diện sản phẩm trong câu hỏi bằng alias trong manifest. So khớp đã bỏ dấu, theo ranh giới từ ("An Gia", "Tâm An", "AVSK", "Manulife", "Dai-ichi"…). Sau đó chỉ tìm trong `doc_id` tương ứng (`WHERE doc_id = ANY(...)`, BM25 lọc tương tự). Không nhận ra sản phẩm thì không lọc |
| `+rewrite` | `gpt-4.1-mini` thêm dấu và mở rộng viết tắt (NĐBH, STBH, BMBH, HĐBH…) trước khi tìm. Dense, BM25 có dấu và reranker dùng câu đã viết lại; BM25 bỏ dấu vẫn dùng câu gốc |

## Kết quả

### Câu gốc (20 câu)
| Phương pháp | hit@1 | hit@3 | hit@5 | recall@5 | recall@10 | MRR |
|---|---|---|---|---|---|---|
| dense | 0.55 | 0.70 | 0.80 | 0.767 | 0.858 | 0.661 |
| bm25 | 0.50 | 0.65 | 0.80 | 0.750 | 0.817 | 0.616 |
| bm25_nd | 0.35 | 0.65 | 0.75 | 0.700 | 0.767 | 0.536 |
| hybrid (dense + bm25) | 0.60 | 0.80 | 0.85 | 0.792 | 0.842 | 0.711 |
| hybrid3 (+ bm25_nd) | 0.55 | 0.85 | 0.90 | 0.842 | 0.842 | 0.696 |
| hybrid3 + rerank | 0.65 | 0.95 | 0.95 | 0.900 | 0.925 | 0.792 |
| dense + filter | 0.55 | 0.75 | 0.90 | 0.867 | 0.883 | 0.679 |
| hybrid3 + rerank + filter | 0.70 | 0.95 | 0.95 | **0.925** | 0.925 | 0.817 |
| rewrite + hybrid3 + rerank + filter | 0.70 | 0.95 | 0.95 | **0.925** | 0.925 | **0.825** |

### Cùng 20 câu, bỏ dấu
| Phương pháp | hit@1 | hit@3 | hit@5 | recall@5 | recall@10 | MRR |
|---|---|---|---|---|---|---|
| dense | 0.10 | 0.15 | 0.30 | 0.300 | 0.500 | 0.178 |
| bm25 (có dấu) | 0.00 | 0.00 | 0.05 | 0.025 | 0.075 | 0.020 |
| bm25_nd | 0.35 | 0.65 | 0.75 | **0.700** | 0.767 | 0.536 |
| hybrid (dense + bm25) | 0.05 | 0.10 | 0.15 | 0.125 | 0.300 | 0.106 |
| hybrid3 | 0.10 | 0.25 | 0.45 | 0.450 | 0.700 | 0.238 |
| hybrid3 + rerank | 0.20 | 0.60 | 0.80 | 0.750 | 0.800 | 0.436 |
| dense + filter | 0.10 | 0.25 | 0.45 | 0.450 | 0.600 | 0.224 |
| hybrid3 + rerank + filter | 0.20 | 0.50 | 0.80 | 0.750 | 0.750 | 0.414 |
| rewrite + hybrid3 + rerank + filter | 0.70 | 0.95 | 0.95 | **0.925** | 0.925 | **0.817** |

### recall@5 theo loại câu (câu gốc)
| Loại | dense | bm25 | bm25_nd | hybrid3 | +rerank | +rerank+filter |
|---|---|---|---|---|---|---|
| comparison (2) | 0.17 | 0.25 | 0.25 | 0.42 | 0.75 | **1.00** |
| no_diacritics (2) | 0.00 | 0.25 | **0.75** | 0.50 | 0.75 | 0.75 |
| table_lookup (5) | 0.80 | 0.60 | 0.20 | 0.80 | 0.80 | 0.80 |
| fact, multi_condition, exclusion, versioning (11) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |

**Độ tin cậy:** chỉ có 20 câu, mỗi câu tương ứng 0.05 hit@k. Các bước nhảy lớn có hướng rõ: dense 0.77 → hybrid3 + rerank 0.90 trên câu gốc; 0.30 → 0.93 trên câu bỏ dấu. Các chênh lệch nhỏ, như giữa có và không có rewrite trên câu gốc, là nhiễu.

## Nhận xét

1. **Hybrid tốt hơn từng phương pháp đơn lẻ, và rerank là bước có lợi lớn nhất.** Trên câu gốc, recall@5 đi từ dense 0.767 → hybrid 0.792 → hybrid3 0.842 → hybrid3 + rerank **0.900**, MRR từ 0.661 lên **0.792**. Dense và BM25 bổ sung cho nhau đúng như lý thuyết: BM25 thắng ở G11 (hạng 2 so với 5, khớp đúng cụm "thai sản" + "An Vui Sống Khỏe"), dense thắng ở G07, G12 (cách diễn đạt khác văn bản). Rerank chủ yếu đẩy chunk đúng từ hạng 4–9 lên top-3. Ví dụ G12 [9, 3] → [3, 1]; G16 [—, 3, —] → [2, 3, 4], tức tìm đủ cả 3 sản phẩm.
2. **Câu gõ không dấu làm hỏng gần hết hệ thống, trừ BM25 bỏ dấu.** Dense rơi từ 0.767 xuống **0.300**, BM25 có dấu từ 0.750 xuống **0.025** (gần như không khớp được từ nào). Riêng `bm25_nd` giữ nguyên **0.700** ở cả hai bộ câu hỏi, vì nó vốn đã so khớp không dấu. Đưa `bm25_nd` vào RRF (hybrid3) kéo câu bỏ dấu từ 0.125 lên 0.450, thêm rerank lên 0.750. Nhưng chỉ khi **viết lại câu hỏi bằng LLM** mới phục hồi hoàn toàn: **0.925**, bằng đúng hiệu năng trên câu có dấu. Chi phí là 1 lệnh gọi LLM nhỏ cho mỗi câu hỏi.
3. **Lọc theo sản phẩm giải quyết câu so sánh.** Riêng lọc metadata đã đưa dense từ 0.767 lên 0.867. Với câu so sánh: hybrid3 + rerank 0.75 → +filter **1.00**. Ví dụ G17 (An Gia so với Manulife): không lọc thì chunk thai sản của AVSK, sản phẩm thứ ba, chen vào. Lọc theo 2 sản phẩm được nêu thì cả hai bằng chứng vào top-5 (hạng 1 và 5).
   - **Lưu ý quan trọng:** mọi câu golden đều **nêu tên sản phẩm**, nên kết quả lọc ở đây lạc quan hơn thực tế. Người dùng thật thường hỏi "hợp đồng của tôi có chi trả thai sản không?". Khi đó phải lấy sản phẩm từ **hợp đồng đã xác thực của người dùng** (API hợp đồng, Lab 6), hoặc hỏi lại người dùng.
4. **Rerank với câu không dấu có thể làm hỏng kết quả.** Cross-encoder được huấn luyện trên văn bản có dấu. Với câu bỏ dấu, nó đôi khi đẩy chunk đúng ra ngoài: G09 (bỏ dấu) xếp hạng [4, 4] ở hybrid3, nhưng **trượt top-10** sau rerank. Vì vậy với người dùng gõ không dấu, **viết lại câu hỏi phải đi trước rerank**.
5. **LLM viết lại cũng sai.** Có 2 ví dụ:
   - G19: "tu ky tai tuc" được thêm dấu thành "**Tự Ký** Tái Tục", trong khi đúng là "**Tử kỳ**".
   - G01 bỏ dấu: "goi Bac" giữ nguyên "**Bac**", đúng phải là "Bạc".

   Thêm dấu cho thuật ngữ chuyên ngành là bài toán mơ hồ (tử/tự, kỳ/ký, bạc/bác), và LLM không biết danh mục sản phẩm. Cách sửa: đưa **danh mục tên sản phẩm và tên gói** vào prompt viết lại, hoặc thay alias đã nhận diện bằng tên chuẩn trước khi gọi LLM. Dù sai, kết quả vẫn tốt vì `bm25_nd` dùng câu gốc và vẫn khớp được.
6. **Các câu còn trượt:**
   - **G03** (chi phí sinh Manulife): trượt ở mọi phương pháp. Nguyên nhân là lỗi parse ô gộp dọc của Lab 1 (dòng "E. Chi phí sinh" không có giá trị). Không có kỹ thuật truy xuất nào sửa được, phải sửa ở parser.
   - **G19 E1** ("1.21. Thời hạn bảo hiểm"): Điều 1 của Dai-ichi gồm 25 định nghĩa trên 4 trang, bị chia thành nhiều chunk có **cùng breadcrumb**. Phần chứa 1.21 không vào top-10. Cách sửa: chunk định nghĩa theo từng mục (1.1, 1.2…) thay vì cả Điều, hoặc thêm số mục vào breadcrumb.
   - **Thiếu sót của golden set:** trang tóm tắt Dai-ichi (trang 2) cũng ghi "Thời hạn bảo hiểm: 01 tháng". Đây là bằng chứng thay thế hợp lệ cho G19 mà golden set chưa liệt kê, cần bổ sung (`group`) khi duyệt.

## pgvector: overfiltering khi lọc metadata
Truy vấn lọc theo AVSK (57/398 chunk, khoảng 14%), `LIMIT 20`:

| Kế hoạch | ef_search | iterative_scan | Số dòng trả về |
|---|---|---|---|
| Mặc định (planner tự chọn) | 40 | off | 20 |
| Buộc dùng HNSW | 10 | off | **4** |
| Buộc dùng HNSW | 10 | relaxed_order | 20 |
| Buộc dùng HNSW | 40 | off | **8** |
| Buộc dùng HNSW | 40 | relaxed_order | 20 |

- Với 398 dòng, PostgreSQL **không dùng HNSW** mà quét rồi sắp xếp chính xác (kế hoạch `Limit → Sort`), nên luôn đúng. Phải tắt `enable_seqscan`, `enable_bitmapscan`, `enable_sort` mới thấy hành vi ở quy mô lớn.
- Khi dùng HNSW, pgvector áp `WHERE` **sau** khi duyệt `ef_search` ứng viên gần nhất. Chỉ khoảng 14% ứng viên thuộc AVSK, nên còn 4 dòng (ef=10) hoặc 8 dòng (ef=40) thay vì 20. Cách sửa: `hnsw.iterative_scan = relaxed_order` (pgvector ≥ 0.8), hoặc tăng `ef_search`, hoặc partition hay partial index theo trường lọc.
- Trong code, `store.search` tự bật `relaxed_order` khi có lọc `doc_ids`.

## Độ trễ (20 câu, GPU RTX 3050 Ti 4GB, p50 / p95, ms)
| Bước | p50 | p95 |
|---|---|---|
| Embed câu hỏi (BGE-M3) | 30 | 127 |
| pgvector top-50 | 7 | 9 |
| BM25 (pyvi) top-50 | 2 | 3 |
| BM25 bỏ dấu top-50 | 2 | 3 |
| RRF | 0.1 | 0.1 |
| Rerank 10 ứng viên | 471 | 500 |
| Rerank 20 ứng viên | 920 | 996 |
| Rerank 50 ứng viên | 2.372 | 2.501 |

**Đánh đổi số ứng viên rerank** (hybrid3 + rerank + filter, câu gốc):

| Số ứng viên | recall@5 | MRR | Rerank p50 |
|---|---|---|---|
| 10 | 0.892 | 0.825 | 471 ms |
| 20 | 0.900 | 0.767 | 920 ms |
| 50 | 0.925 | 0.817 | 2.372 ms |

Rerank chiếm hơn 90% độ trễ. Trên GPU 4GB, độ trễ tăng gần tuyến tính theo số ứng viên. Giảm từ 50 xuống 10 ứng viên làm recall@5 giảm 0.03 (trong mức nhiễu), còn MRR không giảm. Với corpus nhỏ, **10–20 ứng viên là đủ**. Ở production nên đặt ngưỡng theo p95 SLA và đo lại trên golden set lớn hơn. Một chi tiết nhỏ: lần rerank đầu tiên phải nạp model lên GPU, nên notebook có bước khởi động trước khi đo.

## Pipeline đề xuất sau Lab 3
```
câu hỏi → [rewrite: thêm dấu, mở rộng viết tắt, có danh mục sản phẩm]
        → [lọc sản phẩm: từ câu hỏi, hoặc từ hợp đồng của người dùng]
        → dense (pgvector, iterative scan) ∥ BM25 có dấu ∥ BM25 bỏ dấu    (top-50 mỗi nhánh)
        → RRF (k=60) → rerank bge-reranker-v2-m3 (10–20 ứng viên) → top-5
```
recall@5 = 0.925 trên cả câu gốc lẫn câu bỏ dấu. Câu còn trượt là do parse (G03) và do chunk định nghĩa quá dài (G19).

## Câu trả lời phỏng vấn rút ra
- **"Vì sao cần hybrid cho bảo hiểm?"** Số liệu: dense 0.767, BM25 0.750, hybrid3 0.842, thêm rerank 0.900. Hai nhánh sai ở những câu khác nhau. Với tiếng Việt cần **BM25 trên văn bản bỏ dấu**: với người dùng gõ không dấu, dense rơi xuống 0.30, BM25 có dấu xuống 0.03, còn BM25 bỏ dấu giữ 0.70.
- **"RRF hay convex combination?"** RRF không cần chuẩn hoá giữa điểm cosine và BM25, k=60 không cần tinh chỉnh. Convex combination cần dữ liệu để chỉnh α, mà 20 câu là quá ít.
- **"Rerank có đáng không?"** Có. Ở đây +0.06 recall@5 và +0.10 MRR. Tốn 0,5–2,4 giây trên GPU 4GB tùy số ứng viên. Có thể kiểm soát bằng số ứng viên (10–20), GPU mạnh hơn, hoặc cache. Lưu ý: cross-encoder kém với câu không dấu, nên viết lại câu hỏi trước khi rerank.
- **"Lọc metadata làm giảm recall?"** Có, do post-filtering trên HNSW (đã tái hiện được: còn 4/20 dòng). Sửa bằng iterative scan của pgvector 0.8, hoặc tăng ef_search, hoặc partition. Lọc đúng sản phẩm lại là cách hiệu quả nhất cho câu so sánh (0.75 → 1.00), nhưng ngoài thực tế sản phẩm phải lấy từ hợp đồng của người dùng, không chỉ từ câu hỏi.
- **"Query rewriting có rủi ro gì?"** LLM thêm dấu sai thuật ngữ ("Tự Ký" thay cho "Tử kỳ"). Cần cung cấp danh mục thuật ngữ và sản phẩm, đồng thời vẫn giữ một nhánh dùng câu gốc (BM25 bỏ dấu) làm lưới an toàn.
