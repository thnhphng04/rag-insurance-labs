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

## Chi tiết các kỹ thuật chunk

### Phần chung cho mọi chiến lược
- **Đầu vào:** `data/parsed/{doc_id}.docling.json`. Mỗi trang là một `Page` có `page_label` (số trang in) và text Markdown đã chuẩn hóa NFC, đã bỏ ký tự điều khiển và header/footer (Lab 1).
- **Đơn vị đo:** token của **tokenizer BGE-M3** (XLM-RoBERTa, `BAAI/bge-m3`), cùng tokenizer với model embedding. Nhờ vậy "512 token" đúng bằng 512 token mà model nhìn thấy, không phải ước lượng theo số ký tự.
- **Mỗi chunk** (`Chunk` trong `chunking.py`) có 2 trường văn bản tách biệt:
  - `text`: nội dung gốc, dùng để **chấm điểm** (so khớp `must_contain`) và sau này đưa vào prompt cho LLM.
  - `embed_text`: thứ **đem đi embed**, có thể kèm breadcrumb hoặc câu ngữ cảnh.

  Tách như vậy để breadcrumb không "gian lận" khi chấm (breadcrumb chứa tên sản phẩm, có thể trùng từ khóa của đáp án).
- **Metadata:** `doc_id`, `page_labels` (các trang in mà chunk trải qua, dùng cho trích dẫn ở Lab 4), `section` (đường dẫn tiêu đề), `kind` (`text`/`table`), `n_tokens`. `chunk_id` là SHA-1 của `doc_id | strategy | embed_text`, nên cùng nội dung thì cùng id (dùng cho cache embedding và upsert ở Lab 3).

### 1. `fixed`: cửa sổ trượt theo token
1. Nối mọi trang của tài liệu thành một chuỗi, giữa các trang là `\n\n`. Bỏ các dòng `<!-- image -->`. Ghi lại vị trí ký tự bắt đầu của từng trang.
2. Tokenize cả chuỗi một lần với `return_offsets_mapping=True`, để biết mỗi token ứng với đoạn ký tự nào.
3. Lấy cửa sổ 512 token, bước nhảy 448 token (chồng lấp 64). Chuyển chỉ số token về vị trí ký tự để cắt **chuỗi gốc**, không giải mã ngược từ token, nên giữ nguyên dấu và khoảng trắng.
4. `page_labels` = các trang có khoảng ký tự giao với chunk.

Đặc điểm: không quan tâm cấu trúc, cắt cả giữa câu, giữa dòng bảng, giữa hai Điều. Chunk gần như luôn đủ 512 token (trung vị 512). Chồng lấp 64 token giảm rủi ro một ý bị cắt đôi nhưng không loại bỏ được.

### 2. `recursive`: cắt theo ranh giới tự nhiên
1. Dùng chuỗi liền mạch như `fixed`.
2. `RecursiveCharacterTextSplitter.from_huggingface_tokenizer` (LangChain), độ dài đo bằng tokenizer BGE-M3, `chunk_size=512`, `chunk_overlap=64`.
3. Thử cắt lần lượt theo `\n\n` (đoạn) → `\n` (dòng) → `". "` (câu) → `" "` (từ) → ký tự. Chỉ xuống cấp sau khi một đoạn vẫn dài hơn 512 token, nên ưu tiên giữ nguyên đoạn và dòng.
4. `add_start_index=True` cho vị trí bắt đầu của chunk để ánh xạ ra trang.

Đặc điểm: không cắt giữa câu và giữa dòng bảng Markdown (mỗi dòng bảng là 1 dòng văn bản), nhưng vẫn **không biết Điều nào kết thúc ở đâu**. Một chunk thường chứa đuôi Điều trước và đầu Điều sau (ví dụ chunk chứa Điều 8.1 bắt đầu bằng phần cuối Điều 7). Bảng dài vẫn bị chia ở giữa, các phần sau mất dòng tiêu đề cột.

### 3. `structure`: cắt theo cây tiêu đề + breadcrumb
**a) Lọc trang.** Bỏ các trang khai báo `exclude_pages` trong manifest: bìa, trang "bộ tài liệu", trang trống, bìa sau, biểu mẫu trống của Tâm An (trang 23, 25), và trang 1–2 của AVSK (trùng với tài liệu tóm tắt riêng, tức dedup).

**b) Tách khối.** Mỗi trang được chia thành các khối liên tiếp: `heading` (dòng bắt đầu `## `), `table` (các dòng liền nhau bắt đầu `|`) và `text` (còn lại).

**c) Xác định cấp tiêu đề.** Docling xuất mọi tiêu đề cùng mức `##`, nên cấp được suy ra bằng regex (`_level`):

| Cấp | Mẫu | Ví dụ |
|---|---|---|
| 1 | `Chương/Phần` **kèm số**, `Phụ lục`, `Điều khoản bổ sung`, `Bảng quyền lợi`, `Biểu phí`, `Bảng tỷ lệ` | "CHƯƠNG II: QUYỀN LỢI BẢO HIỂM", "PHẦN I: QUY ĐỊNH CHUNG", "ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN" |
| 2 | `Điều <số>`, số La Mã `I.`, `II -` | "Điều 8: Nguyên tắc trả…", "I. ĐỊNH NGHĨA" |
| 3 | mọi tiêu đề khác | "6.1. Quyền lợi Điều trị Nội trú", "2. Hiệu lực bảo hiểm" |

Phải yêu cầu "kèm số" vì nếu không, "**Chương** trình Bảo hiểm" (Manulife) sẽ bị nhận là cấp 1 (lỗi đã gặp, xem bên dưới).

**d) Duy trì stack tiêu đề.** Gặp tiêu đề cấp L thì bỏ khỏi stack mọi tiêu đề có cấp ≥ L, rồi đẩy tiêu đề mới vào. Stack lúc đó chính là đường dẫn Chương › Điều › mục của nội dung bên dưới.

**e) Tạo section.** Mỗi tiêu đề mở một section mới. Các dòng `text` sau đó được thêm vào section hiện tại, kể cả khi sang trang mới (`page_labels` ghi nhận mọi trang). Các xử lý đặc biệt:
- Tiêu đề "MỤC LỤC": bỏ toàn bộ nội dung đến tiêu đề tiếp theo.
- Section chỉ có tiêu đề, không có nội dung (ví dụ "I. ĐỊNH NGHĨA" đứng ngay trước "1. Công ty Bảo hiểm"): không tạo chunk, vì tiêu đề đã nằm trong breadcrumb của các section con.
- Gộp section ngắn: nếu section trước **ngắn hơn 60 token** và có **cùng cha** với section sau, gộp section sau vào. Ví dụ các định nghĩa 1.1, 1.2, 1.3 ngắn được gộp thành một chunk, thay vì nhiều chunk 20–30 token thiếu ngữ cảnh.
- Section dài hơn 400 token: chia tiếp bằng bộ cắt đệ quy (400 token, chồng lấp 48). Mọi phần giữ cùng breadcrumb.

**f) Bảng.** Không cắt bảng Markdown mà **dựng lại từ `tables/{doc_id}.tables.json`** (Lab 1):
1. Trong các bảng JSON **cùng trang**, chọn bảng có nhiều nhãn dòng (30 ký tự đầu) xuất hiện trong khối Markdown nhất. Bảng không khớp được thì bỏ qua: đó là mục lục, biểu mẫu, hoặc bảng 1 cột đã bị loại ở Lab 1.
2. Mỗi dòng dữ liệu viết thành `- {nhãn} — {cột}: {giá trị}; {cột}: {giá trị}; …`. Ô trống được bỏ.
3. Các dòng cùng `section` của bảng được gom vào một nhóm. `section` là các dòng tiêu đề nhóm, ví dụ "A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH", "B › 1. Điều trị ngoại trú". Mỗi nhóm thành một hoặc vài chunk, có dòng đầu `Bảng (tên các cột)`.
4. Breadcrumb của chunk bảng = sản phẩm › stack tiêu đề hiện tại › section của bảng.

Ví dụ chunk bảng (biểu phí An Gia):
```
[Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú…]
Bảng (CHƯƠNG TRÌNH BẢO HIỂM, CHƯƠNG TRÌNH BẢO HIỂM, ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG)
- Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000
- Từ 4 đến 6 tuổi — ĐỒNG: 1.450.000; …
```
So với Markdown, mỗi con số đi kèm tên gói và nhóm tuổi trên cùng dòng, không còn ô gộp lặp lại, không còn đường kẻ `|----|`, và tiêu đề nhóm (nội trú hay ngoại trú) nằm trong breadcrumb.

**g) Breadcrumb.** `embed_text = "[" + sản phẩm › đường dẫn tiêu đề + "]\n" + text`. Tên sản phẩm lấy từ `product` trong manifest (phần trước dấu " - "). Ví dụ chunk văn bản:
```
[An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM]
Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm
- 8.1. Bảo Việt Nhân thọ không trả quyền lợi … trong Thời gian chờ sau đây: …
- Quyền lợi Thai sản: 270 ngày; …
```
Tiêu đề của chính section nằm ở dòng đầu `text`, còn breadcrumb chứa các tiêu đề cha.

### 4. `structure_nobc`: ablation bỏ breadcrumb
Cùng chunk với `structure` (cùng `text`, ranh giới, số lượng), nhưng `embed_text = text`. Mục đích: tách riêng tác dụng của **ranh giới cắt theo cấu trúc** với tác dụng của **ngữ cảnh breadcrumb**.

### 5. `structure+ctx`: Contextual Retrieval (bonus, chỉ AVSK)
1. Lấy 58 chunk `structure` của AVSK.
2. Với mỗi chunk, gọi `gpt-4.1-mini` (temperature 0). Prompt gồm **toàn văn AVSK** (bỏ trang 1–2) đặt ở đầu, sau đó là đoạn trích, kèm yêu cầu viết 1–2 câu tiếng Việt nêu sản phẩm, công ty, chương/điều/phần và nội dung chính của đoạn.
3. Toàn văn ở đầu prompt giống hệt nhau giữa các lệnh gọi, nên OpenAI tự động **prompt caching** (93% token input được cache).
4. `embed_text = câu ngữ cảnh + "\n" + breadcrumb + text`. Kết quả cache trong `data/cache/contextual/` theo hash (model, toàn văn, nội dung chunk), nên chạy lại không tốn phí.
5. Các tài liệu khác giữ nguyên chunk `structure`.

### Hạn chế đã biết của chunk bảng (chưa sửa)
- **Một dòng bị tách lẻ do chia 2 lần.** `_table_chunks` chia nhóm theo ngưỡng 400 token nhưng chỉ đếm các dòng dữ liệu, không tính dòng `Bảng (…)` và breadcrumb. Sau đó `_split_long` lại cắt chunk bảng lần nữa bằng bộ cắt ký tự. Kết quả: nhóm "A" của biểu phí An Gia (9 dòng) thành 3 chunk, trong đó một chunk **chỉ có dòng 51–60 tuổi và không có dòng tiêu đề cột**. Cách sửa: chia nhóm theo dòng có tính cả tiêu đề và breadcrumb, và không cho `_split_long` cắt chunk bảng.
- **Dòng tiêu đề cột lặp tên cột nhãn:** "Bảng (CHƯƠNG TRÌNH BẢO HIỂM, CHƯƠNG TRÌNH BẢO HIỂM, ĐỒNG, …)", vì ô gộp 2 cột nhãn được liệt kê 2 lần. Nên chỉ liệt kê các cột giá trị.
- **Kế thừa lỗi parse của Lab 1:** nhãn Nha khoa bị cắt ("Từ 1 đến" / "4. Bảo hiểm Nha khoa 18 tuổi Từ 19 đến 65 tuổi"), các dòng Manulife mất giá trị do ô gộp dọc ("E. Chi phí sinh" không có giá trị, nên G03 trượt).
- **Ghép bảng JSON với khối Markdown bằng nhãn dòng** có thể chọn nhầm nếu một trang có 2 bảng giống nhau. Chưa gặp trong corpus này.

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
