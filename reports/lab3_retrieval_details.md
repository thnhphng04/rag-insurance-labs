# Lab 3 – Kết quả truy xuất từng câu (gốc)

Sinh tự động. ✅ = chunk chứa đủ đoạn trích của bằng chứng (E1, E2… theo thứ tự trong golden set). Hiển thị top-5; hạng của bằng chứng tính đến top-10 (`—` = ngoài top-10).

## G01 · table_lookup

**Câu hỏi:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là bao nhiêu một năm?

**Đáp án chuẩn:** 1.887.600 đồng/người/năm (biểu phí An Gia, điều khoản chính, nhóm tuổi từ 31 đến 40).

- **E1**: `bv-angia-2016` · Biểu phí bảo hiểm - A. Điều khoản bảo hiểm chính · tr.26 · cần chứa: 'Từ 31 đến 40 tuổi', '1.887.600'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 2 | 1.00 |
| hybrid3 | E1: 2 | 1.00 |
| hybrid3+rerank | E1: 3 | 1.00 |
| hybrid3+rerank+filter | E1: 3 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | a. Trường hợp nằm viện Trường hợp Người được bảo hiểm phải nằm viện thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt sẽ thanh toán các chi phí điều trị, tiền phòng và … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.794.000; BẠC: 1.794.000; VÀNG: 1.794.000; BẠCH KIM: 2.990.000; KIM CƯƠNG: 4.485.000 - … |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 3 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 3 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |

</details>

## G02 · table_lookup

**Câu hỏi:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là bao nhiêu?

**Đáp án chuẩn:** 230.000.000 đồng/người/năm. Lưu ý bảng quyền lợi gốc in là "230.00 0.000/ng/năm".

- **E1**: `bv-angia-2016` · Bảng quyền lợi bảo hiểm - A. Điều khoản bảo hiểm chính · tr.24-25 · cần chứa: 'Tổng hạn mức quyền lợi bảo hiểm chính', '230.00 0.000'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 8. Bảng quyền lợi bảo hiểm Bảng quyền lợi bảo hiểm cung cấp các thông tin tóm tắt về quyền lợi bảo hiểm. Bảng quyền lợi bảo hiểm được cấp cùng và là bộ phận khô… |
| 3 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 10. Giới hạn phụ Là giới hạn bồi thường tối đa cho mỗi hạng mục được quy định chi tiết trong Bảng quyền lợi bảo hiểm. Trong mọi trường hợp, tổng số tiền bồi thư… |
| 4 |  | `bv-taman-2019` · 4,5 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 8. Bảng quyền lợi bảo hiểm Bảng quyền lợi bảo hiểm cung cấp các thông tin tóm tắt về quyền lợi bảo hiểm. Bảng quyền lợi bảo hiểm được cấp cùng và là bộ phận khô… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |

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

**Câu hỏi:** Với quyền lợi thai sản của Manulife Chăm Sóc Sức Khỏe Nâng Cao, chi phí sinh được chi trả như thế nào?

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
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 13 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.1. Người nhận quyền lợi bảo hiểm Trừ trường hợp có thỏa thuận khác giữa Manulife và Bên Mua Bảo Hiểm, các quyền lợi bảo hiểm nêu tại Sản Phẩm Bảo Hiểm này sẽ … |
| 4 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | (*) Mức Đồng Chi Trả: Mức Đồng Chi Trả được ghi nhận tại thời điểm phát hành hợp đồng sẽ áp dụng xuyên suốt thời hạn hợp đồng (bao gồm thời gian tái tục). Trong… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 32. Đồng Chi Trả — col1: Là việc Bên Mua Bảo Hiểm và Manulife cùng chi trả cho Chi Phí Y Tế Thực Tế phát sinh. Mức Đồng Chi Trả là tỷ lệ phần trăm… |
| 4 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |
| 5 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |
| 4 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản (là tổng quyền lợi bảo hiểm… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - D. Chi Phí Dưỡng Nhi/ năm hợp đồng (trong vòng 7 ngày kể từ ngày sinh, LOẠI TRỪ Bệnh Bẩm Sinh/ Dị Tật Bẩm Sinh) — TITA… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |
| 4 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản (là tổng quyền lợi bảo hiểm… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - D. Chi Phí Dưỡng Nhi/ năm hợp đồng (trong vòng 7 ngày kể từ ngày sinh, LOẠI TRỪ Bệnh Bẩm Sinh/ Dị Tật Bẩm Sinh) — TITA… |

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

**Câu hỏi:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho ai và sau bao lâu thì được chi trả chi phí sinh nở?

**Đáp án chuẩn:** Người được bảo hiểm từ 18 đến 45 tuổi, phải tham gia điều khoản chính tương đương chương trình Bạch Kim hoặc Kim Cương. Chi phí sinh nở chỉ được chi trả sau 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản sau 90 ngày. Giới hạn tối đa 21.000.000 (Bạch Kim) / 31.500.000 (Kim Cương) cho một thời hạn bảo hiểm.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5: Bảo hiểm thai sản · tr.15 · cần chứa: '635 ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 5 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |

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

**Câu hỏi:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ nào?

**Đáp án chuẩn:** Áp dụng đồng chi trả 70/30: Bảo Việt chi trả 70%, người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (trừ khoa điều trị tự nguyện/theo yêu cầu của bệnh viện công lập).

- **E1**: `bv-angia-2016` · Bảng quyền lợi - Quy định đồng chi trả đối với trẻ em · tr.24-25 · cần chứa: '70/30'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 4 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn bao gồm cả biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiể… |
| 5 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › I. ĐỊNH NGHĨA | 4. Người phụ thuộc Là con của Người được bảo hiểm theo luật pháp có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khóa học dài hạn và c… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 4 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham gia Điều khoản bổ sung này các chi phí y tế phát sinh điều trị ngoại trú do ố… |
| 5 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn bao gồm cả biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiể… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham gia Điều khoản bổ sung này các chi phí y tế phát sinh điều trị ngoại trú do ố… |
| 4 |  | `bv-angia-2016` · 12 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm - Bảo hiểm cho trường hợp ốm đau, bệnh tật, tai nạn bao gồm cả biến chứng thai sản xảy ra trong thời hạn bảo hiểm khiến Người được bảo hiể… |
| 5 |  | `bv-angia-2016` · 9 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 50. Đồng chi trả Đồng chi trả là số tiền theo tỷ lệ mà Công ty bảo hiểm, Người được bảo hiểm cùng chi trả khi phát sinh chi phí thuộc phạm vi bảo hiểm của Quy t… |

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

**Câu hỏi:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là bao lâu?

**Đáp án chuẩn:** 01 năm đối với bệnh có sẵn (và các bệnh tại điểm loại trừ chung số 36), 01 năm đối với bệnh đặc biệt. Ngoài ra: ốm đau bệnh tật 30 ngày, biến chứng thai sản 90 ngày, trẻ em đến 6 tuổi bị viêm phế quản/tiểu phế quản/viêm phổi 06 tháng.

- **E1** (nhóm thay thế `a`): `bv-angia-2016` · Phần II - 2. Hiệu lực bảo hiểm · tr.13 · cần chứa: '01 năm đối với bệnh có sẵn', '01 năm đối với bệnh đặc biệt'
- **E2** (nhóm thay thế `a`): `bv-angia-2016` · Điều khoản bổ sung 1 - 2. Hiệu lực bảo hiểm · tr.14 · cần chứa: '01 năm đối với bệnh có sẵn', '01 năm đối với bệnh đặc biệt'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1, E2: 1 | 1.00 |
| hybrid3 | E1: 1, E2: 1 | 1.00 |
| hybrid3+rerank | E1: 1, E2: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1, E2: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 3 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 4 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 3 |  | `bv-taman-2019` · 14 | Bảo Việt Tâm An › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH - ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN, BIẾN CHỨNG THAI SẢN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ thời điểm bảo hiểm có hiệu lực theo quy định tại Điểm 11, Phần I Quy tắc bảo hiểm này… |
| 4 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 3 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 4 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 31. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 32. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 5 |  | `bv-taman-2019` · 14 | Bảo Việt Tâm An › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH - ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN, BIẾN CHỨNG THAI SẢN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ thời điểm bảo hiểm có hiệu lực theo quy định tại Điểm 11, Phần I Quy tắc bảo hiểm này… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 3 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 4 |  | `bv-angia-2016` · 14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 3: BẢO HIỂM SINH MẠNG | 1. Phạm vi bảo hiểm Bảo hiểm trường hợp chết hoặc tàn tật toàn bộ vĩnh viễn do nguyên nhân không phải là tai nạn xảy ra trong thời hạn bảo hiểm trừ những điểm l… |
| 5 |  | `bv-angia-2016` · 5 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 19. Ốm đau, bệnh tật Là tình trạng cơ thể có dấu hiệu của một bệnh lý khác với tình trạng sức khỏe bình thường được biểu hiện bằng các triệu chứng hay hội chứng… |

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

**Câu hỏi:** Bảo Việt Tâm An nhận bảo hiểm cho người ở độ tuổi nào?

**Đáp án chuẩn:** Từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 đến 63 tuổi chỉ được tham gia mới nếu có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ.

- **E1**: `bv-taman-2019` · Phần I - II. Đối tượng tham gia bảo hiểm · tr.10 · cần chứa: 'sáu mươi ba (63) tuổi'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 2 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 3 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 4 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 5 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 4 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 2. Người được bảo hiểm Là cá nhân có tính mạng hoặc tình trạng sức khỏe được bảo hiểm theo Hợp đồng bảo hiểm/Giấy chứng nhận bảo hiểm. Người được bảo hiểm đã ho… |
| 5 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 4 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 2. Người được bảo hiểm Là cá nhân có tính mạng hoặc tình trạng sức khỏe được bảo hiểm theo Hợp đồng bảo hiểm/Giấy chứng nhận bảo hiểm. Người được bảo hiểm đã ho… |
| 5 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 2 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 4. Người phụ thuộc Là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khó… |
| 4 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 2. Người được bảo hiểm Là cá nhân có tính mạng hoặc tình trạng sức khỏe được bảo hiểm theo Hợp đồng bảo hiểm/Giấy chứng nhận bảo hiểm. Người được bảo hiểm đã ho… |
| 5 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |

</details>

## G08 · table_lookup

**Câu hỏi:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công bao nhiêu?

**Đáp án chuẩn:** 300.000 đồng/ngày, không quá 60 ngày/năm.

- **E1**: `bv-taman-2019` · Bảng quyền lợi bảo hiểm sức khỏe Bảo Việt Tâm An - mục 8 · tr.22 · cần chứa: 'Trợ cấp bệnh viện công', '300.000/ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 35. Trợ cấp cho Người được bảo hiểm Là khoản tiền trợ cấp cho Người được bảo hiểm trong trường hợp Người được bảo hiểm mắc 01 hoặc nhiều hơn 01 bệnh trong 22 bệ… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 4 |  | `bv-angia-2016` · 7 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 36. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn tại các bệnh viện công lập. … |
| 5 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 5 |  | `bv-taman-2019` · 13 | Bảo Việt Tâm An › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH - ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN, BIẾN CHỨNG THAI SẢN | b. Trường hợp phẫu thuật Trường hợp Người được bảo hiểm phải phẫu thuật phải nằm viện điều trị nội trú thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt sẽ thanh toán t… |

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

**Câu hỏi:** Hồ sơ yêu cầu bồi thường Bảo Việt Tâm An phải nộp trong thời hạn nào và Bảo hiểm Bảo Việt giải quyết trong bao lâu?

**Đáp án chuẩn:** Nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng của đợt điều trị (hoặc ngày tử vong) và không quá 01 năm kể từ ngày xảy ra sự kiện bảo hiểm (không tính thời gian bất khả kháng). Bảo hiểm Bảo Việt giải quyết và chi trả trong vòng 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ.

- **E1** (nhóm thay thế `a`): `bv-taman-2019` · Phần I - IX. Thời hạn khiếu nại và trả tiền bảo hiểm · tr.12 · cần chứa: 'sáu mươi (60) ngày kể từ ngày điều trị cuối cùng', 'mười lăm (15) ngày'
- **E2** (nhóm thay thế `a`): `bv-taman-2019` · Phần V - Thủ tục yêu cầu trả tiền bảo hiểm · tr.18 · cần chứa: 'sáu mươi (60) ngày kể từ ngày điều trị cuối cùng'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1, E2: 1 | 1.00 |
| hybrid3 | E1: 1, E2: 1 | 1.00 |
| hybrid3+rerank | E1: 1, E2: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1, E2: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 3 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 3 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 4 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |
| 5 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 3 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 3 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 4 |  | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | 3. Các chứng từ là bản gốc liên quan đến việc thanh toán chi phí y tế: hóa đơn tài chính, biên lai, phiếu thu theo quy định của Bộ Tài Chính, Tổng cục Thuế và b… |
| 5 |  | `bv-taman-2019` · 5 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 10. Giới hạn phụ Là giới hạn bồi thường tối đa cho mỗi hạng mục được quy định chi tiết trong Bảng quyền lợi bảo hiểm. Trong mọi trường hợp, tổng số tiền bồi thư… |

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

**Câu hỏi:** Nếu tôi tự yêu cầu hủy hợp đồng Bảo Việt Tâm An thì được hoàn lại bao nhiêu phí?

**Đáp án chuẩn:** Bảo hiểm Bảo Việt hoàn trả 80% phí bảo hiểm của thời gian còn lại, với điều kiện trong thời gian hiệu lực chưa có khiếu nại đòi trả tiền bảo hiểm nào. (Nếu Bảo hiểm Bảo Việt yêu cầu hủy thì hoàn toàn bộ phí của thời gian còn lại; trường hợp gian lận chỉ hoàn 70% nếu chưa có bồi thường.)

- **E1**: `bv-taman-2019` · Phần I - III. Ký kết/hủy bỏ hợp đồng bảo hiểm · tr.11 · cần chứa: 'hoàn trả 80% phí bảo hiểm'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 2 | 1.00 |
| hybrid3 | E1: 2 | 1.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 4 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | V. PHÍ BẢO HIỂM VÀ SỐ TIỀN BẢO HIỂM Phí bảo hiểm quy định trong Biểu phí đính kèm Quy tắc bảo hiểm này, phí bảo hiểm phụ thuộc vào chương trình bảo hiểm, độ tuổ… |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 4 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Người được bảo hiểm phải kê khai trung thực đầy đủ nội du… |
| 5 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 2. (i) Đơn phương hủy bỏ toàn bộ Hợp đồng bảo hiểm Theo đó, Hợp đồng bảo hiểm không có hiệu lực từ thời điểm được Dai-ichi Life Việt Nam chấp thuận bảo hiểm. Kh… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 4 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Người được bảo hiểm phải kê khai trung thực đầy đủ nội du… |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 5 |  | `bv-taman-2019` · 8,9 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 41. Thuốc kê theo Đơn của bác sỹ Là những thuốc, dược phẩm được bán và sử dụng theo Đơn của Bác sỹ, theo quy định của pháp luật và không bao gồm thực phẩm chức … |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 4 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

## G11 · fact

**Câu hỏi:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là bao lâu?

**Đáp án chuẩn:** 270 ngày (Điều 8.1). Các sự kiện do tai nạn không áp dụng thời gian chờ.

- **E1**: `bvl-avsk-2022` · Điều 8.1 · tr.16 · cần chứa: 'Quyền lợi Thai sản: 270 ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 5 | 1.00 |
| hybrid3 | E1: 2 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 5 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 4 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 5 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 5 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Bệnh nhân Điều trị Nội trú phải có mặt liên tục tại Cơ sở y tế trong thời gian điều trị. - 1.12. "Điều trị trong ngày" là việc Người được bảo hiểm có làm thủ … |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 5 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | - Bệnh nhân Điều trị Nội trú phải có mặt liên tục tại Cơ sở y tế trong thời gian điều trị. - 1.12. "Điều trị trong ngày" là việc Người được bảo hiểm có làm thủ … |

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

**Câu hỏi:** Trong An Vui Sống Khỏe, chương trình nào được mua thêm quyền lợi điều trị ngoại trú và hạn mức là bao nhiêu?

**Đáp án chuẩn:** Chương trình Bạc không áp dụng. Vàng 10 triệu đồng/năm, Bạch Kim 20 triệu đồng/năm, Kim Cương 40 triệu đồng/năm. Người được bảo hiểm tự chi trả 20% chi phí y tế thực tế; giới hạn 10 lần khám/năm.

- **E1** (nhóm thay thế `a`): `bvl-avsk-2022` · Điều 4 - Bảng giới hạn bảo hiểm tối đa · tr.11 · cần chứa: 'B. Quyền lợi Điều trị Ngoại trú'
- **E2** (nhóm thay thế `a`): `bvl-avsk-2022` · Điều 6.2 Quyền lợi Điều trị Ngoại trú · tr.14 · cần chứa: 'Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 2, E2: 1 | 1.00 |
| hybrid3 | E1: 9, E2: 3 | 1.00 |
| hybrid3+rerank | E1: 3, E2: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 3, E2: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 3, E2: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 2 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 3 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 5 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Giới hạn cho mỗi lần khám, điều trị Bao gồm: - Khám bệnh; - Thuốc điều trị; - Các kỹ thuật chẩn đoán; - Chi phí Điều … |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 2 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 3 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 5 |  | `manulife-cssknc-2026` · 12 | Chăm Sóc Sức Khỏe Nâng Cao › Chương II. QUYỀN VÀ NGHĨA VỤ CỦA BÊN MUA BẢO HIỂM › Điều 4. QUYỀN CỦA BÊN MUA BẢO HIỂM | 4.2. Bổ sung, chấm dứt quyền lợi lựa chọn thêm Trong thời gian Sản Phẩm Bảo Hiểm này có hiệu lực, Bên Mua Bảo Hiểm có thể yêu cầu bổ sung, chấm dứt quyền lợi lự… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 3 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 4 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 5 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 3 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 4 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |
| 5 |  | `bvl-avsk-2022` · 13 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › IV. Quyền lợi Điều trị Ngoại trú đặc biệt | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí chạy thận nhân tạo định kỳ — Bạc: 5.000.000 đồng/năm; Vàng: 10.000.000 đồng/năm; Bạch Kim: 15.000.000 đồng/nă… |

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

**Câu hỏi:** Bảo Việt Nhân thọ giải quyết quyền lợi bảo hiểm An Vui Sống Khỏe trong bao lâu, và tôi phải gửi hồ sơ trong thời hạn nào?

**Đáp án chuẩn:** Bảo Việt Nhân thọ giải quyết trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ (Điều 21). Hồ sơ phải gửi trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do bất khả kháng (Điều 20).

- **E1**: `bvl-avsk-2022` · Điều 20, Điều 21 · tr.22 · cần chứa: 'trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 2 | 1.00 |
| hybrid3+rerank | E1: 2 | 1.00 |
| hybrid3+rerank+filter | E1: 2 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 2 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | - Các bằng chứng hoặc các giấy tờ bổ sung cần thiết khác (nếu có) theo yêu cầu của Bảo Việt Nhân thọ để phục vụ cho việc giải quyết quyền lợi bảo hiểm. - Trường… |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 3 |  | `bvl-avsk-2022` · 11,12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 5: Phạm vi địa lý Bảo Việt Nhân thọ chi trả các quyền lợi bảo hiểm của Sản phẩm bổ trợ này khi Chi phí y tế thực tế phát sinh trong phạm vi lãnh thổ Việt N… |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | - Các bằng chứng hoặc các giấy tờ bổ sung cần thiết khác (nếu có) theo yêu cầu của Bảo Việt Nhân thọ để phục vụ cho việc giải quyết quyền lợi bảo hiểm. - Trường… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 3 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `manulife-cssknc-2026` · 13 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.2. Thời hạn nộp đơn yêu cầu giải quyết quyền lợi bảo hiểm Thời hạn nộp hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm theo quy định tại Điều 6.3 là 01 (một) năm … |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 3 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 5 |  | `bvl-avsk-2022` · 4,5,6 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG | Điều 1: Định nghĩa và giải thích - 1.1. "Người được bảo hiểm" theo Sản phẩm bổ trợ này là cá nhân hiện đang cư trú tại Việt Nam vào Ngày hiệu lực của Sản phẩm b… |

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

**Câu hỏi:** Nếu không có yêu cầu bồi thường trong 3 năm liên tục thì An Vui Sống Khỏe giảm phí bao nhiêu?

**Đáp án chuẩn:** Giảm 15% phí bảo hiểm của quyền lợi tương ứng cho một năm tái tục tiếp theo (1 năm: 5%, 2 năm: 10%). Chỉ áp dụng tỷ lệ cao nhất, không cộng dồn (Điều 7).

- **E1**: `bvl-avsk-2022` · Điều 7 · tr.16 · cần chứa: '03 năm tham gia liên tục'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |
| 5 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG IV: PHÍ BẢO HIỂM | Điều 19: Gia hạn đóng phí bảo hiểm - 19.1. Trường hợp Bên mua bảo hiểm không đóng phí bảo hiểm theo đúng thời hạn đã thoả thuận, Phí bảo hiểm đến hạn của Sản ph… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |
| 5 |  | `bvl-avsk-2022` · 21 | An Vui Sống Khỏe › CHƯƠNG IV: PHÍ BẢO HIỂM | Điều 18: Phí bảo hiểm - 18.1. Trường hợp Sản phẩm chính đóng phí bảo hiểm định kỳ, Sản phẩm bổ trợ sẽ có định kỳ và ngày đến hạn đóng phí bảo hiểm trùng với Sản… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

<details><summary>rewrite+hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

## G15 · exclusion

**Câu hỏi:** An Vui Sống Khỏe có chi trả điều trị đông y, châm cứu không?

**Đáp án chuẩn:** Không. Các phương pháp điều trị không phải Tây y (y học dân tộc, y học cổ truyền, châm cứu, điều trị tại khoa Đông y/Y học cổ truyền/Châm cứu) bị loại trừ theo Điều 10.18.

- **E1**: `bvl-avsk-2022` · Điều 10.18 · tr.18 · cần chứa: 'y học cổ truyền, châm cứu'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 2 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 3 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao gồm cả Điều… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 4 |  | `bvl-avsk-2022` · 11,12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 5: Phạm vi địa lý Bảo Việt Nhân thọ chi trả các quyền lợi bảo hiểm của Sản phẩm bổ trợ này khi Chi phí y tế thực tế phát sinh trong phạm vi lãnh thổ Việt N… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | 1.16. "Điều trị Nha khoa": Điều trị Nha khoa được chi trả theo Sản phẩm bổ trợ này bao gồm: - (i) Điều trị Nha khoa do bệnh lý (thuộc Quyền lợi Điều trị Nha kho… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | 1.16. "Điều trị Nha khoa": Điều trị Nha khoa được chi trả theo Sản phẩm bổ trợ này bao gồm: - (i) Điều trị Nha khoa do bệnh lý (thuộc Quyền lợi Điều trị Nha kho… |

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

**Câu hỏi:** So sánh thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia, An Vui Sống Khỏe và Manulife Chăm Sóc Sức Khỏe Nâng Cao.

**Đáp án chuẩn:** Bảo Việt An Gia: sinh nở sau 635 ngày, biến chứng thai sản sau 90 ngày. An Vui Sống Khỏe (Bảo Việt Nhân thọ): 270 ngày. Manulife: 270 ngày.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5 · tr.15 · cần chứa: '635 ngày'
- **E2**: `bvl-avsk-2022` · Điều 8.1 · tr.16 · cần chứa: 'Quyền lợi Thai sản: 270 ngày'
- **E3**: `manulife-cssknc-2026` · Điều 2. Thời gian chờ · tr.10 · cần chứa: '270 ngày Thai sản'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 6, E2: 4, E3: — | 0.33 |
| hybrid3 | E1: —, E2: 3, E3: — | 0.33 |
| hybrid3+rerank | E1: 2, E2: 3, E3: 4 | 1.00 |
| hybrid3+rerank+filter | E1: 2, E2: 3, E3: 4 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 2, E2: 3, E3: 4 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |
| 4 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 3 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 5 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 3 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 | ✅ E3 | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 5 |  | `bv-angia-2016` · 5 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 12. Thời hạn bảo hiểm Thời hạn bảo hiểm được quy định cụ thể trong Hợp đồng bảo hiểm hoặc Giấy chứng nhận bảo hiểm. Thời hạn bảo hiểm là một (01) năm, không chấ… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 3 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 | ✅ E3 | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 5 |  | `bv-angia-2016` · 5 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 12. Thời hạn bảo hiểm Thời hạn bảo hiểm được quy định cụ thể trong Hợp đồng bảo hiểm hoặc Giấy chứng nhận bảo hiểm. Thời hạn bảo hiểm là một (01) năm, không chấ… |

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

**Câu hỏi:** Giới hạn quyền lợi thai sản của gói Kim Cương trong Bảo Việt An Gia khác gì so với gói Kim Cương của Manulife?

**Đáp án chuẩn:** An Gia Kim Cương: tối đa 31.500.000 đồng cho một thời hạn bảo hiểm (phí bảo hiểm thai sản 5.500.000 đồng/người/năm). Manulife Kim Cương: tối đa 70 triệu đồng cho mỗi lần mang thai (gồm sinh thường, sinh mổ, biến chứng thai sản), đồng chi trả 20%.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5: Bảo hiểm thai sản · tr.15 · cần chứa: '31.500.000'
- **E2**: `manulife-cssknc-2026` · Điều 1.4 Quyền lợi thai sản · tr.9 · cần chứa: 'Giới hạn tối đa cho mỗi lần mang thai', '70 triệu'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: —, E2: 9 | 0.00 |
| hybrid3 | E1: 4, E2: — | 0.50 |
| hybrid3+rerank | E1: 2, E2: 9 | 0.50 |
| hybrid3+rerank+filter | E1: 1, E2: 5 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1, E2: 5 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 5 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 3 |  | `bvl-avsk-2022` · 12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Chi phí Điều trị Nội trú (giới hạn cho mỗi Đợt điều trị, không bao gồm Thai sản) — Bạc: 60.000.000 đồng/đợt; Vàng: 10… |
| 4 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | Bảng (BẠCH KIM, KIM CƯƠNG) - Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — BẠCH KIM: 21.000.000; KIM CƯƠNG: 31.500.000 - Phí bảo hiểm/ người/năm — BẠC… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | Bảng (BẠCH KIM, KIM CƯƠNG) - Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — BẠCH KIM: 21.000.000; KIM CƯƠNG: 31.500.000 - Phí bảo hiểm/ người/năm — BẠC… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | Bảng (BẠCH KIM, KIM CƯƠNG) - Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — BẠCH KIM: 21.000.000; KIM CƯƠNG: 31.500.000 - Phí bảo hiểm/ người/năm — BẠC… |
| 2 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia | ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chư… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |
| 4 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 5 | ✅ E2 | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản (là tổng quyền lợi bảo hiểm… |

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

**Câu hỏi:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) của Dai-ichi Life hiện được ban hành theo văn bản nào?

**Đáp án chuẩn:** Sản phẩm được Bộ Tài chính phê chuẩn theo công văn 14187/BTC-QLBH ngày 09/10/2015 (và công văn 8361/BTC-QLBH ngày 23/06/2017, 623/BTC-QLBH ngày 16/01/2020). Quy tắc và Điều khoản hiện hành được sửa đổi và ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025.

- **E1**: `daiichi-tktt2015-2025` · Trang bìa Quy tắc và Điều khoản · tr.4 · cần chứa: '424/GD/Dai-ichi/2025'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| dense | E1: 1 | 1.00 |
| hybrid3 | E1: 1 | 1.00 |
| hybrid3+rerank | E1: 1 | 1.00 |
| hybrid3+rerank+filter | E1: 1 | 1.00 |
| rewrite+hybrid3+rerank+filter | E1: 1 | 1.00 |

<details><summary>dense: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.6. Chấp nhận bảo hiểm có điều kiện - a. Trường hợp Bên mua bảo hiểm và/hoặc Người được bảo hiểm vi phạm nghĩa vụ cung cấp đối với bất kỳ thông tin nào về sức … |
| 5 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.1. Nghĩa vụ cung cấp thông tin của Bên mua bảo hiểm, Người được bảo hiểm - a. Bên mua bảo hiểm và Người được bảo hiểm có nghĩa vụ cung cấp đầy đủ và chính xác… |

</details>

<details><summary>hybrid3: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | Hoặc - e. Các trường hợp/điều kiện cụ thể khác (nếu có) theo quy định của Dai-ichi Life Việt Nam tại từng thời điểm. - 1.6. Hồ sơ yêu cầu bảo hiểm: là toàn bộ t… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | - (iii) Các điều kiện bảo hiểm khác theo quy định của Dai-ichi Life Việt Nam và quy định pháp luật tại từng thời điểm. - b. Dai-ichi Life Việt Nam sẽ gửi thông … |
| 5 |  | `daiichi-tktt2015-2025` · 15 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 9.3. Trong thời gian Hợp đồng bảo hiểm có hiệu lực và Người được bảo hiểm còn sống, nếu Người được bảo hiểm hoặc đại diện theo pháp luật của Người được bảo hi… |

</details>

<details><summary>hybrid3+rerank: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - b. được thể hiện dưới dạng bằng văn bản giấy hoặc giao dịch/dữ liệu điện tử theo quy định của pháp luật về giao dịch điện tử. - 1.8. Hợp đồng tiết kiệm tích l… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | - (iii) Các điều kiện bảo hiểm khác theo quy định của Dai-ichi Life Việt Nam và quy định pháp luật tại từng thời điểm. - b. Dai-ichi Life Việt Nam sẽ gửi thông … |
| 5 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |

</details>

<details><summary>hybrid3+rerank+filter: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - b. được thể hiện dưới dạng bằng văn bản giấy hoặc giao dịch/dữ liệu điện tử theo quy định của pháp luật về giao dịch điện tử. - 1.8. Hợp đồng tiết kiệm tích l… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | - (iii) Các điều kiện bảo hiểm khác theo quy định của Dai-ichi Life Việt Nam và quy định pháp luật tại từng thời điểm. - b. Dai-ichi Life Việt Nam sẽ gửi thông … |
| 5 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |

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

