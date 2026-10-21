# Lab 4 – Generation có trích dẫn

Notebook: `notebooks/lab4_generation.ipynb` · Code: `src/ragbv/generation.py` · Số liệu: `reports/lab4_results.json` (v2), `reports/lab4_results_v1.json` (v1) · Câu trả lời để duyệt: [`lab4_answers_basic.md`](lab4_answers_basic.md), [`lab4_answers_naive.md`](lab4_answers_naive.md), [`lab4_answers_basic_v1.md`](lab4_answers_basic_v1.md) · Đầu vào cho Lab 5: `data/runs/lab4_basic.jsonl`

## Thiết lập
- **Truy xuất:** pipeline tốt nhất của Lab 3: viết lại câu hỏi → lọc sản phẩm → hybrid3 (dense + BM25 + BM25 bỏ dấu, RRF) → rerank 20 ứng viên → **top-5 chunk**.
- **Sinh:** `gpt-4.1-mini`, temperature 0, **structured output** (JSON schema, `strict`):
  - `status`: `tra_loi` hoặc `khong_du_thong_tin`
  - `answer`: câu trả lời có trích dẫn `[C#]`
  - `citations`: `[{id, quote}]`
- **Ngữ cảnh trong prompt:** mỗi chunk là một khối `<tai_lieu id="C1" san_pham="…" doc_id="…" muc="…" trang="…">text</tai_lieu>`. Breadcrumb đi qua thuộc tính `muc`, `text` là nội dung gốc (xem Lab 2).
- **Hai prompt:**
  - `basic`: 7 quy tắc (chỉ dùng tài liệu, mỗi câu có trích dẫn, từ chối khi thiếu thông tin, không dùng sản phẩm khác để trả lời thay, không cam kết bồi thường, giữ nguyên số liệu kể cả lỗi in, trả lời ngắn).
  - `naive`: chỉ có "Trả lời dựa trên các tài liệu sau, trích dẫn nếu có", cùng định dạng JSON.
- **Bộ câu hỏi:** 20 câu trong phạm vi và 5 câu ngoài phạm vi (bảo hiểm xe ô tô, sản phẩm "An Phúc Gia Lộc" không có trong corpus, lãi suất ngân hàng, trạng thái hợp đồng cá nhân, bảo hiểm thú cưng Manulife).

**Hậu kiểm tự động** (`generation.check`):

| Kiểm tra | Cách làm |
|---|---|
| Có trích dẫn trong câu trả lời | regex `[C\d+]` trong `answer` |
| id không tồn tại | id trích dẫn ngoài C1–C5 |
| Quote chặt | `quote` (sau chuẩn hoá NFC, khoảng trắng) nằm nguyên văn trong đúng chunk được trích |
| Quote khớp từng phần | tách `quote` theo `—`, `;`, `…`, mọi mảnh đều nằm trong chunk (cho dòng bảng bị rút bớt cột) |
| Sửa id bằng quote | quote không có trong chunk được trích nhưng có nguyên văn trong chunk khác → gán lại id |
| Trích đúng đoạn bằng chứng | chunk được trích chứa đủ `must_contain` của bằng chứng golden |
| Từ chối | `status` của 5 câu ngoài phạm vi phải là `khong_du_thong_tin`; 20 câu trong phạm vi không được từ chối |

## Lặp prompt: v1 → v2
Lần chạy đầu (v1), hậu kiểm phát hiện 3 vấn đề, nên prompt được sửa thành v2:
- **v1, quy tắc 2:** "Mỗi ý phải kèm trích dẫn [C1]…". Model chỉ điền mảng `citations`, không chèn `[C#]` vào văn bản.
- **v2:** "Mỗi câu phải **kết thúc** bằng [C#]…, câu trả lời không có [C#] là sai định dạng". Kèm ví dụ dạng `"Câu thứ nhất [C1]. Câu thứ hai [C2]."` và yêu cầu `quote` là đoạn **liền mạch, chép y nguyên từng ký tự**: không dùng "...", không ghép các phần xa nhau, với bảng thì chép nguyên một dòng.

| prompt `basic` | v1 | v2 |
|---|---|---|
| Câu trả lời có `[C#]` trong văn bản | 4/20 | **20/20** |
| Quote nguyên văn (chặt) | 0.617 | **0.867** |
| Trích đúng đoạn bằng chứng | 18/20 | 18/20 |
| Độ trễ LLM p50 | 2,8 s | 5,0 s |

Câu trả lời v2 dài hơn (có trích dẫn từng câu), nên độ trễ tăng gần gấp đôi.

## Kết quả (prompt v2)
| | basic | naive |
|---|---|---|
| Câu ngoài phạm vi từ chối đúng | **5/5** | 5/5 |
| Câu trong phạm vi bị từ chối nhầm | **0/20** | 0/20 |
| Câu trả lời có trích dẫn `[C#]` | **20/20** | 19/20 |
| Trích dẫn id không tồn tại | 0 | 0 |
| Quote nguyên văn (chặt) | **0.867** | 0.825 |
| Quote khớp từng phần | **0.950** | 0.875 |
| Trích dẫn sai id, sửa được bằng quote | 1 | 1 |
| Trích đúng đoạn bằng chứng | 18/20 | 18/20 |
| … sau khi sửa id | **19/20** | 19/20 |
| Ngữ cảnh có bằng chứng (giới hạn trên do retrieval) | 19/20 | 19/20 |
| Token prompt trung bình | 2.434 | 2.147 |
| Độ trễ LLM p50 | 5,0 s | 5,0 s |

## Nhận xét
1. **Hậu kiểm trích dẫn bắt được lỗi mà đọc qua không thấy.** Ở G01, số 1.887.600 **đúng**, quote là đúng dòng "Từ 31 đến 40 tuổi — ĐỒNG: 1.315.600; BẠC: 1.887.600…", nhưng id ghi là **C3** (chunk 41–65 tuổi) trong khi dòng đó nằm ở **C2**. Người dùng bấm vào nguồn sẽ thấy một bảng không có con số đó. Ở v1 còn có trường hợp nặng hơn: G16 gắn quote "270 ngày Thai sản" (câu chữ của Manulife) cho chunk AVSK. Cả hai đều bị phát hiện nhờ kiểm tra quote có nằm nguyên văn trong chunk được trích không. Lỗi lệch id **sửa được tự động** bằng cách tìm chunk thật sự chứa quote.
2. **Bắt buộc quote nguyên văn là cách rẻ để kiểm tra grounding.** Không cần thêm lệnh gọi LLM: kiểm tra chuỗi con đã đủ phát hiện trích dẫn bịa hoặc gán nhầm. Quote dòng bảng thường bị rút bớt cột (G08: "Trợ cấp bệnh viện công — LỘC: 300.000/ngày…" bỏ cột PHÚC). Nội dung đúng nhưng không liền mạch, nên cần mức kiểm tra "khớp từng phần".
3. **Từ chối hoạt động tốt, nhưng bộ câu ngoài phạm vi còn quá dễ.** Cả `basic` lẫn `naive` đều từ chối 5/5 và không từ chối nhầm câu nào. Các câu ngoài phạm vi hiện khác hẳn corpus (xe ô tô, ngân hàng, thú cưng). Lọc sản phẩm và rerank đã đưa ngữ cảnh không liên quan vào prompt, và trường `status` trong JSON schema tự nó "gợi ý" lựa chọn từ chối. Chưa thử các câu **gần phạm vi** (xem Vấn đề hiện hữu).
4. **G03 cho thấy LLM lấp chỗ trống khi ngữ cảnh thiếu.** Ngữ cảnh có dòng "E. Chi phí sinh" nhưng **không có giá trị** (lỗi parse ô gộp dọc, Lab 1). Model không từ chối mà suy ra từ quy định chung về đồng chi trả (C1, trang 4): "chi trả theo Chi Phí Y Tế Thực Tế sau khi áp dụng mức đồng chi trả…". Câu trả lời tình cờ gần đúng, nhưng dựa trên suy luận chứ không trích từ quyền lợi thai sản. Trường hợp này cần grader kiểm tra grounding (Lab 6) hoặc sửa parser.
5. **Giữ nguyên lỗi in:** G02 trả lời "230.000.000" nhưng quote giữ nguyên "230.00 0.000/ng/năm". Đúng tinh thần quy tắc 6 (nêu nguyên văn), dù model không ghi chú rằng bản gốc in lỗi.
6. **Đọc tay 20 câu trả lời so với đáp án chuẩn:**

   | Kết quả | Câu |
   |---|---|
   | Đúng, đủ ý chính | G01, G02, G04, G05, G06, G07, G08, G09, G10, G11, G13, G14, G15, G20 (14) |
   | Đúng ý chính, thiếu ý phụ | G12 (thiếu "Bạc không áp dụng", đồng chi trả 20%), G16 (thiếu "biến chứng thai sản 90 ngày" của An Gia), G17 (thiếu đồng chi trả 20% của Manulife), G18 (thiếu công văn phê chuẩn 2015) (4) |
   | Suy luận, không dựa trên bằng chứng | G03 (1) |
   | **Sai** | **G19** (1) |

   **G19 là lỗi nguy hiểm nhất của Lab 4.** Hệ thống trả lời "Thời hạn bảo hiểm … là **đến khi Người được bảo hiểm đạt 76 tuổi**", trong khi đúng là **01 tháng, gia hạn hằng tháng** (Điều 1.21). Retrieval chỉ lấy được chunk chứa Điều 1.13 (tuổi tối đa 76), không lấy được chunk chứa 1.21. Model không từ chối mà **ghép nhầm** quy định tuổi tối đa thành thời hạn bảo hiểm. Câu trả lời này **vượt qua mọi bước hậu kiểm**: trích dẫn hợp lệ, quote nguyên văn, trích đúng một đoạn bằng chứng (E2). Kết luận: hậu kiểm trích dẫn chỉ chứng minh "câu chữ có trong tài liệu", **không chứng minh câu trả lời đúng**. Cần kiểm tra câu trả lời có được ngữ cảnh hỗ trợ không (faithfulness ở Lab 5, grader ở Lab 6), và cần đo độ đầy đủ của ngữ cảnh (context recall) cho câu hỏi nhiều ý.

## Vấn đề hiện hữu
- **Số trang trích dẫn không phải số in trên giấy** với tài liệu trang đơn có đánh số riêng. AVSK và Dai-ichi dùng số trang PDF (`page_label` = trang PDF), trong khi số in trên giấy bị đánh lại từ phần Quy tắc (ví dụ AVSK PDF tr.16 = in tr.14). An Gia và Tâm An đúng số in. Cần đọc số trang in ở chân trang khi parse (Lab 1).
- **Câu trả lời sai vượt qua hậu kiểm (G19).** Hậu kiểm hiện chỉ kiểm tra cấu trúc trích dẫn. Độ đúng nội dung mới chỉ được đọc tay (14 đúng đủ, 4 thiếu ý phụ, 1 suy luận, 1 sai). Số liệu tự động đo ở Lab 5 (RAGAS + LLM-as-judge).
- **Câu trả lời thiếu ý phụ** (G12, G16, G17, G18): prompt yêu cầu "ngắn gọn, đúng trọng tâm", nên model bỏ các ý phụ có trong ngữ cảnh. Cần cân nhắc giữa ngắn gọn và đầy đủ, hoặc yêu cầu liệt kê điều kiện/ngoại lệ kèm theo.
- **Bộ câu ngoài phạm vi quá dễ**, cần bổ sung câu gần phạm vi, ví dụ:
  - "Gói Đồng của An Gia có quyền lợi thai sản không?" (có trong tài liệu, đáp án là "Không").
  - "Tâm An có chi trả điều trị ở Singapore không?" (phạm vi lãnh thổ: Việt Nam).
  - "An Vui Sống Khỏe có quyền lợi tử vong không?" (không nêu trong QTĐK bổ trợ).
- **Hậu kiểm chỉ kiểm tra quote, chưa kiểm tra câu trả lời có được quote hỗ trợ không.** Model có thể trích đúng một câu nhưng diễn giải sai trong `answer`. Cần bước kiểm tra entailment (LLM grader, Lab 6) hoặc đo faithfulness (Lab 5).
- **Độ trễ:** retrieval khoảng 1–1,5 s (chủ yếu là rerank 20 ứng viên), LLM viết lại khoảng 1 s, LLM sinh khoảng 5 s (p50). Tổng khoảng 7–8 s, chưa streaming. Với SLA chatbot (ví dụ p95 < 5 s) cần streaming, giảm số ứng viên rerank, hoặc dùng model nhỏ hơn cho viết lại.
- **Lỗi kế thừa:** G03 (lỗi parse ô gộp dọc của Manulife) vẫn chưa sửa ở tầng parsing.

## Câu trả lời phỏng vấn rút ra
- **"Làm sao đảm bảo trích dẫn đúng?"** Gán id cho từng chunk trong prompt, dùng structured output, bắt model chép **quote nguyên văn**, rồi hậu kiểm bằng so khớp chuỗi (không tốn thêm LLM). Quote sai thì gán lại id theo chunk thật sự chứa quote, nếu không tìm thấy thì đánh dấu không được hỗ trợ. Ở đây: 20/20 câu có trích dẫn, 95% quote khớp, 1 trích dẫn lệch id được sửa tự động.
- **"Prompt engineering có đo được không?"** Có. v1 → v2 tăng tỉ lệ trích dẫn trong văn bản từ 4/20 lên 20/20, và quote nguyên văn từ 0,62 lên 0,87, đo trên cùng golden set. Đổi lại độ trễ tăng từ 2,8 s lên 5,0 s.
- **"Model không biết thì sao?"** Cho phép từ chối bằng một trường `status` riêng trong schema, không để model tự diễn đạt. Đo cả hai chiều: từ chối đúng câu ngoài phạm vi (5/5) và không từ chối nhầm câu trong phạm vi (0/20). Nhưng **khi ngữ cảnh thiếu một phần thì model không từ chối mà lấp chỗ trống**: G03 suy luận, G19 trả lời sai mà vẫn có trích dẫn hợp lệ. Ca nguy hiểm nhất không phải câu hoàn toàn ngoài phạm vi, mà là câu **retrieval chỉ lấy được một nửa bằng chứng**. Cần grader grounding và đo context recall.
