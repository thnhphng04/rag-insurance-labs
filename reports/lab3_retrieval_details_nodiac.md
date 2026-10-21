# Lab 3 – Kết quả truy xuất từng câu (bỏ dấu)

Sinh tự động. ✅ = chunk chứa đủ đoạn trích của bằng chứng (E1, E2… theo thứ tự trong golden set). Hiển thị top-5; hạng của bằng chứng tính đến top-10 (`—` = ngoài top-10).

## G01 · table_lookup

**Câu hỏi:** Phi bao hiem dieu khoan chinh (dieu tri noi tru) goi Bac cua Bao Viet An Gia cho nguoi 35 tuoi la bao nhieu mot nam?

**Đáp án chuẩn:** 1.887.600 đồng/người/năm (biểu phí An Gia, điều khoản chính, nhóm tuổi từ 31 đến 40).

- **E1**: `bv-angia-2016` · Biểu phí bảo hiểm - A. Điều khoản bảo hiểm chính · tr.26 · cần chứa: 'Từ 31 đến 40 tuổi', '1.887.600'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 8 | 0.00 |
| hybrid3 | E1: — | 0.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 3 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 |  | `bv-angia-2016` · 22 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › Mất dương vật và 2 tinh hoàn ở người: | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 76 — QUYỀN LỢI: Dưới 55 tuổi chưa có con; TỶ LỆ TRẢ TIỀN: 70-80% - 76 — QUYỀN LỢI: Dưới 55 tuổi đã có con; TỶ LỆ TRẢ TIỀN: 55… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 35. Trợ cấp cho Người được bảo hiểm Là khoản tiền trợ cấp cho Người được bảo hiểm trong trường hợp Người được bảo hiểm mắc 01 hoặc nhiều hơn 01 bệnh trong 22 bệ… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 5 |  | `daiichi-tktt2015-2025` · 2,3 | Tử kỳ tái tục hàng tháng (2015) › IV. NGHĨA VỤ KÊ KHAI THÔNG TIN TRUNG THỰC | Quy định chi tiết tại Điều 4.1 của QTĐK Quý khách lưu ý phải kê khai đầy đủ và chính xác tất cả thông tin cần thiết để Dai-ichi Life Việt Nam đánh giá khả năng … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 3 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |

</details>

## G02 · table_lookup

**Câu hỏi:** Tong han muc quyen loi bao hiem chinh cua goi Vang trong Bao Viet An Gia la bao nhieu?

**Đáp án chuẩn:** 230.000.000 đồng/người/năm. Lưu ý bảng quyền lợi gốc in là "230.00 0.000/ng/năm".

- **E1**: `bv-angia-2016` · Bảng quyền lợi bảo hiểm - A. Điều khoản bảo hiểm chính · tr.24-25 · cần chứa: 'Tổng hạn mức quyền lợi bảo hiểm chính', '230.00 0.000'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 4 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 3 | Bảo Việt An Gia | . QUY TẮC BẢO HIỂM "BẢO VIỆT AN GIA" (Ban hành theo Quyết định triển khai số 4542 ngày 13 tháng 10 năm 2016 của Tổng Giám đốc - Tổng Công ty Bảo hiểm Bảo Việt) … |
| 2 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 8. Bảng quyền lợi bảo hiểm Bảng quyền lợi bảo hiểm cung cấp các thông tin tóm tắt về quyền lợi bảo hiểm. Bảng quyền lợi bảo hiểm được cấp cùng và là bộ phận khô… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 4 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |

</details>

## G03 · table_lookup

**Câu hỏi:** Voi quyen loi thai san cua Manulife Cham Soc Suc Khoe Nang Cao, chi phi sinh duoc chi tra nhu the nao?

**Đáp án chuẩn:** Chi phí sinh được chi trả theo Chi Phí Y Tế Thực Tế, nằm trong giới hạn tối đa cho mỗi lần mang thai (Titan 12 triệu, Vàng 25 triệu, Bạch Kim 35 triệu, Kim Cương 70 triệu), áp dụng mức đồng chi trả 20%; chỉ chi trả cho người được bảo hiểm từ đủ 18 đến 45 tuổi.

- **E1**: `manulife-cssknc-2026` · Điều 1.4 Quyền lợi thai sản · tr.9 · cần chứa: 'E. Chi phí sinh', 'Giới hạn tối đa cho mỗi lần mang thai'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: — | 0.00 |
| hybrid3+rerank | E1: — | 0.00 |
| hybrid3+rerank+filter | E1: — | 0.00 |
| rewrite+hybrid3+rerank+filter | E1: — | 0.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 32. Đồng Chi Trả — col1: Là việc Bên Mua Bảo Hiểm và Manulife cùng chi trả cho Chi Phí Y Tế Thực Tế phát sinh. Mức Đồng Chi Trả là tỷ lệ phần trăm… |
| 3 |  | `manulife-cssknc-2026` · 20 | Chăm Sóc Sức Khỏe Nâng Cao › Chương V. HIỆU LỰC CỦA SẢN PHẨM BẢO HIỂM | Điều 16. GIẢI QUYẾT MÂU THUẪN VÀ TRANH CHẤP - 16.1. Hợp Đồng Bảo Hiểm được điều chỉnh và giải thích theo pháp luật của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam. … |
| 4 |  | `manulife-cssknc-2026` · 25 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 41. Ngày Kỷ Niệm Năm Hợp Đồng — col1: Là ngày kỷ niệm tương ứng hàng năm của Ngày Hiệu Lực Hợp Đồng trong suốt thời hạn Hợp Đồng. Nếu năm không có… |
| 5 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | (*) Mức Đồng Chi Trả: Mức Đồng Chi Trả được ghi nhận tại thời điểm phát hành hợp đồng sẽ áp dụng xuyên suốt thời hạn hợp đồng (bao gồm thời gian tái tục). Trong… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 32. Đồng Chi Trả — col1: Là việc Bên Mua Bảo Hiểm và Manulife cùng chi trả cho Chi Phí Y Tế Thực Tế phát sinh. Mức Đồng Chi Trả là tỷ lệ phần trăm… |
| 3 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |
| 4 |  | `manulife-cssknc-2026` · 10,11 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 3. CÁC TRƯỜNG HỢP LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM Manulife sẽ không chi trả quyền lợi bảo hiểm phát sinh từ, liên quan đến hay là hậu quả của bất kỳ trường h… |
| 5 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 16. Chi Phí Tái Tạo Tuyến Vú Sau Đoạn Nhũ Do Ung Thư — col1: nhưng do cơ thể không đào thải nên không cần thiết lấy ra. Là các Chi Phí Y Tế Thực T… |
| 4 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |
| 5 |  | `manulife-cssknc-2026` · 23 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 19. Chi Phí Y Tế Thông Lệ Và Hợp Lý — col1: a. Là mức giá dịch vụ thông thường mà Cơ Sở Y Tế áp dụng chung cho tất cả bệnh nhân của mình theo mức … |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 16. Chi Phí Tái Tạo Tuyến Vú Sau Đoạn Nhũ Do Ung Thư — col1: nhưng do cơ thể không đào thải nên không cần thiết lấy ra. Là các Chi Phí Y Tế Thực T… |
| 4 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |
| 5 |  | `manulife-cssknc-2026` · 23 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 19. Chi Phí Y Tế Thông Lệ Và Hợp Lý — col1: a. Là mức giá dịch vụ thông thường mà Cơ Sở Y Tế áp dụng chung cho tất cả bệnh nhân của mình theo mức … |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |
| 4 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản (là tổng quyền lợi bảo hiểm… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - D. Chi Phí Dưỡng Nhi/ năm hợp đồng (trong vòng 7 ngày kể từ ngày sinh, LOẠI TRỪ Bệnh Bẩm Sinh/ Dị Tật Bẩm Sinh) — TITA… |

</details>

## G04 · multi_condition

**Câu hỏi:** Bao hiem thai san cua Bao Viet An Gia ap dung cho ai va sau bao lau thi duoc chi tra chi phi sinh no?

**Đáp án chuẩn:** Người được bảo hiểm từ 18 đến 45 tuổi, phải tham gia điều khoản chính tương đương chương trình Bạch Kim hoặc Kim Cương. Chi phí sinh nở chỉ được chi trả sau 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản sau 90 ngày. Giới hạn tối đa 21.000.000 (Bạch Kim) / 31.500.000 (Kim Cương) cho một thời hạn bảo hiểm.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5: Bảo hiểm thai sản · tr.15 · cần chứa: '635 ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: 8 | 0.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 3 | Bảo Việt An Gia | . QUY TẮC BẢO HIỂM "BẢO VIỆT AN GIA" (Ban hành theo Quyết định triển khai số 4542 ngày 13 tháng 10 năm 2016 của Tổng Giám đốc - Tổng Công ty Bảo hiểm Bảo Việt) … |
| 2 |  | `daiichi-tktt2015-2025` · 15,16,17 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - (ii) Trong trường hợp có bất kỳ sự thay đổi nghề nghiệp/việc làm của Người được bảo hiểm hoặc Người được bảo hiểm xuất cảnh ngoài Điều kiện chuẩn, không phụ t… |
| 3 |  | `daiichi-tktt2015-2025` · 15,16,17 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 11: THAY ĐỔI THÔNG TIN LIÊN HỆ, NƠI CƯ TRÚ VÀ NGHỀ NGHIỆP - 11.1. Nếu Bên mua bảo hiểm và/hoặc Người được bảo hiểm thay đổi địa chỉ cư trú/liên hệ trong lã… |
| 4 |  | `daiichi-tktt2015-2025` · 17 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 12: THAY ĐỔI TRONG TRƯỜNG HỢP BÊN MUA BẢO HIỂM TỬ VONG HOẶC CHẤM DỨT HOẠT ĐỘNG - 12.1. Nếu Bên mua bảo hiểm bị tử vong (trường hợp là cá nhân và không phải… |
| 5 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 9. Chiến tranh, nội chiến, đình công, khủng bố, bạo động, dân biến, phiến loạn, các hoạt động dân sự hoặc hành động của bất kỳ người cầm đầu của tổ chức nào nhằ… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 2 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 17. Điều trị và/hoặc phẫu thuật cho các bệnh bẩm sinh, bệnh di truyền/dị tật/khuyết tật bẩm sinh, bệnh dị dạng về gen và mọi biến chứng, hậu quả liên quan đến n… |
| 3 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 45. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người được… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 5 |  | `bv-angia-2016` · 3 | Bảo Việt An Gia | . QUY TẮC BẢO HIỂM "BẢO VIỆT AN GIA" (Ban hành theo Quyết định triển khai số 4542 ngày 13 tháng 10 năm 2016 của Tổng Giám đốc - Tổng Công ty Bảo hiểm Bảo Việt) … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 5 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 45. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người được… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 5 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 45. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người được… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |

</details>

## G05 · fact

**Câu hỏi:** Tre em tu 15 ngay tuoi den 3 tuoi tham gia Bao Viet An Gia duoc chi tra theo ty le nao?

**Đáp án chuẩn:** Áp dụng đồng chi trả 70/30: Bảo Việt chi trả 70%, người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (trừ khoa điều trị tự nguyện/theo yêu cầu của bệnh viện công lập).

- **E1**: `bv-angia-2016` · Bảng quyền lợi - Quy định đồng chi trả đối với trẻ em · tr.24-25 · cần chứa: '70/30'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 2 | 1.00 |
| hybrid3+rerank | E1: 3 | 1.00 |
| hybrid3+rerank+filter | E1: 3 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 5 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › I. ĐỊNH NGHĨA | 3. Người yêu cầu bảo hiểm Là người đại diện như bố/mẹ cho những người phụ thuộc là con dưới 18 tuổi hoặc vợ/chồng, con của người được bảo hiểm trên 18 tuổi đứng… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 2 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 3 |  | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 5 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham gia Điều khoản bổ sung này các chi phí y tế phát sinh điều trị ngoại trú do ố… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 4 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn bao gồm cả biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiể… |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham gia Điều khoản bổ sung này các chi phí y tế phát sinh điều trị ngoại trú do ố… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 4 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn bao gồm cả biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiể… |
| 5 |  | `bv-angia-2016` · 21 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › CHI TRÊN | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - — QUYỀN LỢI: Mất cả ngón út và đốt bàn; TỶ LỆ TRẢ TIỀN: 15-20% - — QUYỀN LỢI: Mất cả ngón út; TỶ LỆ TRẢ TIỀN: 10-15% - 22 — Q… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham gia Điều khoản bổ sung này các chi phí y tế phát sinh điều trị ngoại trú do ố… |
| 4 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn bao gồm cả biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiể… |
| 5 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 50. Đồng chi trả Đồng chi trả là số tiền theo tỷ lệ mà Công ty bảo hiểm, Người được bảo hiểm cùng chi trả khi phát sinh chi phí thuộc phạm vi bảo hiểm của Quy t… |

</details>

## G06 · fact

**Câu hỏi:** Thoi gian cho doi voi benh co san va benh dac biet trong quy tac Bao Viet An Gia la bao lau?

**Đáp án chuẩn:** 01 năm đối với bệnh có sẵn (và các bệnh tại điểm loại trừ chung số 36), 01 năm đối với bệnh đặc biệt. Ngoài ra: ốm đau bệnh tật 30 ngày, biến chứng thai sản 90 ngày, trẻ em đến 6 tuổi bị viêm phế quản/tiểu phế quản/viêm phổi 06 tháng.

- **E1** (nhóm thay thế `a`): `bv-angia-2016` · Phần II - 2. Hiệu lực bảo hiểm · tr.13 · cần chứa: '01 năm đối với bệnh có sẵn', '01 năm đối với bệnh đặc biệt'
- **E2** (nhóm thay thế `a`): `bv-angia-2016` · Điều khoản bổ sung 1 - 2. Hiệu lực bảo hiểm · tr.14 · cần chứa: '01 năm đối với bệnh có sẵn', '01 năm đối với bệnh đặc biệt'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 10, E2: 10 | 0.00 |
| hybrid3 | E1: 3, E2: 3 | 1.00 |
| hybrid3+rerank | E1: 2, E2: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2, E2: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 4 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 3 | Bảo Việt An Gia | . QUY TẮC BẢO HIỂM "BẢO VIỆT AN GIA" (Ban hành theo Quyết định triển khai số 4542 ngày 13 tháng 10 năm 2016 của Tổng Giám đốc - Tổng Công ty Bảo hiểm Bảo Việt) … |
| 2 |  | `bv-angia-2016` · 5 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 12. Thời hạn bảo hiểm Thời hạn bảo hiểm được quy định cụ thể trong Hợp đồng bảo hiểm hoặc Giấy chứng nhận bảo hiểm. Thời hạn bảo hiểm là một (01) năm, không chấ… |
| 3 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 4 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 3 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 3 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 3 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 4 |  | `bv-angia-2016` · 14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 3: BẢO HIỂM SINH MẠNG | 1. Phạm vi bảo hiểm Bảo hiểm trường hợp chết hoặc tàn tật toàn bộ vĩnh viễn do nguyên nhân không phải là tai nạn xảy ra trong thời hạn bảo hiểm trừ những điểm l… |
| 5 |  | `bv-angia-2016` · 5 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 19. Ốm đau, bệnh tật Là tình trạng cơ thể có dấu hiệu của một bệnh lý khác với tình trạng sức khỏe bình thường được biểu hiện bằng các triệu chứng hay hội chứng… |

</details>

## G07 · fact

**Câu hỏi:** Bao Viet Tam An nhan bao hiem cho nguoi o do tuoi nao?

**Đáp án chuẩn:** Từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 đến 63 tuổi chỉ được tham gia mới nếu có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ.

- **E1**: `bv-taman-2019` · Phần I - II. Đối tượng tham gia bảo hiểm · tr.10 · cần chứa: 'sáu mươi ba (63) tuổi'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: 5 | 1.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 3 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 5 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 2 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 3 |  | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 4 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 5 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 2 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 5 |  | `bv-taman-2019` · 13 | Bảo Việt Tâm An › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH - ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN, BIẾN CHỨNG THAI SẢN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn, biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiểm phải nằm… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 2 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 5 |  | `bv-taman-2019` · 13 | Bảo Việt Tâm An › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH - ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN, BIẾN CHỨNG THAI SẢN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn, biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiểm phải nằm… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 4 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 2. Người được bảo hiểm Là cá nhân có tính mạng hoặc tình trạng sức khỏe được bảo hiểm theo Hợp đồng bảo hiểm/Giấy chứng nhận bảo hiểm. Người được bảo hiểm đã ho… |
| 5 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 31. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 32. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |

</details>

## G08 · table_lookup

**Câu hỏi:** Chuong trinh Loc cua Bao Viet Tam An tro cap benh vien cong bao nhieu?

**Đáp án chuẩn:** 300.000 đồng/ngày, không quá 60 ngày/năm.

- **E1**: `bv-taman-2019` · Bảng quyền lợi bảo hiểm sức khỏe Bảo Việt Tâm An - mục 8 · tr.22 · cần chứa: 'Trợ cấp bệnh viện công', '300.000/ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 4 | 1.00 |
| hybrid3 | E1: 5 | 1.00 |
| hybrid3+rerank | E1: 3 | 1.00 |
| hybrid3+rerank+filter | E1: 4 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 20 | Bảo Việt Tâm An › PHỤ LỤC I | DANH MỤC 22 BỆNH/TÌNH TRẠNG NGHIÊM TRỌNG 1. Ghép tủy xương 2. Thiếu máu bất sản/Bệnh rối loạn đông máu 3. Nhồi máu cơ tim 4. Tai biến mạch máu não (đột quỵ) 5. … |
| 2 |  | `bv-angia-2016` · 21 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › CỘT SỐNG | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 51 — QUYỀN LỢI: Cắt bỏ cung sau của một đốt sống; TỶ LỆ TRẢ TIỀN: 35-40% - — QUYỀN LỢI: Cắt bỏ cung sau của 2 - 3 đốt sống tr… |
| 3 |  | `bv-angia-2016` · 22 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › BỤNG | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 60 — QUYỀN LỢI: Cắt toàn bộ dạ dày; TỶ LỆ TRẢ TIỀN: 75-85% - 61 — QUYỀN LỢI: Cắt đoạn dạ dày; TỶ LỆ TRẢ TIỀN: 50-60% - 62 — Q… |
| 4 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 5 |  | `bv-angia-2016` · 21 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › CHI DƯỚI | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 44 — QUYỀN LỢI: Mất một đốt ngón cái; TỶ LỆ TRẢ TIỀN: 08-12% - 45 — QUYỀN LỢI: Cứng khớp hông; TỶ LỆ TRẢ TIỀN: 45-55% - 46 — … |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 2 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An | BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ/ng… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 5 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 4 |  | `bv-taman-2019` · 20 | Bảo Việt Tâm An › PHỤ LỤC I | DANH MỤC 22 BỆNH/TÌNH TRẠNG NGHIÊM TRỌNG 1. Ghép tủy xương 2. Thiếu máu bất sản/Bệnh rối loạn đông máu 3. Nhồi máu cơ tim 4. Tai biến mạch máu não (đột quỵ) 5. … |
| 5 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 31. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 32. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 2 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 3 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 4 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 5 |  | `bv-taman-2019` · 6 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 8. Bệnh của máu: Rối loạn đông máu, rối loạn chức năng của bạch cầu đa trung tính, bệnh liên quan mô lưới bạch huyết và hệ thống lưới mô bào, ghép tủy. 9. Bệnh … |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 5 |  | `bv-taman-2019` · 13 | Bảo Việt Tâm An › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH - ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN, BIẾN CHỨNG THAI SẢN | b. Trường hợp phẫu thuật Trường hợp Người được bảo hiểm phải phẫu thuật phải nằm viện điều trị nội trú thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt sẽ thanh toán t… |

</details>

## G09 · multi_condition

**Câu hỏi:** Ho so yeu cau boi thuong Bao Viet Tam An phai nop trong thoi han nao va Bao hiem Bao Viet giai quyet trong bao lau?

**Đáp án chuẩn:** Nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng của đợt điều trị (hoặc ngày tử vong) và không quá 01 năm kể từ ngày xảy ra sự kiện bảo hiểm (không tính thời gian bất khả kháng). Bảo hiểm Bảo Việt giải quyết và chi trả trong vòng 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ.

- **E1** (nhóm thay thế `a`): `bv-taman-2019` · Phần I - IX. Thời hạn khiếu nại và trả tiền bảo hiểm · tr.12 · cần chứa: 'sáu mươi (60) ngày kể từ ngày điều trị cuối cùng', 'mười lăm (15) ngày'
- **E2** (nhóm thay thế `a`): `bv-taman-2019` · Phần V - Thủ tục yêu cầu trả tiền bảo hiểm · tr.18 · cần chứa: 'sáu mươi (60) ngày kể từ ngày điều trị cuối cùng'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 7, E2: 7 | 0.00 |
| hybrid3 | E1: 4, E2: 4 | 1.00 |
| hybrid3+rerank | E1: —, E2: — | 0.00 |
| hybrid3+rerank+filter | E1: —, E2: — | 0.00 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 2 |  | `bv-taman-2019` · 12 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | VIII. NGHĨA VỤ CỦA NGƯỜI ĐƯỢC BẢO HIỂM 1. Bên mua bảo hiểm/Người được bảo hiểm bảo hiểm phải kê khai trung thực đầy đủ các nội dung trong Giấy yêu cầu bảo hiểm … |
| 3 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | V. PHÍ BẢO HIỂM VÀ SỐ TIỀN BẢO HIỂM Phí bảo hiểm quy định trong Biểu phí đính kèm Quy tắc bảo hiểm này, phí bảo hiểm phụ thuộc vào chương trình bảo hiểm, độ tuổ… |
| 4 |  | `bv-taman-2019` · 3 | Bảo Việt Tâm An | QUY TẮC BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) |
| 5 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 2 |  | `bv-taman-2019` · 14 | Bảo Việt Tâm An | PHẦN III: ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG BẢO HIỂM TỬ VONG DO TAI NẠN Quyền lợi bổ sung sau đây sẽ được cấp cùng với Quy tắc và là một bộ phận không thể tách rời Qu… |
| 3 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia | PHẦN III: ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG Các quyền lợi bổ sung sau đây sẽ được cấp cùng với Quy tắc và là một bộ phận không thể tách rời Quy tắc bảo hiểm này. Các … |
| 4 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 5 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | V. PHÍ BẢO HIỂM VÀ SỐ TIỀN BẢO HIỂM Phí bảo hiểm quy định trong Biểu phí đính kèm Quy tắc bảo hiểm này, phí bảo hiểm phụ thuộc vào chương trình bảo hiểm, độ tuổ… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 2 |  | `bv-taman-2019` · 3 | Bảo Việt Tâm An | QUY TẮC BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) |
| 3 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 4. Trường hợp bảo lãnh (áp dụng cho chương trình có dịch vụ bảo lãnh) Trường hợp Người được bảo hiểm khám và điều trị tại các bệnh viện trong hệ thống bảo lãnh … |
| 4 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | 3. Các chứng từ là bản gốc liên quan đến việc thanh toán chi phí y tế: hóa đơn tài chính, biên lai, phiếu thu theo quy định của Bộ Tài Chính, Tổng cục Thuế và b… |
| 5 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 3. Thông tin chung về chi trả bảo hiểm Tất cả các chứng từ và tài liệu mà Bảo hiểm Bảo Việt yêu cầu hỗ trợ cho việc chi trả bảo hiểm sẽ được cung cấp miễn phí c… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 2 |  | `bv-taman-2019` · 3 | Bảo Việt Tâm An | QUY TẮC BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) |
| 3 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 4. Trường hợp bảo lãnh (áp dụng cho chương trình có dịch vụ bảo lãnh) Trường hợp Người được bảo hiểm khám và điều trị tại các bệnh viện trong hệ thống bảo lãnh … |
| 4 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | 3. Các chứng từ là bản gốc liên quan đến việc thanh toán chi phí y tế: hóa đơn tài chính, biên lai, phiếu thu theo quy định của Bộ Tài Chính, Tổng cục Thuế và b… |
| 5 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 1. Trường hợp ứng tiền trước, bồi thường sau: Trường hợp Người được bảo hiểm khám và điều trị tại các cơ sở y tế hợp pháp không thuộc hệ thống bảo lãnh thanh to… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 3 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 4 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | 3. Các chứng từ là bản gốc liên quan đến việc thanh toán chi phí y tế: hóa đơn tài chính, biên lai, phiếu thu theo quy định của Bộ Tài Chính, Tổng cục Thuế và b… |
| 5 |  | `bv-taman-2019` · 5 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 10. Giới hạn phụ Là giới hạn bồi thường tối đa cho mỗi hạng mục được quy định chi tiết trong Bảng quyền lợi bảo hiểm. Trong mọi trường hợp, tổng số tiền bồi thư… |

</details>

## G10 · fact

**Câu hỏi:** Neu toi tu yeu cau huy hop dong Bao Viet Tam An thi duoc hoan lai bao nhieu phi?

**Đáp án chuẩn:** Bảo hiểm Bảo Việt hoàn trả 80% phí bảo hiểm của thời gian còn lại, với điều kiện trong thời gian hiệu lực chưa có khiếu nại đòi trả tiền bảo hiểm nào. (Nếu Bảo hiểm Bảo Việt yêu cầu hủy thì hoàn toàn bộ phí của thời gian còn lại; trường hợp gian lận chỉ hoàn 70% nếu chưa có bồi thường.)

- **E1**: `bv-taman-2019` · Phần I - III. Ký kết/hủy bỏ hợp đồng bảo hiểm · tr.11 · cần chứa: 'hoàn trả 80% phí bảo hiểm'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 3 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 9 | 0.00 |
| hybrid3+rerank+filter | E1: — | 0.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 |  | `bv-taman-2019` · 20 | Bảo Việt Tâm An › PHỤ LỤC I | DANH MỤC 22 BỆNH/TÌNH TRẠNG NGHIÊM TRỌNG 1. Ghép tủy xương 2. Thiếu máu bất sản/Bệnh rối loạn đông máu 3. Nhồi máu cơ tim 4. Tai biến mạch máu não (đột quỵ) 5. … |
| 3 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 5 |  | `daiichi-tktt2015-2025` · 7 | Tử kỳ tái tục hàng tháng (2015) | CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm này, các thuật ngữ và từ ngữ viết tắt được hiểu và giải… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 2 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Người được bảo hiểm phải kê khai trung thực đầy đủ nội du… |
| 4 |  | `daiichi-tktt2015-2025` · 10,11 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 2: QUYỀN LỢI CÓ THỂ ĐƯỢC BẢO HIỂM Tại thời điểm yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm phải có quyền lợi có thể được bảo hiểm với Người được bảo hiểm … |
| 5 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 2. (i) Đơn phương hủy bỏ toàn bộ Hợp đồng bảo hiểm Theo đó, Hợp đồng bảo hiểm không có hiệu lực từ thời điểm được Dai-ichi Life Việt Nam chấp thuận bảo hiểm. Kh… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | 3. Các chứng từ là bản gốc liên quan đến việc thanh toán chi phí y tế: hóa đơn tài chính, biên lai, phiếu thu theo quy định của Bộ Tài Chính, Tổng cục Thuế và b… |
| 2 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM | 4. Đối với trường hợp Tai nạn: Tai nạn sinh hoạt, tai nạn lao động: Bản tường trình tóm tắt về tai nạn, không yêu cầu xác nhận của cơ quan chính quyền địa phươn… |
| 3 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | 3. Các chứng từ là bản gốc liên quan đến việc thanh toán chi phí y tế: hóa đơn tài chính, biên lai, phiếu thu theo quy định của Bộ Tài Chính, Tổng cục Thuế và b… |
| 2 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 31. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 32. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 3 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 26. Các hình thức thẩm mỹ, phẫu thuật thẩm mỹ, chỉnh hình. 27. Chi phí để cung cấp, bảo dưỡng, sửa chữa hay thay thế bộ phận/thiết bị hỗ trợ điều trị hay bộ phậ… |
| 4 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM | 4. Đối với trường hợp Tai nạn: Tai nạn sinh hoạt, tai nạn lao động: Bản tường trình tóm tắt về tai nạn, không yêu cầu xác nhận của cơ quan chính quyền địa phươn… |
| 5 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 5 |  | `bv-taman-2019` · 8,9 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 41. Thuốc kê theo Đơn của bác sỹ Là những thuốc, dược phẩm được bán và sử dụng theo Đơn của Bác sỹ, theo quy định của pháp luật và không bao gồm thực phẩm chức … |

</details>

## G11 · fact

**Câu hỏi:** Thoi gian cho cua quyen loi thai san trong san pham An Vui Song Khoe la bao lau?

**Đáp án chuẩn:** 270 ngày (Điều 8.1). Các sự kiện do tai nạn không áp dụng thời gian chờ.

- **E1**: `bvl-avsk-2022` · Điều 8.1 · tr.16 · cần chứa: 'Quyền lợi Thai sản: 270 ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: 6 | 0.00 |
| hybrid3+rerank | E1: 4 | 1.00 |
| hybrid3+rerank+filter | E1: 4 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 2 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 3 |  | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 5 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | Bảng (BẠCH KIM, KIM CƯƠNG) - Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — BẠCH KIM: 21.000.000; KIM CƯƠNG: 31.500.000 - Phí bảo hiểm/ người/năm — BẠC… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 4 |  | `bvl-avsk-2022` · 11,12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 5: Phạm vi địa lý Bảo Việt Nhân thọ chi trả các quyền lợi bảo hiểm của Sản phẩm bổ trợ này khi Chi phí y tế thực tế phát sinh trong phạm vi lãnh thổ Việt N… |
| 5 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG IV: PHÍ BẢO HIỂM | Điều 19: Gia hạn đóng phí bảo hiểm - 19.1. Trường hợp Bên mua bảo hiểm không đóng phí bảo hiểm theo đúng thời hạn đã thoả thuận, Phí bảo hiểm đến hạn của Sản ph… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 5 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Bệnh nhân Điều trị Nội trú phải có mặt liên tục tại Cơ sở y tế trong thời gian điều trị. - 1.12. "Điều trị trong ngày" là việc Người được bảo hiểm có làm thủ … |

</details>

## G12 · table_lookup

**Câu hỏi:** Trong An Vui Song Khoe, chuong trinh nao duoc mua them quyen loi dieu tri ngoai tru va han muc la bao nhieu?

**Đáp án chuẩn:** Chương trình Bạc không áp dụng. Vàng 10 triệu đồng/năm, Bạch Kim 20 triệu đồng/năm, Kim Cương 40 triệu đồng/năm. Người được bảo hiểm tự chi trả 20% chi phí y tế thực tế; giới hạn 10 lần khám/năm.

- **E1** (nhóm thay thế `a`): `bvl-avsk-2022` · Điều 4 - Bảng giới hạn bảo hiểm tối đa · tr.11 · cần chứa: 'B. Quyền lợi Điều trị Ngoại trú'
- **E2** (nhóm thay thế `a`): `bvl-avsk-2022` · Điều 6.2 Quyền lợi Điều trị Ngoại trú · tr.14 · cần chứa: 'Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: —, E2: 5 | 1.00 |
| hybrid3 | E1: —, E2: 10 | 0.00 |
| hybrid3+rerank | E1: 10, E2: 4 | 1.00 |
| hybrid3+rerank+filter | E1: 10, E2: 4 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 3, E2: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 3 |  | `bv-angia-2016` · 22 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › BỤNG | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 70 — QUYỀN LỢI: Cắt bỏ lá lách; TỶ LỆ TRẢ TIỀN: 40-50% - 71 — QUYỀN LỢI: Cắt bỏ đuôi tụy, lách; TỶ LỆ TRẢ TIỀN: 60-70% |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 5 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 4 |  | `bvl-avsk-2022` · 13 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › III. Quyền lợi Cấy ghép nội tạng | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí cho người nhận tạng (là Người được bảo hiểm) - a) Chi phí Điều trị Nội trú — Bạc: Được áp dụng và tính chung … |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Bệnh nhân Điều trị Nội trú phải có mặt liên tục tại Cơ sở y tế trong thời gian điều trị. - 1.12. "Điều trị trong ngày" là việc Người được bảo hiểm có làm thủ … |
| 2 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 3 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 4 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Bệnh nhân Điều trị Nội trú phải có mặt liên tục tại Cơ sở y tế trong thời gian điều trị. - 1.12. "Điều trị trong ngày" là việc Người được bảo hiểm có làm thủ … |
| 2 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 3 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 4 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 3 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 4 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 5 |  | `bvl-avsk-2022` · 13 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › IV. Quyền lợi Điều trị Ngoại trú đặc biệt | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí chạy thận nhân tạo định kỳ — Bạc: 5.000.000 đồng/năm; Vàng: 10.000.000 đồng/năm; Bạch Kim: 15.000.000 đồng/nă… |

</details>

## G13 · multi_condition

**Câu hỏi:** Bao Viet Nhan tho giai quyet quyen loi bao hiem An Vui Song Khoe trong bao lau, va toi phai gui ho so trong thoi han nao?

**Đáp án chuẩn:** Bảo Việt Nhân thọ giải quyết trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ (Điều 21). Hồ sơ phải gửi trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do bất khả kháng (Điều 20).

- **E1**: `bvl-avsk-2022` · Điều 20, Điều 21 · tr.22 · cần chứa: 'trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: — | 0.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 4 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.40. "Theo quy định của Bảo Việt Nhân thọ" dẫn chiếu trong Quy tắc, Điều khoản này được hiểu là quy định do Bảo Việt Nhân thọ ban hành phù hợp với quy định c… |
| 3 |  | `bv-angia-2016` · 3 | Bảo Việt An Gia | . QUY TẮC BẢO HIỂM "BẢO VIỆT AN GIA" (Ban hành theo Quyết định triển khai số 4542 ngày 13 tháng 10 năm 2016 của Tổng Giám đốc - Tổng Công ty Bảo hiểm Bảo Việt) … |
| 4 |  | `bvl-avsk-tomtat-2022` · 1,2 | An Vui Sống Khỏe | 6. Áp dụng tương tự Một số quy định liên quan đến Sản phẩm bổ trợ này sẽ được áp dụng theo Quy tắc, Điều khoản của Sản phẩm chính theo quy định nêu tại Điều 2. … |
| 5 |  | `bvl-avsk-2022` · 3 | An Vui Sống Khỏe | (Phê chuẩn theo Công văn số 2217/BTC-QLBH ngày 08 tháng 03 năm 2022 của Bộ Tài chính) |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bvl-avsk-2022` · 20 | An Vui Sống Khỏe › CHƯƠNG III: THỜI HẠN BẢO HIỂM VÀ HIỆU LỰC CỦA SẢN PHẨM BỔ TRỢ | Điều 14: Chấp nhận, tái tục, khôi phục bảo hiểm có điều kiện Trong trường hợp chấp nhận bảo hiểm hoặc chấp nhận tái tục bảo hiểm hoặc chấp nhận khôi phục bảo hi… |
| 3 |  | `bvl-avsk-2022` · 11,12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 5: Phạm vi địa lý Bảo Việt Nhân thọ chi trả các quyền lợi bảo hiểm của Sản phẩm bổ trợ này khi Chi phí y tế thực tế phát sinh trong phạm vi lãnh thổ Việt N… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.40. "Theo quy định của Bảo Việt Nhân thọ" dẫn chiếu trong Quy tắc, Điều khoản này được hiểu là quy định do Bảo Việt Nhân thọ ban hành phù hợp với quy định c… |
| 5 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 20 | An Vui Sống Khỏe › CHƯƠNG III: THỜI HẠN BẢO HIỂM VÀ HIỆU LỰC CỦA SẢN PHẨM BỔ TRỢ | Điều 14: Chấp nhận, tái tục, khôi phục bảo hiểm có điều kiện Trong trường hợp chấp nhận bảo hiểm hoặc chấp nhận tái tục bảo hiểm hoặc chấp nhận khôi phục bảo hi… |
| 2 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 10: Loại trừ trách nhiệm bảo hiểm Bảo Việt Nhân thọ không trả các Quyền lợi bảo hiểm quy định tại Điều 6 khi xảy ra rủi ro với Người được bảo hiểm trong cá… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.7. Các Bệnh có sẵn, Thương tật có sẵn; Dị tật bẩm sinh, Bệnh bẩm sinh, Bệnh di truyền trừ trường hợp Bảo Việt Nhân thọ đã biết và chấp nhận bảo hiểm; - 10.… |
| 2 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 3 |  | `bvl-avsk-2022` · 20 | An Vui Sống Khỏe › CHƯƠNG III: THỜI HẠN BẢO HIỂM VÀ HIỆU LỰC CỦA SẢN PHẨM BỔ TRỢ | Điều 14: Chấp nhận, tái tục, khôi phục bảo hiểm có điều kiện Trong trường hợp chấp nhận bảo hiểm hoặc chấp nhận tái tục bảo hiểm hoặc chấp nhận khôi phục bảo hi… |
| 4 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 5 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 3 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 5 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |

</details>

## G14 · fact

**Câu hỏi:** Neu khong co yeu cau boi thuong trong 3 nam lien tuc thi An Vui Song Khoe giam phi bao nhieu?

**Đáp án chuẩn:** Giảm 15% phí bảo hiểm của quyền lợi tương ứng cho một năm tái tục tiếp theo (1 năm: 5%, 2 năm: 10%). Chỉ áp dụng tỷ lệ cao nhất, không cộng dồn (Điều 7).

- **E1**: `bvl-avsk-2022` · Điều 7 · tr.16 · cần chứa: '03 năm tham gia liên tục'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: 8 | 0.00 |
| hybrid3+rerank | E1: 4 | 1.00 |
| hybrid3+rerank+filter | E1: 5 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 2 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |
| 5 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Giới hạn cho mỗi lần khám, điều trị Bao gồm: - Khám bệnh; - Thuốc điều trị; - Các kỹ thuật chẩn đoán; - Chi phí Điều … |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 4 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 5 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Giới hạn cho mỗi lần khám, điều trị Bao gồm: - Khám bệnh; - Thuốc điều trị; - Các kỹ thuật chẩn đoán; - Chi phí Điều … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 3 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 4 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Các cơ sở phẫu thuật chuyển đổi giới tính, cơ sở phẫu thuật thẩm mỹ, làm đẹp; - Các viện nghiên cứu khoa học về y khoa (trừ các viện có chức năng điều trị như… |
| 2 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.7. Các Bệnh có sẵn, Thương tật có sẵn; Dị tật bẩm sinh, Bệnh bẩm sinh, Bệnh di truyền trừ trường hợp Bảo Việt Nhân thọ đã biết và chấp nhận bảo hiểm; - 10.… |
| 3 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 5 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 5 |  | `bvl-avsk-2022` · 19,20 | An Vui Sống Khỏe › CHƯƠNG III: THỜI HẠN BẢO HIỂM VÀ HIỆU LỰC CỦA SẢN PHẨM BỔ TRỢ | Điều 12: Thời hạn bảo hiểm Thời hạn bảo hiểm của Sản phẩm bổ trợ là một năm kể từ ngày phát sinh hiệu lực theo quy định tại Điều 11 hoặc ngày tái tục Sản phẩm b… |

</details>

## G15 · exclusion

**Câu hỏi:** An Vui Song Khoe co chi tra dieu tri dong y, cham cuu khong?

**Đáp án chuẩn:** Không. Các phương pháp điều trị không phải Tây y (y học dân tộc, y học cổ truyền, châm cứu, điều trị tại khoa Đông y/Y học cổ truyền/Châm cứu) bị loại trừ theo Điều 10.18.

- **E1**: `bvl-avsk-2022` · Điều 10.18 · tr.18 · cần chứa: 'y học cổ truyền, châm cứu'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: — | 0.00 |
| hybrid3 | E1: 6 | 0.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bv-angia-2016` · 22 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › LỒNG NGỰC | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 53 — QUYỀN LỢI: Cắt bỏ 1 -2 xương sườn; TỶ LỆ TRẢ TIỀN: 15-20% - 54 — QUYỀN LỢI: Cắt bỏ từ 3 xương sườn trở lên; TỶ LỆ TRẢ TI… |
| 3 |  | `bvl-avsk-2022` · 3 | An Vui Sống Khỏe | (Phê chuẩn theo Công văn số 2217/BTC-QLBH ngày 08 tháng 03 năm 2022 của Bộ Tài chính) |
| 4 |  | `bv-angia-2016` · 22 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › BỤNG | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 60 — QUYỀN LỢI: Cắt toàn bộ dạ dày; TỶ LỆ TRẢ TIỀN: 75-85% - 61 — QUYỀN LỢI: Cắt đoạn dạ dày; TỶ LỆ TRẢ TIỀN: 50-60% - 62 — Q… |
| 5 |  | `bv-angia-2016` · 22 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › BỤNG | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 70 — QUYỀN LỢI: Cắt bỏ lá lách; TỶ LỆ TRẢ TIỀN: 40-50% - 71 — QUYỀN LỢI: Cắt bỏ đuôi tụy, lách; TỶ LỆ TRẢ TIỀN: 60-70% |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bvl-avsk-tomtat-2022` · 1,2 | An Vui Sống Khỏe | 6. Áp dụng tương tự Một số quy định liên quan đến Sản phẩm bổ trợ này sẽ được áp dụng theo Quy tắc, Điều khoản của Sản phẩm chính theo quy định nêu tại Điều 2. … |
| 3 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Giới hạn cho mỗi lần khám, điều trị Bao gồm: - Khám bệnh; - Thuốc điều trị; - Các kỹ thuật chẩn đoán; - Chi phí Điều … |
| 4 |  | `bvl-avsk-2022` · 3 | An Vui Sống Khỏe | (Phê chuẩn theo Công văn số 2217/BTC-QLBH ngày 08 tháng 03 năm 2022 của Bộ Tài chính) |
| 5 |  | `bv-angia-2016` · 21 | Bảo Việt An Gia › PHỤ LỤC I: BẢNG TỶ LỆ TRẢ TIỀN THƯƠNG TẬT › CHI DƯỚI | Bảng (QUYỀN LỢI, TỶ LỆ TRẢ TIỀN) - 44 — QUYỀN LỢI: Mất một đốt ngón cái; TỶ LỆ TRẢ TIỀN: 08-12% - 45 — QUYỀN LỢI: Cứng khớp hông; TỶ LỆ TRẢ TIỀN: 45-55% - 46 — … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 3 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao gồm cả Điều… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 5 |  | `bvl-avsk-2022` · 12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Chi phí Điều trị Nội trú (giới hạn cho mỗi Đợt điều trị, không bao gồm Thai sản) — Bạc: 60.000.000 đồng/đợt; Vàng: 10… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 3 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Các cơ sở phẫu thuật chuyển đổi giới tính, cơ sở phẫu thuật thẩm mỹ, làm đẹp; - Các viện nghiên cứu khoa học về y khoa (trừ các viện có chức năng điều trị như… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao gồm cả Điều… |
| 5 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | 1.16. "Điều trị Nha khoa": Điều trị Nha khoa được chi trả theo Sản phẩm bổ trợ này bao gồm: - (i) Điều trị Nha khoa do bệnh lý (thuộc Quyền lợi Điều trị Nha kho… |

</details>

## G16 · comparison

**Câu hỏi:** So sanh thoi gian cho de duoc chi tra quyen loi thai san/sinh con cua Bao Viet An Gia, An Vui Song Khoe va Manulife Cham Soc Suc Khoe Nang Cao.

**Đáp án chuẩn:** Bảo Việt An Gia: sinh nở sau 635 ngày, biến chứng thai sản sau 90 ngày. An Vui Sống Khỏe (Bảo Việt Nhân thọ): 270 ngày. Manulife: 270 ngày.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5 · tr.15 · cần chứa: '635 ngày'
- **E2**: `bvl-avsk-2022` · Điều 8.1 · tr.16 · cần chứa: 'Quyền lợi Thai sản: 270 ngày'
- **E3**: `manulife-cssknc-2026` · Điều 2. Thời gian chờ · tr.10 · cần chứa: '270 ngày Thai sản'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: —, E2: —, E3: — | 0.00 |
| hybrid3 | E1: —, E2: —, E3: — | 0.00 |
| hybrid3+rerank | E1: —, E2: —, E3: — | 0.00 |
| hybrid3+rerank+filter | E1: —, E2: —, E3: — | 0.00 |
| rewrite+hybrid3+rerank+filter | E1: 2, E2: 3, E3: 4 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `daiichi-tktt2015-2025` · 15 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 9.3. Trong thời gian Hợp đồng bảo hiểm có hiệu lực và Người được bảo hiểm còn sống, nếu Người được bảo hiểm hoặc đại diện theo pháp luật của Người được bảo hi… |
| 4 |  | `manulife-cssknc-2026` · 20 | Chăm Sóc Sức Khỏe Nâng Cao › Chương V. HIỆU LỰC CỦA SẢN PHẨM BẢO HIỂM | Điều 16. GIẢI QUYẾT MÂU THUẪN VÀ TRANH CHẤP - 16.1. Hợp Đồng Bảo Hiểm được điều chỉnh và giải thích theo pháp luật của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam. … |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.40. "Theo quy định của Bảo Việt Nhân thọ" dẫn chiếu trong Quy tắc, Điều khoản này được hiểu là quy định do Bảo Việt Nhân thọ ban hành phù hợp với quy định c… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.7. Các Bệnh có sẵn, Thương tật có sẵn; Dị tật bẩm sinh, Bệnh bẩm sinh, Bệnh di truyền trừ trường hợp Bảo Việt Nhân thọ đã biết và chấp nhận bảo hiểm; - 10.… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 25 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 46. Phẫu Thuật Trong Ngày — col1: Là hình thức Phẫu Thuật mà Người Được Bảo Hiểm nhập viện và điều trị tại Bệnh Viện nhưng không nằm qua đêm. Manu… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 25 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 46. Phẫu Thuật Trong Ngày — col1: Là hình thức Phẫu Thuật mà Người Được Bảo Hiểm nhập viện và điều trị tại Bệnh Viện nhưng không nằm qua đêm. Manu… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 3 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 | ✅ E3 | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 5 |  | `bv-angia-2016` · 5 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 12. Thời hạn bảo hiểm Thời hạn bảo hiểm được quy định cụ thể trong Hợp đồng bảo hiểm hoặc Giấy chứng nhận bảo hiểm. Thời hạn bảo hiểm là một (01) năm, không chấ… |

</details>

## G17 · comparison

**Câu hỏi:** Gioi han quyen loi thai san cua goi Kim Cuong trong Bao Viet An Gia khac gi so voi goi Kim Cuong cua Manulife?

**Đáp án chuẩn:** An Gia Kim Cương: tối đa 31.500.000 đồng cho một thời hạn bảo hiểm (phí bảo hiểm thai sản 5.500.000 đồng/người/năm). Manulife Kim Cương: tối đa 70 triệu đồng cho mỗi lần mang thai (gồm sinh thường, sinh mổ, biến chứng thai sản), đồng chi trả 20%.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5: Bảo hiểm thai sản · tr.15 · cần chứa: '31.500.000'
- **E2**: `manulife-cssknc-2026` · Điều 1.4 Quyền lợi thai sản · tr.9 · cần chứa: 'Giới hạn tối đa cho mỗi lần mang thai', '70 triệu'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: —, E2: — | 0.00 |
| hybrid3 | E1: —, E2: — | 0.00 |
| hybrid3+rerank | E1: 5, E2: — | 0.50 |
| hybrid3+rerank+filter | E1: 4, E2: — | 0.50 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 5 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 32. Đồng Chi Trả — col1: Là việc Bên Mua Bảo Hiểm và Manulife cùng chi trả cho Chi Phí Y Tế Thực Tế phát sinh. Mức Đồng Chi Trả là tỷ lệ phần trăm… |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | (*) Mức Đồng Chi Trả: Mức Đồng Chi Trả được ghi nhận tại thời điểm phát hành hợp đồng sẽ áp dụng xuyên suốt thời hạn hợp đồng (bao gồm thời gian tái tục). Trong… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 5 |  | `daiichi-tktt2015-2025` · 15 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 10: TRƯỜNG HỢP KÊ KHAI NHẦM TUỔI VÀ GIỚI TÍNH CỦA NGƯỜI ĐƯỢC BẢO HIỂM - 10.1. Nếu có nhầm lẫn (không do lỗi cung cấp thông tin của Bên mua bảo hiểm hoặc Ng… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |
| 4 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |
| 5 |  | `manulife-cssknc-2026` · 10,11 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 3. CÁC TRƯỜNG HỢP LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM Manulife sẽ không chi trả quyền lợi bảo hiểm phát sinh từ, liên quan đến hay là hậu quả của bất kỳ trường h… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 45. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người được… |
| 2 |  | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 44. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người được… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 5 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 2 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 45. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người được… |
| 3 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 4 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | Bảng (BẠCH KIM, KIM CƯƠNG) - Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — BẠCH KIM: 21.000.000; KIM CƯƠNG: 31.500.000 - Phí bảo hiểm/ người/năm — BẠC… |
| 2 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |
| 4 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 5 | ✅ E2 | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản (là tổng quyền lợi bảo hiểm… |

</details>

## G18 · versioning

**Câu hỏi:** Quy tac va Dieu khoan san pham Tu ky tai tuc hang thang (2015) cua Dai-ichi Life hien duoc ban hanh theo van ban nao?

**Đáp án chuẩn:** Sản phẩm được Bộ Tài chính phê chuẩn theo công văn 14187/BTC-QLBH ngày 09/10/2015 (và công văn 8361/BTC-QLBH ngày 23/06/2017, 623/BTC-QLBH ngày 16/01/2020). Quy tắc và Điều khoản hiện hành được sửa đổi và ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025.

- **E1**: `daiichi-tktt2015-2025` · Trang bìa Quy tắc và Điều khoản · tr.4 · cần chứa: '424/GD/Dai-ichi/2025'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 4 | 1.00 |
| hybrid3 | E1: 3 | 1.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 17,18 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 2: CÁC ĐIỀU KHOẢN VỀ QUYỀN LỢI BẢO HIỂM Điều 13: QUYỀN LỢI TRONG TRƯỜNG HỢP NGƯỜI ĐƯỢC BẢO HIỂM TỬ VONG HOẶC THƯƠNG TẬT… | - c. Tham gia vào các hoạt động bất hợp pháp, chống cự khi bị bắt giữ hay vượt ngục; hoặc - d. Chấn thương do tham gia các cuộc đua, các loại hình thể thao chuy… |
| 2 |  | `daiichi-tktt2015-2025` · 15 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 10: TRƯỜNG HỢP KÊ KHAI NHẦM TUỔI VÀ GIỚI TÍNH CỦA NGƯỜI ĐƯỢC BẢO HIỂM - 10.1. Nếu có nhầm lẫn (không do lỗi cung cấp thông tin của Bên mua bảo hiểm hoặc Ng… |
| 3 |  | `daiichi-tktt2015-2025` · 17,18 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 2: CÁC ĐIỀU KHOẢN VỀ QUYỀN LỢI BẢO HIỂM Điều 13: QUYỀN LỢI TRONG TRƯỜNG HỢP NGƯỜI ĐƯỢC BẢO HIỂM TỬ VONG HOẶC THƯƠNG TẬT… | Điều 14: CÁC ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM - 14.1. Loại trừ bảo hiểm đối với trường hợp tử vong: Dai-ichi Life Việt Nam sẽ không chi trả quyền lợi bả… |
| 4 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 5 |  | `daiichi-tktt2015-2025` · 7 | Tử kỳ tái tục hàng tháng (2015) | CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm này, các thuật ngữ và từ ngữ viết tắt được hiểu và giải… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.6. Chấp nhận bảo hiểm có điều kiện - a. Trường hợp Bên mua bảo hiểm và/hoặc Người được bảo hiểm vi phạm nghĩa vụ cung cấp đối với bất kỳ thông tin nào về sức … |
| 2 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.1. Nghĩa vụ cung cấp thông tin của Bên mua bảo hiểm, Người được bảo hiểm - a. Bên mua bảo hiểm và Người được bảo hiểm có nghĩa vụ cung cấp đầy đủ và chính xác… |
| 3 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 4 |  | `daiichi-tktt2015-2025` · 15 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 9.3. Trong thời gian Hợp đồng bảo hiểm có hiệu lực và Người được bảo hiểm còn sống, nếu Người được bảo hiểm hoặc đại diện theo pháp luật của Người được bảo hi… |
| 5 |  | `daiichi-tktt2015-2025` · 15 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 10: TRƯỜNG HỢP KÊ KHAI NHẦM TUỔI VÀ GIỚI TÍNH CỦA NGƯỜI ĐƯỢC BẢO HIỂM - 10.1. Nếu có nhầm lẫn (không do lỗi cung cấp thông tin của Bên mua bảo hiểm hoặc Ng… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Hoặc - e. Các trường hợp/điều kiện cụ thể khác (nếu có) theo quy định của Dai-ichi Life Việt Nam tại từng thời điểm. - 1.6. Hồ sơ yêu cầu bảo hiểm: là toàn bộ t… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 4 |  | `daiichi-tktt2015-2025` · 2,3 | Tử kỳ tái tục hàng tháng (2015) › IV. NGHĨA VỤ KÊ KHAI THÔNG TIN TRUNG THỰC | Quy định chi tiết tại Điều 4.1 của QTĐK Quý khách lưu ý phải kê khai đầy đủ và chính xác tất cả thông tin cần thiết để Dai-ichi Life Việt Nam đánh giá khả năng … |
| 5 |  | `daiichi-tktt2015-2025` · 15,16,17 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - (ii) Trong trường hợp có bất kỳ sự thay đổi nghề nghiệp/việc làm của Người được bảo hiểm hoặc Người được bảo hiểm xuất cảnh ngoài Điều kiện chuẩn, không phụ t… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Hoặc - e. Các trường hợp/điều kiện cụ thể khác (nếu có) theo quy định của Dai-ichi Life Việt Nam tại từng thời điểm. - 1.6. Hồ sơ yêu cầu bảo hiểm: là toàn bộ t… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 4 |  | `daiichi-tktt2015-2025` · 2,3 | Tử kỳ tái tục hàng tháng (2015) › IV. NGHĨA VỤ KÊ KHAI THÔNG TIN TRUNG THỰC | Quy định chi tiết tại Điều 4.1 của QTĐK Quý khách lưu ý phải kê khai đầy đủ và chính xác tất cả thông tin cần thiết để Dai-ichi Life Việt Nam đánh giá khả năng … |
| 5 |  | `daiichi-tktt2015-2025` · 15,16,17 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - (ii) Trong trường hợp có bất kỳ sự thay đổi nghề nghiệp/việc làm của Người được bảo hiểm hoặc Người được bảo hiểm xuất cảnh ngoài Điều kiện chuẩn, không phụ t… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - b. được thể hiện dưới dạng bằng văn bản giấy hoặc giao dịch/dữ liệu điện tử theo quy định của pháp luật về giao dịch điện tử. - 1.8. Hợp đồng tiết kiệm tích l… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | - (iii) Các điều kiện bảo hiểm khác theo quy định của Dai-ichi Life Việt Nam và quy định pháp luật tại từng thời điểm. - b. Dai-ichi Life Việt Nam sẽ gửi thông … |
| 5 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |

</details>

## G19 · no_diacritics

**Câu hỏi:** thoi han bao hiem cua tu ky tai tuc hang thang dai ichi la bao lau, NDBH toi da bao nhieu tuoi

**Đáp án chuẩn:** Thời hạn bảo hiểm là 01 tháng kể từ ngày hiệu lực hợp đồng và được gia hạn hàng tháng nếu hợp đồng không chấm dứt theo Điều 7 (Điều 1.21). Người được bảo hiểm từ 18 đến 75 tuổi khi tham gia; tuổi tối đa khi kết thúc thời hạn bảo hiểm là 76 tuổi (Điều 1.13).

- **E1**: `daiichi-tktt2015-2025` · Điều 1.21 · tr.9 · cần chứa: '1.21. Thời hạn bảo hiểm'
- **E2**: `daiichi-tktt2015-2025` · Điều 1.13 · tr.8 · cần chứa: '76 (bảy mươi sáu) tuổi'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: —, E2: — | 0.00 |
| hybrid3 | E1: —, E2: — | 0.00 |
| hybrid3+rerank | E1: —, E2: 1 | 0.50 |
| hybrid3+rerank+filter | E1: —, E2: 1 | 0.50 |
| rewrite+hybrid3+rerank+filter | E1: —, E2: 1 | 0.50 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 3 | Tử kỳ tái tục hàng tháng (2015) | VI. TRƯỜNG HỢP CHẤM DỨT HỢP ĐỒNG BẢO HIỂM TRƯỚC HẠN Quy định chi tiết tại Điều 7 của QTĐK HĐBH được chấm dứt trước hạn theo yêu cầu của BMBH hoặc khi Phí bảo hi… |
| 2 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |
| 3 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 5. Các hành động đánh nhau của Người được bảo hiểm, trừ khi chứng minh được hành động đánh nhau đó chỉ với mục đích tự vệ. 6. Hậu quả của tai nạn xảy ra ngoài t… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 2 |  | `daiichi-tktt2015-2025` · 3 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | Ngoài các nội dung nêu trên, Quý khách cần lưu ý một số nội dung sau: - Tuân thủ nghĩa vụ đóng phí bảo hiểm đầy đủ, đúng hạn theo định kỳ đóng phí trong HĐBH, n… |
| 3 |  | `daiichi-tktt2015-2025` · 10,11 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 2: QUYỀN LỢI CÓ THỂ ĐƯỢC BẢO HIỂM Tại thời điểm yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm phải có quyền lợi có thể được bảo hiểm với Người được bảo hiểm … |
| 4 |  | `daiichi-tktt2015-2025` · 2,3 | Tử kỳ tái tục hàng tháng (2015) › IV. NGHĨA VỤ KÊ KHAI THÔNG TIN TRUNG THỰC | Quy định chi tiết tại Điều 4.1 của QTĐK Quý khách lưu ý phải kê khai đầy đủ và chính xác tất cả thông tin cần thiết để Dai-ichi Life Việt Nam đánh giá khả năng … |
| 5 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.6. Chấp nhận bảo hiểm có điều kiện - a. Trường hợp Bên mua bảo hiểm và/hoặc Người được bảo hiểm vi phạm nghĩa vụ cung cấp đối với bất kỳ thông tin nào về sức … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 2 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 5. Các hành động đánh nhau của Người được bảo hiểm, trừ khi chứng minh được hành động đánh nhau đó chỉ với mục đích tự vệ. 6. Hậu quả của tai nạn xảy ra ngoài t… |
| 4 |  | `daiichi-tktt2015-2025` · 7 | Tử kỳ tái tục hàng tháng (2015) | CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm này, các thuật ngữ và từ ngữ viết tắt được hiểu và giải… |
| 5 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Hoặc - e. Các trường hợp/điều kiện cụ thể khác (nếu có) theo quy định của Dai-ichi Life Việt Nam tại từng thời điểm. - 1.6. Hồ sơ yêu cầu bảo hiểm: là toàn bộ t… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 2 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 7 | Tử kỳ tái tục hàng tháng (2015) | CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm này, các thuật ngữ và từ ngữ viết tắt được hiểu và giải… |
| 4 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Hoặc - e. Các trường hợp/điều kiện cụ thể khác (nếu có) theo quy định của Dai-ichi Life Việt Nam tại từng thời điểm. - 1.6. Hồ sơ yêu cầu bảo hiểm: là toàn bộ t… |
| 5 |  | `daiichi-tktt2015-2025` · 14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 7: CHẤM DỨT HỢP ĐỒNG BẢO HIỂM Hợp đồng bảo hiểm này sẽ chấm dứt hiệu lực trong các trường hợp sau: - 7.1. Bên mua bảo hiểm yêu cầu chấm dứt Hợp đồng bảo hi… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 2 |  | `daiichi-tktt2015-2025` · 14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 7: CHẤM DỨT HỢP ĐỒNG BẢO HIỂM Hợp đồng bảo hiểm này sẽ chấm dứt hiệu lực trong các trường hợp sau: - 7.1. Bên mua bảo hiểm yêu cầu chấm dứt Hợp đồng bảo hi… |
| 3 |  | `daiichi-tktt2015-2025` · 14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Điều 6: THỜI GIAN GIA HẠN ĐÓNG PHÍ BẢO HIỂM VÀ MẤT HIỆU LỰC HỢP ĐỒNG - 6.1. Thời gian gia hạn đóng Phí bảo hiểm là 60 (sáu mươi) ngày và sẽ bắt đầu tính từ Ngày… |
| 4 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Việc chứng nhận Người được bảo hiểm bị liệt hoàn toàn và không thể phục hồi chức năng của (các) bộ phận cơ thể hoặc mù hoàn toàn phải được thực hiện không sớm h… |
| 5 |  | `daiichi-tktt2015-2025` · 7 | Tử kỳ tái tục hàng tháng (2015) | CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm này, các thuật ngữ và từ ngữ viết tắt được hiểu và giải… |

</details>

## G20 · no_diacritics

**Câu hỏi:** STBH bao hiem tai nan ca nhan trong An Gia toi da bao nhieu va phi tinh the nao

**Đáp án chuẩn:** Số tiền bảo hiểm tai nạn cá nhân tối đa 1 tỷ đồng/người/vụ (mọi chương trình). Phí bằng 0,09% STBH/năm.

- **E1**: `bv-angia-2016` · Bảng quyền lợi - B.2 Bảo hiểm tai nạn cá nhân · tr.24-25 · cần chứa: 'Tai nạn cá nhân', 'Tối đa 1 tỷ đồng'
- **E2**: `bv-angia-2016` · Biểu phí - B.2 BH tai nạn cá nhân · tr.26 · cần chứa: '0,09% STBH'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 7, E2: 6 | 0.00 |
| hybrid3 | E1: 5, E2: 1 | 1.00 |
| hybrid3+rerank | E1: 1, E2: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 1, E2: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 5 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |
| 2 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 1. Điều trị ngoại trú do ốm bệnh, tai nạn — ĐỒNG: 6.000.000/NĂM; BẠC: 6.000.000/năm; VÀNG: 6.000.000/năm; BẠCH KIM… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 1. Điều trị ngoại trú do ốm bệnh, tai nạn — ĐỒNG: 6.000.000/NĂM; BẠC: 6.000.000/năm; VÀNG: 6.000.000/năm; BẠCH KIM… |
| 2 | ✅ E2 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 4 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 5 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 1. Điều trị ngoại trú do ốm bệnh, tai nạn — ĐỒNG: 6.000.000/NĂM; BẠC: 6.000.000/năm; VÀNG: 6.000.000/năm; BẠCH KIM… |
| 2 | ✅ E2 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 4 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 5 |  | `bv-angia-2016` · 14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 2: BẢO HIỂM TAI NẠN CÁ NHÂN | 1. Quyền lợi bảo hiểm Bảo hiểm cho trường hợp chết, thương tật toàn bộ vĩnh viễn hoặc thương tật bộ phận vĩnh viễn do tai nạn xảy ra trong thời hạn bảo hiểm. - … |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 1. Điều trị ngoại trú do ốm bệnh, tai nạn — ĐỒNG: 6.000.000/NĂM; BẠC: 6.000.000/năm; VÀNG: 6.000.000/năm; BẠCH KIM… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |
| 5 | ✅ E2 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |

</details>

