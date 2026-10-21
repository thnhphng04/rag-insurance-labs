# Lab 2 – Chunking

Notebook: `notebooks/lab2_chunking.ipynb` · Code: `src/ragbv/chunking.py`, `embedding.py`, `metrics.py`, `contextual.py`, `golden.py` · Chunk: `data/chunks/*.jsonl` · Số liệu thô: `reports/lab2_results.json`

## Thiết lập
- Đầu vào: output Docling đã làm sạch của Lab 1 (6 tài liệu) và tables JSON.
- Embedding: BGE-M3 dense (fp16, GPU 4GB), cosine. Truy xuất trên **toàn corpus**, không lọc theo sản phẩm.
- Golden set: 20 câu có bằng chứng (`data/golden/golden_set.jsonl`, bản duyệt ở `golden_set_review.md`).
- Chấm điểm: một chunk là "đúng" nếu thuộc đúng `doc_id` và chứa đủ các đoạn trích `must_contain`. Cách chấm này **không phụ thuộc cách cắt**. Cả 4 chiến lược đều chứa trọn 28/28 bằng chứng trong ít nhất 1 chunk, nên recall tối đa có thể đạt là như nhau.
- Câu có nhiều bằng chứng: `recall@k` yêu cầu đủ mọi bằng chứng bắt buộc (câu so sánh cần cả 2–3 sản phẩm). Các bằng chứng cùng `group` thay thế được cho nhau (cùng nội dung lặp ở 2 chỗ).

| Chiến lược | Cách cắt | Thứ đem đi embed | Số chunk | Token TB / trung vị |
|---|---|---|---|---|
| fixed | cửa sổ 512 token, chồng lấp 64 | nội dung | 197 | 505 / 512 |
| recursive | `\n\n` → `\n` → câu → từ, ≤ 512 token, chồng lấp 64 | nội dung | 226 | 407 / 453 |
| structure | Chương/Phần › Điều › mục; bảng gom theo nhóm từ tables JSON; bỏ mục lục, biểu mẫu, bìa, trang tóm tắt trùng | **breadcrumb** + nội dung | 402 (101 chunk bảng) | 239 / 215 |
| structure_nobc | như structure | chỉ nội dung (ablation) | 402 | 239 / 215 |

## Kết quả (20 câu)

| Chiến lược | hit@1 | hit@3 | hit@5 | recall@5 | recall@10 | MRR |
|---|---|---|---|---|---|---|
| fixed | 0.25 | 0.65 | 0.70 | 0.633 | 0.808 | 0.452 |
| recursive | 0.45 | 0.65 | 0.75 | 0.708 | 0.800 | 0.578 |
| structure_nobc | 0.35 | 0.60 | 0.70 | 0.650 | 0.808 | 0.511 |
| **structure** | **0.60** | **0.70** | **0.85** | **0.783** | **0.858** | **0.691** |
| structure + ctx (AVSK) | 0.60 | 0.75 | 0.85 | 0.808 | 0.858 | 0.704 |

recall@5 theo loại câu hỏi:

| Loại | fixed | recursive | structure_nobc | structure |
|---|---|---|---|---|
| table_lookup (5) | 0.40 | 0.60 | 0.60 | **0.80** |
| exclusion (1) | 0.00 | 0.00 | 0.00 | **1.00** |
| fact (6) | 0.83 | 0.83 | 0.83 | 0.83 |
| multi_condition (3) | 1.00 | 1.00 | 1.00 | 1.00 |
| versioning (1) | 1.00 | 1.00 | 1.00 | 1.00 |
| comparison (2) | 0.58 | 0.58 | 0.25 | 0.58 |
| no_diacritics (2) | 0.25 | 0.50 | 0.25 | 0.25 |

**Lưu ý về độ tin cậy:** chỉ có 20 câu, nên 1 câu thay đổi tương ứng 0.05 điểm hit@k. Chênh lệch giữa structure và recursive (+0.075 recall@5, +0.11 MRR) có hướng nhất quán, nhưng chưa đủ để khẳng định có ý nghĩa thống kê. Cần golden set khoảng 100–200 câu.

## Nhận xét

1. **Chunk theo cấu trúc tốt nhất ở mọi metric, nhưng phần lớn lợi ích đến từ breadcrumb chứ không phải từ ranh giới cắt.** Cùng ranh giới cắt, khi bỏ breadcrumb (structure_nobc) thì recall@5 giảm từ 0.783 xuống 0.650, ngang mức fixed. Nguyên nhân: một chunk như "Điều 10.18 … y học cổ truyền, châm cứu" đứng một mình không nói nó thuộc **sản phẩm nào**. Corpus có 4 sản phẩm sức khỏe với điều khoản gần giống nhau, nên embedding không phân biệt được. Ví dụ G15 (đông y, AVSK): structure xếp hạng 2, structure_nobc hạng 7, recursive trượt top-10.
2. **Bảng là nơi chênh lệch rõ nhất** (table_lookup: fixed 0.40 so với structure 0.80). G01 (phí gói Bạc, 35 tuổi) chỉ structure tìm được (hạng 1). Với fixed và recursive, bảng biểu phí Markdown 7 cột có ô gộp lặp lại bị cắt ngang. Chunk dạng "Từ 31 đến 40 tuổi — ĐỒNG: 1.315.600; BẠC: 1.887.600; …" có section "A. Điều khoản chính" ngay trong breadcrumb.
3. **Chunk nhỏ hơn thì hit@1 cao hơn.** Kích thước trung vị 215 token so với 453–512 token, giúp hit@1 tăng từ 0.25 (fixed) lên 0.60. Chunk 512 token chứa 3–4 điều khoản khác nhau nên embedding bị "loãng".
4. **Câu không dấu thất bại ở mọi chiến lược.** G19 ("thoi han bao hiem … NDBH toi da bao nhieu tuoi") không tìm được bằng chứng nào trong top-10. Dense embedding BGE-M3 không bù được việc mất dấu và viết tắt. Đây là việc của Lab 3: viết lại câu hỏi (thêm dấu, mở rộng viết tắt) và BM25 trên văn bản đã bỏ dấu.
5. **Câu so sánh nhiều sản phẩm là điểm yếu cấu trúc của truy xuất 1 lượt.** Ở G17 (thai sản Kim Cương An Gia so với Manulife), top-5 bị chiếm bởi chunk thai sản của **AVSK**, một sản phẩm thứ ba không được hỏi. Chunking không sửa được điều này. Cần tách câu hỏi (query decomposition) và lọc theo sản phẩm (Lab 3 và Lab 6).
6. **Lỗi parse lan sang truy xuất.** G03 (chi phí sinh Manulife) trượt ở cả 4 chiến lược. Dòng "E. Chi phí sinh" trong chunk bảng không có giá trị vì Docling làm mất ô gộp dọc (lỗi 10 của Lab 1), nên chunk không có gì liên quan đến "chi trả như thế nào". Phải sửa ở tầng parsing.

## Bonus: Contextual Retrieval (AVSK)
Mỗi chunk structure của AVSK (58 chunk) được `gpt-4.1-mini` viết 1–2 câu ngữ cảnh dựa trên toàn văn tài liệu, rồi gắn vào trước breadcrumb. Ví dụ: "Đoạn trích thuộc Quy tắc, Điều khoản Sản phẩm bổ trợ của Bảo Việt Nhân thọ, nằm trong Chương I, Điều 1, giới thiệu các định nghĩa…".

| 6 câu có bằng chứng AVSK (G11–G16) | hit@1 | hit@3 | hit@5 | recall@5 | MRR |
|---|---|---|---|---|---|
| structure | 0.50 | 0.67 | 0.83 | 0.78 | 0.653 |
| structure + ctx | 0.50 | **0.83** | **1.00** | **0.94** | **0.708** |

- **Chi phí:** 58 lệnh gọi, 975.505 token input, trong đó **910.336 token (93%) được prompt caching** vì toàn văn tài liệu nằm ở đầu prompt, cộng 4.037 token output. Theo bảng giá gpt-4.1-mini tại thời điểm viết (0,40 / 0,10 / 1,60 USD mỗi 1 triệu token input / cached input / output), ước tính khoảng **0,12 USD** cho cả tài liệu. Lần chạy lại dùng cache nội bộ nên không tốn thêm.
- **Nhận xét:** lợi ích thêm nhỏ hơn so với breadcrumb (breadcrumb đã cung cấp phần lớn ngữ cảnh "sản phẩm nào, điều nào"), nhưng có. Với sản phẩm có cấu trúc lỏng hơn (ít tiêu đề, nhiều trang tóm tắt), Contextual Retrieval sẽ có ích hơn. Đây là cùng kết luận với bài của Anthropic, nhưng ở đây là tiếng Việt và cỡ mẫu rất nhỏ.

## Lỗi của chính chunker (đã sửa)
Phân tích lỗi phát hiện breadcrumb sai ở lần chạy đầu:
- **AVSK:** "Điều 8" bị gắn vào "Bảng Giới hạn bảo hiểm tối đa…", vì "bảng giới hạn" bị xếp là tiêu đề cấp 1 và thay chỗ "CHƯƠNG II".
- **Manulife:** "Điều 2. THỜI GIAN CHỜ" bị gắn vào "Chương trình Bảo hiểm", vì regex `chương` khớp cả "**Chương** trình".

Cách sửa: "Chương"/"Phần" phải kèm số, và bảng nằm trong Điều là cấp 3. Lần chạy đầu (breadcrumb sai) có recall@5 0.808 và MRR 0.643; sau khi sửa là 0.783 và 0.691. Hạng của câu đúng **tăng** ở nhiều câu (MRR +0.05), nhưng G11 tụt từ hạng 2 xuống 6, làm recall@5 giảm 1 câu. Với 20 câu, cần thận trọng khi đọc các chênh lệch cỡ 0.025–0.05.

Còn tồn tại: Dai-ichi có tiêu đề bị Docling gộp ("CHƯƠNG 1: … Điều 1: …") nên các Điều 2, 3 không thành tiêu đề riêng.

## Câu trả lời phỏng vấn rút ra
- **"Chọn chunk size thế nào?"** Không chọn bằng cảm tính. Đo recall@k và MRR trên golden set có bằng chứng ở mức đoạn trích. Ở đây chunk theo Điều/mục (trung vị khoảng 215 token) kèm breadcrumb thắng cửa sổ 512 token: MRR 0.69 so với 0.45.
- **"Sửa lỗi gì?"** Chunk mất ngữ cảnh sản phẩm và điều khoản, bảng bị cắt ngang. **Tốn gì?** Phụ thuộc chất lượng parsing (tiêu đề sai thì breadcrumb sai) và cần luật cấp tiêu đề riêng cho từng hãng. **Đo bằng gì?** Recall@5, MRR, và ablation bỏ breadcrumb.
- **Breadcrumb là cách "Contextual Retrieval miễn phí":** với tài liệu có cấu trúc tốt như quy tắc bảo hiểm, nó mang lại phần lớn lợi ích. Contextual Retrieval bằng LLM bổ sung thêm một chút, với chi phí khoảng 0,12 USD cho mỗi tài liệu 25 trang nhờ prompt caching.
- Chunking không sửa được câu không dấu, câu so sánh nhiều sản phẩm, và lỗi parse. Đó là việc của query rewriting, hybrid search, lọc metadata và parser.
