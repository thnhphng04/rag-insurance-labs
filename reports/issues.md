# Vấn đề hiện hữu – tổng hợp 7 lab

Danh sách các vấn đề **chưa sửa** tính đến khi xong Lab 7, xếp theo mức ưu tiên. Chi tiết nằm trong mục "Vấn đề hiện hữu" của từng `reports/labN.md`.

**Mức ưu tiên:**
- **P0**: gây câu trả lời sai hoặc thiếu cho người dùng, hoặc rủi ro an toàn.
- **P1**: làm sai lệch đo lường hoặc kết luận.
- **P2**: chi phí, độ trễ, vận hành.

## Cần bạn quyết khi review
| # | Việc | Ảnh hưởng nếu đồng ý |
|---|---|---|
| D1 | **Duyệt golden set** ([`data/golden/golden_set_review.md`](../data/golden/golden_set_review.md)), nhất là các đáp án chuẩn | Có thể đổi số liệu Lab 2–6 |
| D2 | **Thêm bằng chứng thay thế cho G19**: trang tóm tắt Dai-ichi (trang 2) có ghi "Thời hạn bảo hiểm: 01 tháng" | G19 có thể chuyển từ trượt sang tìm được ở Lab 2–3 |
| D3 | **Tách đáp án chuẩn thành ý bắt buộc và ý bổ sung** (G06, G10, G11, G14 có ý ngoài câu hỏi) | Judge và FactualCorrectness bớt phạt oan |
| D4 | **Sửa lỗi chunk mất tiêu đề Điều** (I-02) rồi chạy lại Lab 2–6 | Đổi toàn bộ số liệu retrieval, có thể sửa G15 tận gốc |
| D5 | **Bật LangFuse self-host** khi máy rảnh RAM (đang có job `TradingProject` chiếm khoảng 3,8 GB) | Kiểm chứng code tracing với server thật |

## P0 – ảnh hưởng trực tiếp tới câu trả lời
| ID | Lab | Vấn đề | Câu bị ảnh hưởng | Đề xuất |
|---|---|---|---|---|
| I-01 | 1 | **Ô gộp theo chiều dọc mất giá trị** (Docling gán ô "Chi Phí Y Tế Thực Tế" cho 1 dòng). Manulife có 14 dòng trống ở trang 5–9 | G03 trượt ở mọi lab, câu trả lời phải suy luận | Đối chiếu với lưới đường kẻ của PyMuPDF `find_tables` (lưới đúng 100% ở Lab 1), hoặc dùng VLM cho trang bảng |
| I-02 | 2 | **Chunk mất tiêu đề Điều:** khi một Điều dài bị cắt nhiều phần, các phần sau chỉ có breadcrumb cấp cha, không có "Điều 10: Loại trừ…" | G15 bị đảo nghĩa ở Lab 6 v1; G19 (Điều 1 Dai-ichi có 25 định nghĩa) không lấy được Điều 1.21 | Đưa tiêu đề của chính section vào breadcrumb mọi phần; chunk định nghĩa theo từng mục (1.1, 1.2…) |
| I-03 | 4, 6 | **Ngữ cảnh thiếu một nửa thì model lấp chỗ trống thay vì từ chối.** Câu sai vẫn qua mọi hậu kiểm trích dẫn | G19 sai ở Lab 4 (đã hết sai ở Lab 6 v2 nhưng vẫn thiếu ý) | Bước kiểm tra "ngữ cảnh đã đủ cho mọi ý của câu hỏi chưa"; grounding grader có bộ test riêng (I-12) |
| I-04 | 6 | **Grader tài liệu loại nhầm đoạn cần thiết** (chunk Manulife "- 270 ngày Thai sản") | G16 ở Lab 6 thiếu phần Manulife, trong khi Lab 4 đủ | Đo recall của grader; chỉ lọc khi rerank score thấp; ưu tiên giữ thừa |
| I-05 | 7 | **Đầu độc nội dung** (tài liệu giả trông như quy định) vượt qua prompt; chưa có kiểm soát nguồn | 1/5 câu bị chiếm quyền với prompt naive (P2) | Chỉ nạp từ nguồn đã duyệt, hash/phiên bản theo `doc_id`, diff khi cập nhật, người duyệt |
| I-06 | 7 | **Output guard chưa gắn vào pipeline chính** (chỉ chạy trong Lab 7) | Mọi câu trả lời | Gắn `injection.output_guard` và hậu kiểm `invalid_ids` vào `generation`/đồ thị |
| I-07 | 7 | **Lớp quét khi nạp bằng regex không tổng quát hóa** (0/4 payload ẩn) | – | Bộ phân loại prompt injection (model chuyên dụng hoặc LLM judge) lúc ingest |

## P1 – đo lường, độ tin cậy của kết luận
| ID | Lab | Vấn đề | Đề xuất |
|---|---|---|---|
| I-08 | Golden | **Chỉ 20 câu**; mỗi câu bằng 0.05 điểm hit@k; nhiều chênh lệch giữa các phương pháp nằm trong mức nhiễu (Lab 2: sửa chunk bảng làm metric xê dịch ±0.03) | Mở rộng lên 100–200 câu, có chuyên gia nghiệp vụ duyệt |
| I-09 | Golden, 3 | **Mọi câu đều nêu tên sản phẩm** nên lọc sản phẩm có kết quả lạc quan (0.925) | Thêm câu không nêu sản phẩm; lấy sản phẩm từ hợp đồng đã xác thực của người dùng |
| I-10 | Golden, 4 | **Câu ngoài phạm vi quá dễ** (xe ô tô, ngân hàng, thú cưng): cả prompt naive cũng từ chối 5/5 | Thêm câu gần phạm vi (gói Đồng có thai sản không, điều trị ở nước ngoài, quyền lợi không có trong QTĐK) |
| I-11 | 5 | **RAGAS không ổn định trên tiếng Việt:** G16 faithfulness 0 (câu đúng), G19 context recall 1.0 (ngữ cảnh thiếu), dao động giữa các lần chạy; answer relevancy chỉ sinh 1/3 câu hỏi ngược | Chạy nhiều lần; judge mạnh hơn; dịch prompt RAGAS (`adapt_prompts`); dùng `llm_factory` thay wrapper deprecated; ưu tiên metric deterministic |
| I-12 | 5, 6 | **LLM judge và grounding grader chưa được hiệu chỉnh:** judge đồng thuận 70% với người, bỏ sót G19 sai; `check_grounding` chưa từng chấm "không đạt" | Bộ test câu trả lời sai có chủ đích (đảo nghĩa, ghép nhầm, sai số); rubric nhị phân theo từng ý; đo trên 50–100 nhãn người |
| I-13 | 5 | **LangFuse chưa chạy, code gửi trace chưa kiểm chứng với server** (máy thiếu RAM). Trace hiện ghi JSONL cục bộ | `cd infra/langfuse; docker compose up -d` rồi chạy lại `lab5_eval.ipynb` |
| I-14 | 7 | Thí nghiệm injection nhỏ (5 câu × 3 payload × 3 prompt, mỗi ô 1 lần chạy); "naive" vẫn dùng JSON schema; định nghĩa "thành công" chỉ dựa vào regex | promptfoo red-team, LLM judge "câu trả lời có bị ảnh hưởng không", đối chứng văn bản tự do |
| I-15 | 6 | Thời gian đo ở Lab 6 có lẫn lệnh gọi lấy từ cache (cận dưới) | Đo lại với cache tắt |

## P1 – parsing, dữ liệu
| ID | Lab | Vấn đề | Đề xuất |
|---|---|---|---|
| I-16 | 1, 4 | **Số trang trích dẫn của AVSK/Dai-ichi là số trang PDF**, không phải số in trên giấy (AVSK PDF tr.16 = in tr.14) | Đọc số trang in ở chân trang khi parse |
| I-17 | 1 | Nhãn dòng Nha khoa của biểu phí An Gia bị cắt ("Từ 1 đến" / "…18 tuổi Từ 19 đến 65 tuổi"); số liệu vẫn đúng dòng | Sửa tay trong tables JSON hoặc dùng lưới `find_tables` |
| I-18 | 1 | `keep_spread_pages` (trang đôi có bảng trải ngang) phải khai báo tay | Tự phát hiện bảng cắt ngang đường giữa trang |
| I-19 | 1, 2 | Docling gộp tiêu đề Dai-ichi ("CHƯƠNG 1: … Điều 1: …"), nên Điều 2, 3 không thành tiêu đề riêng | Tách tiêu đề bằng regex `Điều \d+` |
| I-20 | 1 | Khôi phục chữ trong vùng hình (`recover_picture_text`) gom theo cột với ngưỡng 60pt, mới thử trên 1 sơ đồ | Kiểm tra trên nhiều dạng sơ đồ hơn |
| I-21 | 1 | Lỗi in trong tài liệu gốc ("230.00 0.000", "0,09% TBH") được giữ nguyên văn; câu trả lời chưa ghi chú lỗi in | Quy tắc prompt riêng cho số liệu bất thường |

## P2 – chi phí, độ trễ, tính năng
| ID | Lab | Vấn đề | Đề xuất |
|---|---|---|---|
| I-22 | 3, 4 | **Độ trễ khoảng 7–8 s/câu** (rerank 20 ứng viên khoảng 1 s trên GPU 4GB, LLM khoảng 5 s), chưa streaming | Streaming; 10 ứng viên rerank; GPU mạnh hơn; model nhỏ cho bước viết lại |
| I-23 | 3 | **LLM viết lại thêm dấu sai** thuật ngữ ("Tự Ký" thay cho "Tử kỳ", "Bac" thay cho "Bạc") | Đưa danh mục sản phẩm, gói và thuật ngữ vào prompt viết lại |
| I-24 | 3 | Reranker làm hỏng câu không dấu (G09 bỏ dấu: hạng 4 → ngoài top-10) | Luôn viết lại trước khi rerank (đã làm trong pipeline đề xuất) |
| I-25 | 6 | **Đồ thị agentic gấp đôi chi phí** (4,3 lệnh gọi LLM/câu, khoảng 5.400 token); câu ngoài phạm vi tốn 5–6 lệnh gọi | Chặn sớm câu ngoài phạm vi bằng tín hiệu rẻ (không nhận ra sản phẩm, rerank score thấp) |
| I-26 | 6 | **Chưa có tool:** tra bảng phí (dữ liệu có sẵn ở `data/parsed/tables/*.json`), tra hợp đồng có xác thực | Thêm tool vào đồ thị, router theo loại câu hỏi |
| I-27 | 4 | Câu trả lời bỏ ý phụ do quy tắc "ngắn gọn" (G12, G16, G17, G18) | Yêu cầu liệt kê điều kiện và ngoại lệ đi kèm |
| I-28 | 2 | Contextual Retrieval (LLM) không cho lợi ích đo được so với breadcrumb, tốn khoảng 0,12 USD/tài liệu | Chỉ dùng cho tài liệu ít cấu trúc |
| I-29 | 7 | Chưa thử các kênh tấn công khác: direct injection, lịch sử hội thoại, memory poisoning, tool output, OWASP LLM08 (rò rỉ giữa tenant) | Bổ sung khi có dữ liệu hợp đồng cá nhân và tool |

## Môi trường, hạ tầng
| ID | Vấn đề | Ghi chú |
|---|---|---|
| E-01 | `pip install -r requirements.txt` kéo torch về bản CPU | Cài lại torch cu126 sau cùng (ghi trong `requirements.txt` và README) |
| E-02 | `ragas` 0.4.3 cần `langchain-community==0.4.1` | Đã khóa phiên bản trong `requirements.txt` |
| E-03 | Docker Desktop phải bật tay; container `lab-pgvector-1` (port 5433) **vẫn đang chạy** | `docker compose down` để tắt |
| E-04 | Repo private chứa PDF quy tắc của các hãng bảo hiểm | Giữ private |
| E-05 | Cache `data/cache/` (embedding, LLM) không commit. Chạy lại trên máy khác sẽ gọi lại API (tốn phí) và có thể cho kết quả hơi khác | – |
