# Lab 5 – Evaluation: RAGAS + LLM-as-judge + tracing

Notebook: `notebooks/lab5_eval.ipynb` · Code: `src/ragbv/evaluation.py`, `src/ragbv/tracing.py` · Số liệu: `reports/lab5_results.json`, `reports/lab5_ragas_variance.json` · Trace: `data/traces/lab5_pipeline.jsonl`

## Thiết lập
- **Đầu vào:** câu trả lời của Lab 4 (prompt `basic` v2, top-5 ngữ cảnh), 20 câu trong phạm vi.
- **RAGAS 0.4.3:** judge `gpt-4.1-mini` (temperature 0), embedding `text-embedding-3-small`. Các metric:
  - `Faithfulness`: tỉ lệ ý trong câu trả lời được ngữ cảnh hỗ trợ.
  - `ResponseRelevancy`: độ liên quan của câu trả lời với câu hỏi.
  - `LLMContextPrecisionWithReference`: average precision, có tính thứ tự.
  - `LLMContextRecall`: tỉ lệ ý của đáp án chuẩn tìm thấy trong ngữ cảnh.
  - `FactualCorrectness` (F1): so khớp ý giữa câu trả lời và đáp án chuẩn.
- **LLM-as-judge tự viết:** rubric 4 nhãn bằng tiếng Việt (`dung_du`, `thieu_y`, `sai`, `tu_choi`), JSON output. Đối chiếu với **nhãn người** (mình đọc tay ở Lab 4).
- **Tracing:** mỗi câu hỏi là một trace gồm các span `retrieve` (có thời gian từng bước con), `generate` (token, độ trễ LLM) và `check_citations`, kèm điểm `cites_valid`.
- **Cài đặt:** `ragas` 0.4.3 cần `langchain-community==0.4.1`. Bản 0.4.2 đã bỏ `chat_models.vertexai` mà ragas vẫn import (đã ghi vào `requirements.txt`).

## Kết quả RAGAS (trung bình 20 câu)
| Metric | Điểm |
|---|---|
| faithfulness | 0.871 |
| answer_relevancy | 0.612 |
| context_precision (có reference) | 0.793 |
| context_recall | 0.888 |
| factual_correctness (F1) | 0.453 |

## LLM-as-judge so với nhãn người
| người \ judge | dung_du | thieu_y |
|---|---|---|
| dung_du (14) | 9 | 5 |
| thieu_y (5) | 0 | 5 |
| sai (1: G19) | 0 | **1** |

Đồng thuận **70% (14/20)**. Judge **khắt khe hơn** người ở 5 câu (G04, G06, G10, G11, G14): nó phạt việc câu trả lời thiếu các ý **có trong đáp án chuẩn nhưng câu hỏi không hỏi**. Ví dụ G06 hỏi thời gian chờ của bệnh có sẵn và bệnh đặc biệt, nhưng đáp án chuẩn liệt kê thêm thời gian chờ ốm đau 30 ngày, thai sản 90 ngày… Judge **bỏ sót lỗi nghiêm trọng duy nhất** (G19, chấm `thieu_y` thay vì `sai`): nó thấy thiếu ý "01 tháng" nhưng không nhận ra câu "thời hạn bảo hiểm là đến khi đạt 76 tuổi" là **sai**.

## Độ tin cậy của RAGAS trên dữ liệu này
Kiểm tra lại từng câu (và chạy lại 2 lần với G02, G11, G16, G17, G19) cho thấy điểm từng câu **không đáng tin**:

| Câu | Thực tế (đọc tay) | RAGAS |
|---|---|---|
| G19 | Ngữ cảnh **không** có "01 tháng"/Điều 1.21; câu trả lời sai | context_recall **1.0** ở lần chạy chính, **0.5 và 1.0** ở 2 lần chạy lại |
| G16 | Trả lời đúng cả 3 sản phẩm, trích dẫn hợp lệ, quote nguyên văn | faithfulness **0.0** (cả 3 lần), context_precision **0.0** |
| G17 | Trả lời đúng ý chính, trích dẫn hợp lệ | faithfulness **0.0** rồi **0.33** |
| G02, G11, G14, G20 | Trả lời đúng | factual_correctness **0.0** |
| Nhiều câu | — | answer_relevancy 0.19–0.36 cho câu trả lời đúng trọng tâm (G07, G10, G14, G19, G20) |

Nguyên nhân có thể:
1. Prompt của RAGAS bằng tiếng Anh, còn câu hỏi, ngữ cảnh và câu trả lời bằng tiếng Việt. Bước tách ý và bước xác minh của judge dễ sai, nhất là với nội dung so sánh nhiều sản phẩm và bảng số.
2. `ResponseRelevancy` yêu cầu 3 câu hỏi ngược nhưng `ChatOpenAI` qua wrapper chỉ trả 1 ("LLM returned 1 generations instead of requested 3"), nên điểm nhiễu hơn. Ngoài ra, model sinh câu hỏi ngược có thể không giữ được cách diễn đạt tiếng Việt.
3. `FactualCorrectness` so khớp cả hai chiều với đáp án chuẩn. Đáp án chuẩn của golden set có thêm ý phụ, nên câu trả lời ngắn mà đúng vẫn có precision/recall thấp.
4. Có biến thiên giữa các lần chạy dù temperature = 0.

**Kết luận:** con số trung bình của RAGAS ở đây chỉ nên dùng để **so sánh tương đối giữa các phiên bản** (cùng judge, cùng dữ liệu, chạy nhiều lần), không dùng làm thước đo tuyệt đối hay để chẩn đoán từng câu. Các tín hiệu đáng tin hơn trong project này:
- recall theo đoạn trích bằng chứng (`must_contain`, deterministic) ở Lab 2–3
- hậu kiểm trích dẫn (deterministic) ở Lab 4
- judge rubric tiếng Việt, đã đối chiếu với nhãn người (70% đồng thuận, cần hiệu chỉnh)
- đọc tay

## Chẩn đoán retrieval hay generation
Quy tắc: context_recall < 0.5 là lỗi retrieval; faithfulness < 0.7 là generation không bám ngữ cảnh; nhãn người khác `dung_du` là generation thiếu ý hoặc diễn giải sai.

| Câu | Chẩn đoán tự động (dùng RAGAS) | Chẩn đoán đúng (đọc tay + `must_contain`) |
|---|---|---|
| G03 | generation thiếu ý | **Parse** (ô gộp dọc mất giá trị) → ngữ cảnh thiếu → generation suy luận |
| G12, G18 | generation thiếu ý | Đúng: ngữ cảnh đủ, câu trả lời bỏ ý phụ (prompt "ngắn gọn") |
| G16 | retrieval | **Sai**: cả 3 bằng chứng trong top-5 (Lab 3–4), lỗi do judge |
| G17 | không bám ngữ cảnh | **Sai**: câu trả lời bám ngữ cảnh, thiếu ý phụ (đồng chi trả 20%) |
| G19 | không bám ngữ cảnh | **Retrieval** (thiếu chunk Điều 1.21), sau đó generation ghép nhầm |

Chẩn đoán tự động dựa trên RAGAS chỉ đúng hoàn toàn **2/6** câu có vấn đề (G12, G18). G03 đúng một phần: phát hiện có vấn đề nhưng không chỉ ra được nguyên nhân gốc là parse. Khi dùng recall theo `must_contain` của golden set (deterministic) thay cho context_recall của RAGAS, chẩn đoán retrieval đúng cho cả G16 và G19.

## Tracing
- **LangFuse self-host chưa chạy.** Máy chỉ còn khoảng 1,9 GB RAM trống, vì đang có job `TradingProject/reference/waka/optimize_waka.py` (khoảng 3,8 GB và 9 worker) của một dự án khác. Stack LangFuse gồm Postgres, ClickHouse, Redis, MinIO, web và worker, cần khoảng 3–4 GB. Mình không bật để tránh swap làm chậm job đó.
- `tracing.Tracer` tự kiểm tra `LANGFUSE_HOST/api/public/health`. Không có server thì ghi **JSONL cục bộ** (`data/traces/lab5_pipeline.jsonl`) với cùng cấu trúc trace → span (input, output, `duration_ms`) → scores.
- Độ trễ từng bước đọc từ trace (p50): BGE-M3 dense 12 ms, BM25 3 ms, BM25 bỏ dấu 3 ms, **rerank 20 ứng viên 1.009 ms**, **LLM sinh 5.030 ms**. Rewrite 1 ms là do đọc cache; lúc gọi thật khoảng 1 s. Token: prompt khoảng 2.371, completion khoảng 170.

## Vấn đề hiện hữu
- **LangFuse chưa chạy và code gửi trace lên LangFuse chưa được kiểm chứng với server thật.** `tracing.py` gọi `start_as_current_observation`/`start_as_current_span` của SDK v5.0.3 theo tài liệu, nhưng chưa chạy thử. Để bật khi máy rảnh RAM:
  ```powershell
  cd infra/langfuse; docker compose up -d   # UI: http://localhost:3000, user/pass trong infra/langfuse/.env (LANGFUSE_INIT_USER_*)
  ```
  Sau đó chạy lại `notebooks/lab5_eval.ipynb`. Key project đã có sẵn trong `.env` qua cơ chế headless init.
- **RAGAS không ổn định trên tiếng Việt** (xem bảng trên). Cần: (1) chạy nhiều lần lấy trung bình; (2) thử judge mạnh hơn (`gpt-4.1`) hoặc prompt RAGAS dịch sang tiếng Việt (RAGAS hỗ trợ `adapt_prompts`); (3) dùng `llm_factory` (Instructor) thay cho `LangchainLLMWrapper` đã deprecated, để `n=3` hoạt động.
- **Judge LLM bỏ sót câu sai (G19)** và khắt khe với câu thiếu ý không được hỏi. Cần hiệu chỉnh rubric: tách "có thông tin sai" thành câu hỏi riêng (kiểm tra từng ý với đáp án chuẩn), và chỉ chấm "thiếu ý" với ý mà câu hỏi thực sự hỏi. Đo lại đồng thuận trên 50–100 nhãn người.
- **Đáp án chuẩn của golden set chứa ý ngoài phạm vi câu hỏi** (G06, G10, G11, G14), gây nhiễu cho FactualCorrectness và judge. Cần tách `answer` thành ý **bắt buộc** (câu hỏi hỏi) và ý **bổ sung**.
- **Chưa có đánh giá trực tuyến:** chưa có feedback người dùng, chưa lấy mẫu trace production, chưa có ngưỡng chặn release trong CI.

## Câu trả lời phỏng vấn rút ra
- **"Faithfulness cao nhưng vẫn sai?"** G19 là ví dụ thật: faithfulness 0.67, quote nguyên văn, trích dẫn hợp lệ, nhưng câu trả lời sai vì ngữ cảnh thiếu một nửa bằng chứng (context recall thực tế thấp). Thứ tự kiểm tra: context recall trước, faithfulness sau, rồi correctness so với reference.
- **"Có tin RAGAS không?"** Dùng làm tín hiệu tương đối, không phải chân lý. Ở đây RAGAS cho G16 faithfulness 0 (câu đúng) và G19 context recall 1.0 (ngữ cảnh thiếu). Luôn **đối chiếu với nhãn người** (judge ở đây đồng thuận 70%) và ưu tiên các metric deterministic khi có thể (recall theo đoạn trích, kiểm tra trích dẫn).
- **"LLM-as-judge có thiên lệch gì?"** Thấy rõ 2 điều: khắt khe với câu trả lời ngắn so với đáp án chuẩn dài, và bỏ sót một lỗi sai thực chất. Cách giảm: rubric nhị phân theo từng ý, cố định phiên bản model judge, đo đồng thuận với người định kỳ.
