# Lab 6 – CRAG-lite bằng LangGraph

Notebook: `notebooks/lab6_crag.ipynb` · Code: `src/ragbv/graph.py` · Đồ thị: [`lab6_graph.md`](lab6_graph.md) (mermaid) · Câu trả lời: [`lab6_answers.md`](lab6_answers.md) (v2), [`lab6_answers_v1.md`](lab6_answers_v1.md) · Số liệu: `reports/lab6_results.json` (v2), `reports/lab6_results_v1.json`

## Đồ thị
```
prepare → retrieve → grade_documents ─┬─ có đoạn liên quan ──→ generate → check_grounding ─┬─ đạt ─────────→ finish
                ↑                      ├─ không, còn lượt ──→ transform_query ─┬─→ retrieve   ├─ không đạt (lần 1) → regenerate → check_grounding
                └──────────────────────┘                                       └─ truy vấn lặp → fallback
                                       └─ không, hết lượt (2) ─→ fallback                    └─ không đạt (lần 2) → fallback
```
| Nút | Làm gì | LLM |
|---|---|---|
| `prepare` | Viết lại câu hỏi (Lab 3). Câu nêu ≥ 2 sản phẩm thì **tách câu con theo sản phẩm**, mỗi câu con lọc `doc_id` của sản phẩm đó | `gpt-4.1-mini` (có cache) |
| `retrieve` | hybrid3 + rerank (20 ứng viên), top-5 mỗi câu con, gộp và bỏ trùng, tối đa 8 đoạn | – |
| `grade_documents` | Chấm từng đoạn: `co`/`khong` giúp trả lời trực tiếp (kiểu CRAG Correct/Incorrect), 1 lệnh gọi cho cả lô | `gpt-4.1-mini` |
| `transform_query` | Viết lại thành truy vấn khác, dùng thuật ngữ quy tắc, tối đa 2 lần. Truy vấn lặp lại thì dừng | `gpt-4.1-mini` |
| `generate` | Prompt `basic` của Lab 4 + quy tắc "trả lời từng phần có thông tin, nói rõ phần thiếu" | `gpt-4.1-mini` |
| `check_grounding` | Tách ý, kiểm tra từng ý có được tài liệu nói rõ không (kiểu ISSUP của Self-RAG) | **`gpt-4.1`** |
| `regenerate` | Sinh lại 1 lần, kèm danh sách ý không được hỗ trợ | `gpt-4.1-mini` |
| `fallback` | "Chưa có đủ thông tin … liên hệ tư vấn viên" | – |

Giới hạn vòng lặp: tối đa 2 lần `transform_query`, 1 lần `regenerate`, `recursion_limit=25`.

## Hai phiên bản
**v1** (lần chạy đầu) có 3 lỗi:
- **G16, G17 (so sánh) bị từ chối toàn bộ.** `grade_documents` loại nhầm chunk Manulife. Sau đó quy tắc 3 của prompt Lab 4 ("không trả lời một phần bằng phỏng đoán") khiến model từ chối cả câu. Pipeline Lab 4 không bị vì đưa nguyên 5 chunk vào prompt.
- **G19 vẫn sai như Lab 4** ("thời hạn bảo hiểm … đến khi đạt 76 tuổi"). `check_grounding` (gpt-4.1-mini) chấm cả hai ý là "được hỗ trợ".
- **G15 bị đảo nghĩa:** "An Vui Sống Khỏe **chi trả** các phương pháp … y học cổ truyền, châm cứu" (đúng là **không** chi trả). Grader chỉ giữ 1 chunk: **phần thứ hai của Điều 10**, không có dòng tiêu đề "Điều 10: Loại trừ trách nhiệm bảo hiểm" (xem Vấn đề hiện hữu). `check_grounding` (gpt-4.1-mini) chấm ý sai này là "được hỗ trợ".
- **Câu ngoài phạm vi tốn 6 lệnh gọi LLM.** `transform_query` lần 2 sinh **lại đúng truy vấn của lần 1**.

**v2** (sửa trong phạm vi đồ thị, không đổi chunk để giữ nguyên số liệu Lab 2–5):
- grader và grounding được thấy breadcrumb (`muc`) của từng đoạn;
- `generate` có thêm quy tắc trả lời từng phần (`PARTIAL_RULES`);
- dừng sớm khi truy vấn biến đổi bị lặp;
- `check_grounding` dùng `gpt-4.1`.

## Kết quả (20 câu trong phạm vi + 5 ngoài phạm vi)
**Đọc tay** (cùng tiêu chí với Lab 4):

| | Đúng, đủ | Thiếu ý | Sai | Ngoài phạm vi từ chối |
|---|---|---|---|---|
| Lab 4: pipeline cố định | 14 | 5 | **1** (G19) | 5/5 |
| Lab 6 v1: đồ thị | (chưa đọc tay đủ 20 câu) | + 2 từ chối nhầm (G16, G17) | **2** (G15 đảo nghĩa; G19 vẫn sai như Lab 4) | 5/5 |
| **Lab 6 v2: đồ thị** | 14 | 6 | **0** | 5/5 |

Judge LLM của Lab 5 (đồng thuận với người 70%): Lab 4 có 9 `dung_du`, 11 `thieu_y`; Lab 6 v2 có 10 `dung_du`, 10 `thieu_y`.

**Chi phí** (v2):

| | Lab 4 | Lab 6 v2 |
|---|---|---|
| Lệnh gọi LLM / câu (TB) | 2 (viết lại + sinh) | **4,3** (câu trong phạm vi: 4; câu ngoài phạm vi: 5–6) |
| Token / câu (TB) | khoảng 2.800 | **khoảng 5.400** |
| Thời gian / câu (p50, gồm cả lệnh gọi lấy từ cache) | khoảng 7 s | **khoảng 10,6 s** |

**Đường đi:** 20/25 câu đi thẳng `prepare → retrieve → grade → generate → check → finish`. 4 câu ngoài phạm vi đi qua `transform_query` rồi `fallback`. O04 (trạng thái hợp đồng cá nhân) tìm được 1 đoạn "liên quan" ở lần biến đổi đầu, rồi model tự từ chối. **`regenerate` chưa kích hoạt lần nào**, và `check_grounding` chấm "đạt" cho mọi câu trả lời.

## Nhận xét
1. **Đồ thị loại được câu trả lời sai duy nhất (G19), nhưng không phải nhờ bước kiểm tra grounding.** Ở v2, G19 chỉ còn "Tuổi tối đa … khi kết thúc Thời hạn bảo hiểm là 76 tuổi [C1]". Không còn câu sai "thời hạn bảo hiểm đến khi 76 tuổi", nhưng vẫn thiếu ý "01 tháng" vì retrieval vẫn không lấy được Điều 1.21 (`transform_query` không chạy, vì grader thấy có đoạn liên quan). Sự cải thiện đến từ **ngữ cảnh gọn hơn** (grader giữ 3/5 đoạn) cộng với **quy tắc trả lời từng phần**, không phải từ `check_grounding`.
2. **Bộ lọc tài liệu (grader) vừa giúp vừa hại.** Nó loại đoạn nhiễu (giữ trung bình khoảng 2,6/5 đoạn), làm ngữ cảnh gọn hơn. Nhưng nó cũng **loại nhầm đoạn cần thiết**: chunk Manulife "- 270 ngày Thai sản" (G16) bị chấm "khong", có lẽ vì đây là danh sách mốc thời gian khôi phục từ sơ đồ, thiếu ngữ cảnh. Kết quả là G16 thiếu phần Manulife, trong khi Lab 4 trả lời đủ cả 3 sản phẩm. Ở bài toán bảo hiểm, **loại nhầm (false negative) nguy hiểm hơn giữ thừa**, vì nó biến câu trả lời đủ thành "chưa có thông tin".
3. **Tách câu con theo sản phẩm hoạt động:** G17 lấy được cả An Gia và Manulife (giữ 8/8 đoạn). G16 tách thành 3 câu con đúng, nhưng vẫn mất Manulife ở bước grader (nhận xét 2).
4. **`check_grounding` hầu như không có tác dụng trên bộ câu hỏi này.** v1 dùng gpt-4.1-mini và chấm "được hỗ trợ" cả cho câu đảo nghĩa (G15) lẫn câu ghép nhầm (G19). v2 dùng gpt-4.1 thì không còn câu sai nào để bắt, nên **chưa chứng minh được giá trị**. Để đánh giá đúng bước này cần tập câu hỏi có ngữ cảnh "bẫy" (thiếu một nửa, dễ ghép nhầm).
5. **Agentic có giá:** gấp đôi số lệnh gọi LLM và token, thêm khoảng 3–4 s độ trễ. Câu ngoài phạm vi tốn nhiều nhất (5–6 lệnh gọi) để đi đến cùng một kết luận như pipeline cố định (5/5 từ chối). Thứ tự hợp lý hơn: nhận diện câu ngoài phạm vi rẻ trước (không nhận ra sản phẩm, không tìm thấy đoạn nào qua ngưỡng rerank), rồi mới chạy vòng biến đổi truy vấn.
6. **Lặp phiên bản có số đo:** v1 → v2 nhờ log từng nút và so sánh với Lab 4 trên cùng golden set. Không có log thì sẽ không thấy grader loại nhầm chunk Manulife hay `transform_query` lặp lại.

## Vấn đề hiện hữu
- **Chunk mất tiêu đề Điều (Lab 2, nguyên nhân gốc của G15 v1).** Khi một Điều dài bị `_split_long` cắt thành nhiều phần, chỉ phần đầu có dòng tiêu đề ("Điều 10: Loại trừ trách nhiệm bảo hiểm"). Breadcrumb chỉ chứa tiêu đề cha (Chương), nên các phần sau **không cho biết đây là danh sách loại trừ**. Khi phần đó đứng một mình trong prompt, model hiểu ngược nghĩa. Cách sửa: đưa tiêu đề của chính section vào breadcrumb của mọi phần (`section` + heading). Phải chạy lại Lab 2–5 vì chunk thay đổi.
- **Grader loại nhầm đoạn cần thiết (G16).** Cần đo recall của grader (tỉ lệ đoạn bằng chứng golden bị chấm "khong"). Các hướng: hạ ngưỡng (giữ đoạn "có thể liên quan"); chỉ lọc khi rerank score thấp; hoặc không lọc mà chỉ dùng grader để quyết định có cần `transform_query` hay không.
- **`check_grounding` chưa được kiểm chứng.** Chưa từng chấm "không đạt", nên `regenerate` chưa chạy lần nào. Cần bộ test riêng gồm câu trả lời sai có chủ đích (đảo nghĩa, ghép nhầm, sai số) để đo recall của grader.
- **G19 vẫn thiếu Điều 1.21:** đồ thị không gọi `transform_query` khi đã có một phần đoạn liên quan. Cần thêm bước kiểm tra "ngữ cảnh đã đủ cho mọi ý của câu hỏi chưa" (câu hỏi nhiều ý), thay vì chỉ "có ít nhất 1 đoạn liên quan".
- **Câu ngoài phạm vi tốn kém** (5–6 lệnh gọi LLM). Nên chặn sớm bằng tín hiệu rẻ (không nhận ra sản phẩm, rerank score thấp).
- **Chưa có tool tra bảng phí** (dữ liệu đã có sẵn trong `tables/*.json` từ Lab 1). Câu như "phí gói Vàng cho người 35 tuổi" nên đi qua tool tra bảng thay vì để LLM đọc số. Chưa có tool tra hợp đồng có xác thực cho câu như O04.
- **Độ trễ chưa đo cold-start đúng cách:** các lệnh gọi viết lại và sinh có thể lấy từ cache của Lab 4, nên thời gian 10,6 s là cận dưới. Đo thật cần xóa `data/cache/` hoặc tắt cache.

## Câu trả lời phỏng vấn rút ra
- **"Agentic RAG có tốt hơn không?"** Trên 20 câu: loại được 1 câu sai, đổi lại 1 câu trả lời kém đầy đủ hơn, gấp đôi chi phí LLM, thêm khoảng 3–4 s. Không phải mặc định tốt hơn. Đáng dùng khi eval chỉ ra lỗi cụ thể mà luồng cố định không sửa được (ở đây: câu trả lời ghép nhầm khi ngữ cảnh thiếu, câu so sánh nhiều sản phẩm).
- **"Self-RAG/CRAG khác nhau thế nào trong thực tế?"** Grader tài liệu (CRAG) quyết định "tìm lại hay trả lời", rủi ro chính là loại nhầm. Grader câu trả lời (Self-RAG ISSUP) là chốt chặn cuối, nhưng model nhỏ chấm dễ dãi (G15, G19 ở v1 đều được chấm "được hỗ trợ").
- **"Làm sao tránh agent lặp vô hạn?"** Giới hạn cứng (2 lần biến đổi, 1 lần sinh lại, `recursion_limit`), phát hiện truy vấn lặp để dừng sớm, nhánh fallback chuyển tư vấn viên, và log từng nút để thấy vòng lặp vô ích (v1: 6 lệnh gọi cho 1 câu ngoài phạm vi).
