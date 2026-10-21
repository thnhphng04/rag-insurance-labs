# Dữ liệu gợi ý cho Lab RAG (bảo hiểm)

Oct 20, 2026 · @Thanh Phong Trần

## Bộ tài liệu chính của Bảo Việt

Dùng 3 file quy tắc bảo hiểm công khai của Bảo Việt làm corpus chính, vì chúng liên quan trực tiếp đến buổi phỏng vấn.

| Tài liệu | Đơn vị | Điểm mạnh cho lab |
| --- | --- | --- |
| [Quy tắc bảo hiểm "Bảo Việt An Gia"](https://www.baovietbank.vn/media/BANCA/QuyTacBVAG.pdf) | Tổng Công ty Bảo hiểm Bảo Việt | Có Bảng quyền lợi (trang 24) và Biểu phí (trang 26): hợp để test parse bảng và câu hỏi về phí |
| [Quy tắc bảo hiểm sức khỏe "Bảo Việt Tâm An"](https://baoviet.com.vn/insurance/Uploads/Library/Images/SP18032011_1.%20Quy%20tac%20Bao%20Viet%20Tam%20An.pdf) | Tổng Công ty Bảo hiểm Bảo Việt | Có định nghĩa, bảng quyền lợi và hạn mức phụ cho từng hạng mục: hợp để viết câu hỏi về hạn mức |
| [Quy tắc, Điều khoản "An Vui Sống Khỏe"](https://baovietnhantho.com.vn/storage/9d098962-1cee-4778-bf0a-fdf804fa6fca/DK-R20-An-vui-song-khoe.pdf) | Bảo Việt Nhân thọ | Cấu trúc Chương → Điều rõ (Điều 6 quyền lợi, Điều 8 nguyên tắc trả, Điều 21 thời hạn giải quyết): hợp để chunk theo cấu trúc |

Bản [tóm tắt 2 trang của An Vui Sống Khỏe](https://www.baovietnhantho.com.vn/storage/9a7d81ac-def8-47ff-b366-0affa4b81a49/BTR20_AnVuiSongKhoe_tom_tat_dieu_khoan_va_mot_so_luu_y_quan_trong.pdf) giúp tạo câu hỏi và đáp án nhanh: có 4 chương trình Bạc, Vàng, Bạch kim, Kim cương, với quyền lợi nội trú, ngoại trú, nha khoa và giảm phí khi không có yêu cầu bồi thường.

## Tài liệu bổ sung

Thêm tài liệu của hãng khác để tạo câu hỏi so sánh nhiều tài liệu và test versioning.

| Tài liệu | Dùng để |
| --- | --- |
| [Manulife – Sức khỏe nâng cao](https://www.manulife.com.vn/content/dam/insurance/vn/documents/service-docs/san-pham/song-khoe-moi-ngay-phien-ban-cai-tien/quy-tac-dieu-kien-va-dieu-khoan-san-pham.pdf) | Câu hỏi so sánh, ví dụ quyền lợi thai sản Bảo Việt và Manulife. Nội trú là quyền lợi mặc định; ngoại trú, nha khoa, thai sản là quyền lợi mua thêm |
| Dai-ichi – Tử kỳ tái tục hàng tháng (2015) | Test versioning và metadata: Quy tắc của sản phẩm 2015 được ban hành lại theo Quyết định số 424/GD/Dai-ichi/2025. Tìm trên dai-ichi-life.com.vn với tên "Quy tắc và Điều khoản Tử kỳ tái tục hàng tháng (2015) cập nhật 30.06.2025" |

## Dataset có sẵn nhãn cho eval

Nếu không muốn tự viết nhiều câu hỏi, dùng bộ pháp luật tiếng Việt có sẵn cặp query–passage để đo recall@k, MRR, nDCG.

- **GreenNode/zalo-ai-legal-text-retrieval-vn** (Hugging Face): bộ eval retrieval pháp luật tiếng Việt. Đã có kết quả của multilingual-e5-base và vietnamese-bi-encoder trên bộ này để làm baseline.
- [**bqbbao6/vietnamese-legal-embedding**](https://huggingface.co/bqbbao6/vietnamese-legal-embedding): model để so sánh với BGE-M3. Fine-tune từ multilingual-e5-base trên 250.000 bộ ba pháp luật. Khi dùng, thêm tiền tố `query:` cho câu hỏi và `passage:` cho văn bản.

## Cách dùng cho 7 lab

| Lab | File nên dùng |
| --- | --- |
| Lab 1 – Parsing | An Gia (bảng quyền lợi, biểu phí) |
| Lab 2 – Chunking | An Vui Sống Khỏe (Chương/Điều rõ) |
| Lab 3 – Hybrid + rerank | Cả 3 file Bảo Việt |
| Lab 4 – Citation | Tâm An + 5 câu hỏi về sản phẩm không có trong tài liệu |
| Lab 5 – Eval | 20 câu tự viết + bộ Zalo legal |
| Lab 6 – CRAG | Cả 3 file Bảo Việt + Manulife (câu so sánh) |
| Lab 7 – Injection | Chèn câu độc hại vào 1 chunk của Tâm An |

Tải các file về máy rồi gửi vào chat; Claude có thể viết sẵn 20 câu hỏi kèm đáp án và số Điều/trang để làm golden set.
