# Lab 1 – Parsing PDF bảo hiểm tiếng Việt

Notebook: `notebooks/lab1_parsing.ipynb` · Code: `src/ragbv/parsing.py`, `src/ragbv/eval_parsing.py` · Số liệu thô: `reports/lab1_results.json`

## Thiết lập
- Corpus: 6 PDF trong `data/raw/` (xem `data/manifest.yaml`).
- So sánh 3 cách parse + 1 biến thể bảng:
  - `pymupdf`: text thô theo thứ tự content stream
  - `pymupdf_sort`: text sắp lại theo tọa độ (`sort=True`)
  - `docling`: layout model + TableFormer (ACCURATE), tắt OCR vì PDF có text layer
  - `pymupdf_find_tables`: phát hiện bảng theo đường kẻ, chỉ chạy trên các trang bảng
- Ground truth chép tay từ ảnh trang: biểu phí An Gia (90 ô), biểu phí Tâm An (27 ô), 5 dòng bảng quyền lợi An Gia (22 ô), thứ tự 21 định nghĩa An Gia (trang in 4–5, mỗi trang 2 cột).
- Làm sạch: chuẩn hóa NFC, bỏ ký tự điều khiển, bỏ header/footer lặp lại.

## Kết quả

### Bảng: `row_integrity` = tỉ lệ ô nằm đúng dòng và đúng thứ tự cột
| Parser | Biểu phí An Gia | Biểu phí Tâm An | Quyền lợi An Gia (trải ngang trang đôi) |
|---|---|---|---|
| pymupdf | 0.00 | 0.00 | 0.00 |
| pymupdf_sort | 1.00 | 1.00 | 1.00 |
| pymupdf_find_tables | 0.00 | 0.00 | 0.00 |
| pymupdf_find_tables (bỏ qua lỗi ký tự) | 1.00 | 1.00 | 1.00 |
| **docling** | **1.00** | **1.00** | **1.00** |

Cả 4 cách đều có `value_recall` = 1.0, tức là mọi con số đều có trong text. Khác biệt chỉ nằm ở chỗ con số còn gắn với đúng dòng (độ tuổi) và đúng cột (chương trình) hay không.

### Thứ tự đọc (định nghĩa 1→21, trang 2 cột)
| Parser | Tìm thấy | Đúng thứ tự (LIS/21) |
|---|---|---|
| pymupdf | 21/21 | 1.000 |
| pymupdf_sort | 21/21 | **0.619** (đọc xen 2 cột: 6,1,7,2,8,3…) |
| docling | 21/21 | 1.000 |

### Tách trang đôi (An Gia, Docling, bảng quyền lợi)
| Chế độ | row_integrity |
|---|---|
| Tách mọi trang đôi làm 2 nửa | **0.227** |
| Giữ nguyên trang 13 (`keep_spread_pages` trong manifest) | 1.000 |

### Thời gian (RTX 3050 Ti 4GB)
Docling mất 63.7 giây cho cả corpus (An Gia 32 giây). PyMuPDF mất dưới 1 giây cho mỗi tài liệu.

### Dấu tiếng Việt
Cả 6 PDF có text layer tốt: 0 ký tự lỗi (U+FFFD), 0 ký tự private-use, 0 dấu tổ hợp chưa NFC với mọi parser. Notebook vẫn minh họa rủi ro: "bảo hiểm" dạng NFD dài 11 ký tự, dạng NFC dài 8, và hai dạng không khớp chuỗi. Vì vậy bước chuẩn hóa NFC vẫn được giữ.

## Các lỗi điển hình tìm thấy

1. **Text thô phá vỡ cấu trúc bảng.** PyMuPDF thô in mỗi ô thành một dòng riêng ("Từ 1 đến 3 tuổi" / "2.585.000" / "3.707.000"…). Khi chunk, con số sẽ tách khỏi độ tuổi và chương trình, nên LLM không biết 3.707.000 là phí gói Bạc. `sort=True` sửa được bảng nhưng lại **đọc xen kẽ 2 cột** ở trang văn bản (thứ tự đúng chỉ 0.62). Không có cấu hình PyMuPDF nào tốt cho cả hai loại trang. Docling đạt 1.0 ở cả hai.
2. **Trang đôi.** An Gia và Tâm An là PDF dàn trang đôi (1 trang PDF = 2 trang in). Nếu không tách, trích dẫn sẽ sai số trang và thứ tự đọc lẫn giữa 2 trang. Ngược lại, nếu tách máy móc thì **bảng quyền lợi trải ngang 2 nửa bị cắt đôi**: Docling chỉ còn cột Đồng và một phần cột Bạc, row_integrity giảm từ 1.0 xuống 0.23. Cách sửa: tách theo mặc định, khai báo ngoại lệ trong manifest, và gán nhãn trang "24-25".
3. **Ký tự điều khiển ẩn.** PDF An Gia có 43 ký tự `\x07` (BEL) chen giữa số mục và tiêu đề ("9.\t\x07Tổng hạn Mức…"). Nhìn bằng mắt không thấy, nhưng regex "9. Tổng hạn" không khớp, và BM25 hay chunk theo cấu trúc sẽ bị trượt. Docling giữ nguyên các ký tự này (44 ký tự). Đã thêm bước loại chúng trong `normalize()`.
4. **`find_tables()` nhận đúng lưới nhưng làm hỏng chữ trong ô.** Lỗi gồm mất khoảng trắng ("Từ1đến3tuổi") và tách dấu chấm hàng nghìn ra khỏi số ("2585000\n. ."). Khi bỏ qua lỗi ký tự thì cấu trúc đúng 100%, nhưng text như vậy sẽ làm hỏng BM25 và so khớp số.
5. **Header chạy bị nâng thành tiêu đề.** Docling biến header "Quy tắc, Điều khoản Sản phẩm bổ trợ…" của AVSK thành `##` ở 4 trang. Nếu chunk theo heading, các tiêu đề giả này sẽ cắt ngang Điều 1, Điều 6, Điều 8. Đã sửa bằng cách lấy header/footer phát hiện từ lớp text PyMuPDF rồi lọc khỏi output Docling.
6. **Bộ lọc header/footer xóa nhầm.** Phiên bản đầu coi các dòng "1.16." (số mục định nghĩa đứng riêng một dòng) là footer lặp, vì sau khi thay số đều thành `#.#.`, và xóa mất chúng. Đã sửa: dòng chỉ gồm số và dấu chấm không bao giờ bị coi là header.

## Ghi chú cho Lab 2 (chunking)
- Dùng output `data/parsed/{doc_id}.docling.json` (đã làm sạch, có `pdf_page`, `page_label`).
- **Trùng lặp:** bản tóm tắt AVSK (`bvl-avsk-tomtat-2022`) trùng 0.707 (Jaccard 5-gram) với trang 1–2 của `bvl-avsk-2022`, trong khi với phần còn lại chỉ 0.019. Cần dedup hoặc gắn `doc_type=tom_tat` để tránh 2 chunk giống nhau chiếm top-k.
- **Trang không nên index như nội dung:** mục lục (AVSK, Dai-ichi, Manulife liệt kê "Điều X…" nên sẽ bị chunk theo cấu trúc tách nhầm; An Gia, Tâm An liệt kê "Phần I–V"), các biểu mẫu trống (Tâm An trang in 23, 25: giấy yêu cầu bồi thường, giấy sửa đổi bổ sung), bìa và trang quảng cáo.
- Bảng Markdown của Docling lặp lại nội dung ô gộp (span) ở mọi cột ("A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH…" × 7). Điều này tốn token và làm nhiễu embedding, nên cần gộp các ô trùng trước khi embed.
- Lỗi gốc trong tài liệu: bảng quyền lợi An Gia ghi "230.00 0.000" cho tổng hạn mức gói Vàng (đúng phải là 230.000.000). Đây là câu hỏi hay cho golden set: hệ thống nên trích nguyên văn và không tự "sửa".

## Câu trả lời phỏng vấn rút ra
- **Sửa lỗi gì:** parser hiểu layout (Docling) giữ được dòng–cột của bảng phí và thứ tự đọc nhiều cột, điều mà text thô không làm được đồng thời cả hai.
- **Tốn gì:** chậm hơn khoảng 100 lần so với PyMuPDF (64 giây so với dưới 1 giây cho 6 tài liệu trên GPU 4GB) và cần GPU/model local. Đổi lại, dữ liệu không rời hạ tầng.
- **Đo bằng gì:** đo trên chính tài liệu của mình, với ground truth ô bảng (row_integrity), thứ tự tiêu đề (LIS) và đếm ký tự lỗi/ký tự điều khiển. Không dựa vào benchmark của nhà cung cấp.
- Bài học lớn nhất: lỗi parsing thường **vô hình** (ký tự `\x07`, header thành heading, bảng bị cắt đôi). Chỉ có test tự động với ground truth mới phát hiện được.

## Trạng thái môi trường
- `.venv` Python 3.12, torch 2.14.1+cu126 (GPU OK), Docling 2.141, PyMuPDF 2.0.
- `ragas 0.3.1` đang lỗi import do lệch phiên bản `langchain-community`. Sẽ xử lý ở Lab 5.
- Docker pgvector (Lab 3) và LangFuse self-host (Lab 5) đã có file cấu hình nhưng **chưa khởi động**.
