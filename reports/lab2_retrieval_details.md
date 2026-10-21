# Lab 2 – Kết quả truy xuất từng câu golden (BGE-M3 dense, toàn corpus)

Sinh tự động. ✅ = chunk chứa đủ đoạn trích của bằng chứng (E1, E2… theo thứ tự trong golden set). Hiển thị top-5; hạng của bằng chứng tính đến top-10 (`—` = ngoài top-10).

## G01 · table_lookup

**Câu hỏi:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là bao nhiêu một năm?

**Đáp án chuẩn:** 1.887.600 đồng/người/năm (biểu phí An Gia, điều khoản chính, nhóm tuổi từ 31 đến 40).

- **E1**: `bv-angia-2016` · Biểu phí bảo hiểm - A. Điều khoản bảo hiểm chính · tr.26 · cần chứa: 'Từ 31 đến 40 tuổi', '1.887.600'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: — | 0.00 |
| recursive | E1: — | 0.00 |
| structure_nobc | E1: — | 0.00 |
| structure | E1: 2 | 1.00 |
| structure+ctx | E1: 2 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 24-25 |  | ẢO HIỂM \| ĐỒNG \| BẠC \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\|---\|---\|---\| \| A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn \| A. ĐIỀU K… |
| 2 |  | `bv-angia-2016` · 24-25,26 |  | Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| \| 4. Bảo hiểm Nha khoa Khám và chẩn đoán bệnh về răng Lấy cao răng Trám răng bằng các chất liệu thông t… |
| 3 |  | `bv-taman-2019` · 21,22 |  | \| 3.760.000 \| \| Từ 31 đến 40 tuổi \| 1.365.600 \| 2.960.000 \| 4.111.000 \| \| Từ 41 đến 50 tuổi \| 1.425.400 \| 3.090.000 \| 4.286.500 \| \| Từ 51 đến 60 tuổi \| 1.485.20… |
| 4 |  | `bv-taman-2019` · 20,21 |  | ột quỵ) 5. Suy tim mất bù (bệnh tim giai đoạn cuối) 6. Phẫu thuật động mạch chủ/van tim 7. Bệnh Parkinson/Alzheimer 8. Phẫu thuật sọ não do bệnh của não bộ 9. H… |
| 5 |  | `bv-angia-2016` · 24-25 |  | /vụ \| 500.000/vụ \| 500.000/vụ \| \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ S… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 |  | \| CHƯƠNG TRÌNH BẢO HIỂM \| CHƯƠNG TRÌNH BẢO HIỂM \| ĐỒNG \| BẠC \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\|---\|---\|---\|---\| \| A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều… |
| 2 |  | `bv-angia-2016` · 24-25 |  | \| CHƯƠNG TRÌNH BẢO HIỂM \| ĐỒNG \| BẠC \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\|---\|---\|---\| \| A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai… |
| 3 |  | `bvl-avsk-2022` · 12 |  | \| Chương trình \| Bạc \| Vàng \| Bạch Kim \| Kim Cương \| \|---\|---\|---\|---\|---\| \| Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Nội trú \| 150.000.000 đồng/năm \| 25… |
| 4 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |
| 5 |  | `manulife-cssknc-2026` · 6 |  | \| Chương trình bảo hiểm \| BẠC \| TITAN \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\|---\|---\|---\| \| 2. Chi phí Phòng và Giường tại Khoa Chăm Sóc Đặc Biệt hoặc Giư… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 3 |  | `bvl-avsk-2022` · 12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Nội trú — Bạc: 150.000.000 đồng/năm; Vàng: 250.000.000 đồng/năm; Bạch Ki… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 1. Điều trị ngoại trú do ốm bệnh, tai nạn — ĐỒNG: 6.000.000/NĂM; BẠC: 6.000.000/năm; VÀNG: 6.000.000/năm; BẠCH KIM… |
| 5 |  | `bvl-avsk-2022` · 12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Chi phí Điều trị Nội trú (giới hạn cho mỗi Đợt điều trị, không bao gồm Thai sản) — Bạc: 60.000.000 đồng/đợt; Vàng: 10… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 2 | ✅ E1 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. Chi phí khám và điều trị trong vòng 30 ngày trước khi nhập viện — ĐỒNG: 2.000.000/năm; BẠC: 3.000.000/năm; VÀNG… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

## G02 · table_lookup

**Câu hỏi:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là bao nhiêu?

**Đáp án chuẩn:** 230.000.000 đồng/người/năm. Lưu ý bảng quyền lợi gốc in là "230.00 0.000/ng/năm".

- **E1**: `bv-angia-2016` · Bảng quyền lợi bảo hiểm - A. Điều khoản bảo hiểm chính · tr.24-25 · cần chứa: 'Tổng hạn mức quyền lợi bảo hiểm chính', '230.00 0.000'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 8 | 0.00 |
| recursive | E1: 2 | 1.00 |
| structure_nobc | E1: 1 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21,22 |  | \| 3.760.000 \| \| Từ 31 đến 40 tuổi \| 1.365.600 \| 2.960.000 \| 4.111.000 \| \| Từ 41 đến 50 tuổi \| 1.425.400 \| 3.090.000 \| 4.286.500 \| \| Từ 51 đến 60 tuổi \| 1.485.20… |
| 2 |  | `bv-angia-2016` · 24-25,26 |  | Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| \| 4. Bảo hiểm Nha khoa Khám và chẩn đoán bệnh về răng Lấy cao răng Trám răng bằng các chất liệu thông t… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 4 |  | `bv-angia-2016` · 26,27,28 |  | 0,2% STBH \| 0,2% STBH \| 0,2% STBH \| \| Từ 1 đến \| Từ 1 đến \| 600.000 \| 600.000 \| 1.500.000 \| 2.600.000 \| 3.900.000 \| \| 4. Bảo hiểm Nha khoa \| 18 tuổi Từ 19 đến 6… |
| 5 |  | `bv-taman-2019` · 20,21 |  | ột quỵ) 5. Suy tim mất bù (bệnh tim giai đoạn cuối) 6. Phẫu thuật động mạch chủ/van tim 7. Bệnh Parkinson/Alzheimer 8. Phẫu thuật sọ não do bệnh của não bộ 9. H… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 22 |  | \| QUYỀN LỢI BẢO HIỂM \| PHÚC \| LỘC \| THỌ \| \|---\|---\|---\|---\| \| Tổng hạn mức quyền lợi bảo hiểm /người/năm \| 193.800.000 \| 430.000.000 \| 842.000.000 \| \| Phạm vi l… |
| 2 | ✅ E1 | `bv-angia-2016` · 24-25 |  | \| CHƯƠNG TRÌNH BẢO HIỂM \| ĐỒNG \| BẠC \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\|---\|---\|---\| \| A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai… |
| 3 |  | `manulife-cssknc-2026` · 1,2 |  | ## Mức Đồng Chi Trả: 20% (áp dụng cho Người Được Bảo Hiểm tại mọi độ tuổi) Đơn vị: Việt Nam đồng \| Chương trình bảo hiểm \| TITAN \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \|… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 5 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 3 |  | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 1.1. Lựa chọn Chương trình bảo hiểm Bảo Việt nhân thọ cung cấp 04 chương trình bảo hiểm Bạc, Vàng, Bạch kim và Kim cương tương ứng với các mức Số tiền bảo hiểm … |
| 5 |  | `bvl-avsk-2022` · 12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Nội trú — Bạc: 150.000.000 đồng/năm; Vàng: 250.000.000 đồng/năm; Bạch Ki… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 41 đến 50 tuổi — ĐỒNG: 1.375.400; BẠC: 1.973.400; VÀNG: 2.990.000; BẠCH KIM: 4.036.500; KIM CƯƠNG: 4.933.500 - … |
| 4 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 2.585.000; BẠC: 3.707.000; VÀNG: 5.616.000; BẠCH KIM: 7.582.000; KIM CƯƠNG: 9.267.000 - Từ… |

</details>

## G03 · table_lookup

**Câu hỏi:** Với quyền lợi thai sản của Manulife Chăm Sóc Sức Khỏe Nâng Cao, chi phí sinh được chi trả như thế nào?

**Đáp án chuẩn:** Chi phí sinh được chi trả theo Chi Phí Y Tế Thực Tế, nằm trong giới hạn tối đa cho mỗi lần mang thai (Titan 12 triệu, Vàng 25 triệu, Bạch Kim 35 triệu, Kim Cương 70 triệu), áp dụng mức đồng chi trả 20%; chỉ chi trả cho người được bảo hiểm từ đủ 18 đến 45 tuổi.

- **E1**: `manulife-cssknc-2026` · Điều 1.4 Quyền lợi thai sản · tr.9 · cần chứa: 'E. Chi phí sinh', 'Giới hạn tối đa cho mỗi lần mang thai'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 10 | 0.00 |
| recursive | E1: — | 0.00 |
| structure_nobc | E1: — | 0.00 |
| structure | E1: — | 0.00 |
| structure+ctx | E1: — | 0.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 9,10 |  | Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản. - Các chi phí y tế liên quan đến thai sản (bao gồm việ… |
| 2 |  | `manulife-cssknc-2026` · 24,25 |  | thường, xét nghiệm máu cơ bản, chi phí chích ngừa, siêu âm thai theo chỉ định của Bác Sĩ. Manulife không chi trả cho các chi phí xét nghiệm tầm soát trước khi s… |
| 3 |  | `manulife-cssknc-2026` · 11,12 |  | - Quyền lợi thai sản; và các trường hợp loại trừ khác được quy định trong các định nghĩa Bệnh Viện, Cấy Ghép Nội Tạng, Chi Phí Phẫu Thuật, Cơ Sở Y Tế, Điều Trị … |
| 4 |  | `manulife-cssknc-2026` · 4,5 |  | kể từ thời điểm thay đổi, trừ trường hợp có thỏa thuận khác giữa Bên Mua Bảo Hiểm và Manulife. ## Minh họa về việc bổ sung thêm quyền lợi bảo hiểm Chị H. đang t… |
| 5 |  | `manulife-cssknc-2026` · 4 |  | Quyền lợi Điều Trị Nội Trú \| 1.1 Quyền lợi Điều Trị Nội Trú \| 1.1 Quyền lợi Điều Trị Nội Trú \| 1.1 Quyền lợi Điều Trị Nội Trú \| \| Quyền lợi lựa chọn thêm \| Khôn… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 9,10 |  | ## Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai s… |
| 2 |  | `manulife-cssknc-2026` · 24 |  | \| 36. Kiểm Tra Thai Định Kỳ \| Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu thông thường, xét … |
| 3 |  | `manulife-cssknc-2026` · 1,2 |  | Chương trình bảo hiểm Bên Mua Bảo Hiểm lựa chọn được thể hiện trên Trang Hợp Đồng (Giấy Chứng Nhận Bảo Hiểm) hoặc Xác Nhận Thay Đổi Hợp Đồng, nếu có. Trong trườ… |
| 4 |  | `bvl-avsk-2022` · 1 |  | \| Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản \| Không áp dụng \| 15.000.000 đồng/năm \| 30.000.000 đồng/năm \| 50.000.000 đồng/năm \| \| Giới hạn phụ trong Phần … |
| 5 |  | `manulife-cssknc-2026` · 22 |  | \| 16. Chi Phí Tái Tạo Tuyến Vú Sau Đoạn Nhũ Do Ung Thư \| nhưng do cơ thể không đào thải nên không cần thiết lấy ra. Là các Chi Phí Y Tế Thực Tế cần thiết phát s… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 16. Chi Phí Tái Tạo Tuyến Vú Sau Đoạn Nhũ Do Ung Thư — col1: nhưng do cơ thể không đào thải nên không cần thiết lấy ra. Là các Chi Phí Y Tế Thực T… |
| 4 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 32. Đồng Chi Trả — col1: Là việc Bên Mua Bảo Hiểm và Manulife cùng chi trả cho Chi Phí Y Tế Thực Tế phát sinh. Mức Đồng Chi Trả là tỷ lệ phần trăm… |
| 5 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 13 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.1. Người nhận quyền lợi bảo hiểm Trừ trường hợp có thỏa thuận khác giữa Manulife và Bên Mua Bảo Hiểm, các quyền lợi bảo hiểm nêu tại Sản Phẩm Bảo Hiểm này sẽ … |
| 4 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | (*) Mức Đồng Chi Trả: Mức Đồng Chi Trả được ghi nhận tại thời điểm phát hành hợp đồng sẽ áp dụng xuyên suốt thời hạn hợp đồng (bao gồm thời gian tái tục). Trong… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 2 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 3 |  | `manulife-cssknc-2026` · 13 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.1. Người nhận quyền lợi bảo hiểm Trừ trường hợp có thỏa thuận khác giữa Manulife và Bên Mua Bảo Hiểm, các quyền lợi bảo hiểm nêu tại Sản Phẩm Bảo Hiểm này sẽ … |
| 4 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | (*) Mức Đồng Chi Trả: Mức Đồng Chi Trả được ghi nhận tại thời điểm phát hành hợp đồng sẽ áp dụng xuyên suốt thời hạn hợp đồng (bao gồm thời gian tái tục). Trong… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |

</details>

## G04 · multi_condition

**Câu hỏi:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho ai và sau bao lâu thì được chi trả chi phí sinh nở?

**Đáp án chuẩn:** Người được bảo hiểm từ 18 đến 45 tuổi, phải tham gia điều khoản chính tương đương chương trình Bạch Kim hoặc Kim Cương. Chi phí sinh nở chỉ được chi trả sau 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản sau 90 ngày. Giới hạn tối đa 21.000.000 (Bạch Kim) / 31.500.000 (Kim Cương) cho một thời hạn bảo hiểm.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5: Bảo hiểm thai sản · tr.15 · cần chứa: '635 ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 1 | 1.00 |
| recursive | E1: 1 | 1.00 |
| structure_nobc | E1: 1 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15,16 |  | a sinh non - Sinh khó - Biến chứng của các nguyên nhân trên. ## b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao … |
| 2 |  | `bv-angia-2016` · 15 |  | Ông Ích Khiêm, Thanh Khê, Đà Nẵng. ## ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham… |
| 3 |  | `bvl-avsk-2022` · 14 |  | ---\|---\|---\| \| Quyền lợi Thai sản chỉ áp dụng với Người được bảo hiểm là nữ trong độ tuổi từ 18 đến 45 tại thời điểm sinh con hoặc xảy ra Biến chứng thai sản. \|… |
| 4 |  | `bv-angia-2016` · 13,14 |  | chứng thai sản như định nghĩa kể từ ngày tham gia bảo hiểm. - 01 năm đối với bệnh có sẵn và các bệnh được liệt kê tại Điểm loại trừ chung số 36 của Quy tắc bảo … |
| 5 |  | `bv-angia-2016` · 14,15 |  | 90) ngày kể từ ngày đóng phí bảo hiểm đối với bệnh thông thường. Các hợp đồng bảo hiểm tái tục liên tục mặc nhiên có hiệu lực ngay sau khi Người tham gia bảo hi… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 |  | \| THAI SẢN \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\| \| Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm \| 21.000.000 \| 31.500.000 \| \| Phí bảo hiểm/ người/năm … |
| 2 | ✅ E1 | `bv-angia-2016` · 1,2,3 |  | ## 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến … |
| 3 |  | `manulife-cssknc-2026` · 9,10 |  | ## Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai s… |
| 4 |  | `bv-taman-2019` · 10 |  | ## 44. Biến chứng thai sản Là tình trạng bất thường của bào thai, biến chứng do nguyên nhân tai nạn hoặc bệnh lý phát sinh trong quá trình mang thai của Người đ… |
| 5 |  | `bvl-avsk-2022` · 1 |  | \| Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản \| Không áp dụng \| 15.000.000 đồng/năm \| 30.000.000 đồng/năm \| 50.000.000 đồng/năm \| \| Giới hạn phụ trong Phần … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |
| 3 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.31. "Chi phí xe cứu thương" là chi phí vận chuyển cấp cứu bằng xe cứu thương và chăm sóc trong quá trình vận chuyển Người được bảo hiểm đang trong tình trạn… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 5 |  | `bv-angia-2016` · 13 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham gia Điều khoản bổ sung này các chi phí y tế phát sinh điều trị ngoại trú do ố… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | a. Biến chứng thai sản và sinh khó Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sin… |
| 4 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | b. Sinh thường Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợ… |
| 5 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |

</details>

## G05 · fact

**Câu hỏi:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ nào?

**Đáp án chuẩn:** Áp dụng đồng chi trả 70/30: Bảo Việt chi trả 70%, người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (trừ khoa điều trị tự nguyện/theo yêu cầu của bệnh viện công lập).

- **E1**: `bv-angia-2016` · Bảng quyền lợi - Quy định đồng chi trả đối với trẻ em · tr.24-25 · cần chứa: '70/30'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 2 | 1.00 |
| recursive | E1: 1 | 1.00 |
| structure_nobc | E1: 1 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26,27,28 |  | 0,2% STBH \| 0,2% STBH \| 0,2% STBH \| \| Từ 1 đến \| Từ 1 đến \| 600.000 \| 600.000 \| 1.500.000 \| 2.600.000 \| 3.900.000 \| \| 4. Bảo hiểm Nha khoa \| 18 tuổi Từ 19 đến 6… |
| 2 | ✅ E1 | `bv-angia-2016` · 24-25,26 |  | Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| \| 4. Bảo hiểm Nha khoa Khám và chẩn đoán bệnh về răng Lấy cao răng Trám răng bằng các chất liệu thông t… |
| 3 |  | `bv-angia-2016` · 9,10 |  | định của bác sỹ trong cùng một cơ sở y tế, trong một ngày thì vẫn chỉ tính là một lần khám/điều trị. ## 50. Đồng chi trả Đồng chi trả là số tiền theo tỷ lệ mà C… |
| 4 |  | `bv-angia-2016` · 10 |  | /mẹ như đã đề cập ở trên - Chỉ được tham gia chương trình Bạch kim/Kim cương - Phí bảo hiểm bằng 150% phí của độ tuổi 1-3 theo chương trình tham gia tương ứng #… |
| 5 |  | `bv-taman-2019` · 10,11 |  | trong Bảng Quyền lợi bảo hiểm đính kèm. 4. Người được bảo hiểm từ 15 ngày tuổi đến dưới 1 tuổi chỉ được tham gia với điều kiện: Cung cấp Giấy Yêu cầu bảo hiểm t… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25,26 |  | ## QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 2 |  | `bv-taman-2019` · 22,23 |  | ## QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%… |
| 3 |  | `bv-angia-2016` · 10 |  | 2. Trường hợp trẻ em dưới mười tám (18) tuổi chỉ được nhận bảo hiểm với điều kiện phải tham gia bảo hiểm cùng hợp đồng với Bố và/hoặc Mẹ hoặc Bố/Mẹ đã tham gia … |
| 4 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |
| 5 |  | `bv-taman-2019` · 10,11 |  | Trường hợp Người được bảo hiểm trên sáu mươi (60) tuổi đến sáu mươi ba (63) tuổi tại thời điểm bắt đầu hiệu lực của Hợp đồng bảo hiểm thì chỉ được phép tham gia… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `manulife-cssknc-2026` · 5 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Mức Đồng Chi Trả: Người Được Bảo Hiểm trong độ tuổi từ 30 (ba mươi) ngày Tuổi đến 4 (bốn) Tuổi: 20%. Người Được Bảo Hiểm trong độ tuổi từ 5 (năm) Tuổi trở lên: … |
| 4 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 5 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › I. ĐỊNH NGHĨA | 3. Người yêu cầu bảo hiểm Là người đại diện như bố/mẹ cho những người phụ thuộc là con dưới 18 tuổi hoặc vợ/chồng, con của người được bảo hiểm trên 18 tuổi đứng… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) - Qu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG › 1. Điều trị ngoại trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Từ 1 đến 3 tuổi — ĐỒNG: 3.370.000; BẠC: 3.370.000; VÀNG: 3.370.000; BẠCH KIM: 5.516.000; KIM CƯƠNG: 8.424.000 - Từ… |

</details>

## G06 · fact

**Câu hỏi:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là bao lâu?

**Đáp án chuẩn:** 01 năm đối với bệnh có sẵn (và các bệnh tại điểm loại trừ chung số 36), 01 năm đối với bệnh đặc biệt. Ngoài ra: ốm đau bệnh tật 30 ngày, biến chứng thai sản 90 ngày, trẻ em đến 6 tuổi bị viêm phế quản/tiểu phế quản/viêm phổi 06 tháng.

- **E1** (nhóm thay thế `a`): `bv-angia-2016` · Phần II - 2. Hiệu lực bảo hiểm · tr.13 · cần chứa: '01 năm đối với bệnh có sẵn', '01 năm đối với bệnh đặc biệt'
- **E2** (nhóm thay thế `a`): `bv-angia-2016` · Điều khoản bổ sung 1 - 2. Hiệu lực bảo hiểm · tr.14 · cần chứa: '01 năm đối với bệnh có sẵn', '01 năm đối với bệnh đặc biệt'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 2, E2: 2 | 1.00 |
| recursive | E1: 1, E2: 1 | 1.00 |
| structure_nobc | E1: 3, E2: 3 | 1.00 |
| structure | E1: 1, E2: 1 | 1.00 |
| structure+ctx | E1: 1, E2: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 10,11 |  | . - 1.39. "Thời gian chờ" là khoảng thời gian mà nếu xảy ra các sự kiện bảo hiểm trong thời gian đó thì Bảo Việt Nhân thọ sẽ không chi trả quyền lợi bảo hiểm. T… |
| 2 | ✅ E1,E2 | `bv-angia-2016` · 13,14 |  | cùng với Quy tắc và là một bộ phận không thể tách rời Quy tắc bảo hiểm này. Các quyền lợi bổ sung này chỉ được áp dụng trong trường hợp được ghi rõ ràng là được… |
| 3 |  | `bv-angia-2016` · 14,15 |  | 90) ngày kể từ ngày đóng phí bảo hiểm đối với bệnh thông thường. Các hợp đồng bảo hiểm tái tục liên tục mặc nhiên có hiệu lực ngay sau khi Người tham gia bảo hi… |
| 4 | ✅ E1,E2 | `bv-angia-2016` · 13,14 |  | chứng thai sản như định nghĩa kể từ ngày tham gia bảo hiểm. - 01 năm đối với bệnh có sẵn và các bệnh được liệt kê tại Điểm loại trừ chung số 36 của Quy tắc bảo … |
| 5 |  | `bv-angia-2016` · 17,18 |  | tại đây và/hoặc các danh mục khác tương tự như vậy như các loại vitamin, thuốc bổ, khoáng chất và các chất hữu cơ thực phẩm chức năng), thuốc tăng cường miễn dị… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 1,2,3 |  | ## ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN ## 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham g… |
| 2 |  | `bv-taman-2019` · 12,13 |  | ## IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt … |
| 3 |  | `bvl-avsk-2022` · 1 |  | Tại mỗi lần xem xét, Bảo Việt Nhân thọ chỉ áp dụng tỷ lệ giảm phí theo tỷ lệ cao nhất được hưởng với từng Quyền lợi bảo hiểm, không áp dụng cộng dồn các tỷ lệ g… |
| 4 |  | `bv-angia-2016` · 18 |  | 34. Bệnh có sẵn như định nghĩa trong Quy tắc này chỉ được bảo hiểm từ năm thứ hai tham gia liên tục. 35. Bệnh đặc biệt như định nghĩa trong Quy tắc này chỉ được… |
| 5 |  | `bv-angia-2016` · 1,2,3 |  | 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự kiện bảo hiểm. 2. Bảo hiểm Bảo Việt có trách … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 2 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 3 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 4 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 5 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 3 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 4 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |
| 2 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 30. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 31. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 3 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 5 | ✅ E1,E2 | `bv-angia-2016` · 13 | Bảo Việt An Gia › PHẦN II: ĐIỀU KHOẢN BẢO HIỂM CHÍNH ĐIỀU TRỊ NỘI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |

</details>

## G07 · fact

**Câu hỏi:** Bảo Việt Tâm An nhận bảo hiểm cho người ở độ tuổi nào?

**Đáp án chuẩn:** Từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 đến 63 tuổi chỉ được tham gia mới nếu có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ.

- **E1**: `bv-taman-2019` · Phần I - II. Đối tượng tham gia bảo hiểm · tr.10 · cần chứa: 'sáu mươi ba (63) tuổi'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: — | 0.00 |
| recursive | E1: 1 | 1.00 |
| structure_nobc | E1: 1 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 21,22 |  | \| 3.760.000 \| \| Từ 31 đến 40 tuổi \| 1.365.600 \| 2.960.000 \| 4.111.000 \| \| Từ 41 đến 50 tuổi \| 1.425.400 \| 3.090.000 \| 4.286.500 \| \| Từ 51 đến 60 tuổi \| 1.485.20… |
| 2 |  | `bv-taman-2019` · 20,21 |  | ột quỵ) 5. Suy tim mất bù (bệnh tim giai đoạn cuối) 6. Phẫu thuật động mạch chủ/van tim 7. Bệnh Parkinson/Alzheimer 8. Phẫu thuật sọ não do bệnh của não bộ 9. H… |
| 3 |  | `bv-angia-2016` · 15 |  | Ông Ích Khiêm, Thanh Khê, Đà Nẵng. ## ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham… |
| 4 |  | `bv-angia-2016` · 3,4 |  | G TỶ LỆ TRẢ TIỀN THƯƠNG TẬT .............................................................................................20 \| \| BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆ… |
| 5 |  | `daiichi-tktt2015-2025` · 8,9 |  | độ tuổi từ 18 (mười tám) đến 75 (bảy mươi lăm) tuổi tính theo tuổi sinh nhật vừa qua tại thời điểm tham gia bảo hiểm. Tuổi tối đa của Người được bảo hiểm khi kế… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 10,11 |  | Trường hợp Người được bảo hiểm trên sáu mươi (60) tuổi đến sáu mươi ba (63) tuổi tại thời điểm bắt đầu hiệu lực của Hợp đồng bảo hiểm thì chỉ được phép tham gia… |
| 2 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |
| 3 |  | `bv-taman-2019` · 1,2,3,4 |  | Tiền bảo hiểm sẽ được chi trả cho Người được bảo hiểm hoặc Người thụ hưởng/Người được ủy quyền hợp pháp theo đúng quy định của Pháp luật. ## 4. Trường hợp bảo l… |
| 4 |  | `bvl-avsk-2022` · 3,4 |  | 1 Quy tắc, Điều khoản Sản phẩm bổ trợ này là Thỏa thuận bổ sung kèm theo Sản phẩm bảo hiểm chính (Hợp đồng chính) giữa Bên mua bảo hiểm và Bảo Việt Nhân thọ. ##… |
| 5 |  | `bv-angia-2016` · 1,2,3 |  | Là người đại diện như bố/mẹ cho những người phụ thuộc là con dưới 18 tuổi hoặc vợ/chồng, con của người được bảo hiểm trên 18 tuổi đứng ra yêu cầu và ký kết Hợp … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 2 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 3 |  | `manulife-cssknc-2026` · 5 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Mức Đồng Chi Trả: Người Được Bảo Hiểm trong độ tuổi từ 30 (ba mươi) ngày Tuổi đến 4 (bốn) Tuổi: 20%. Người Được Bảo Hiểm trong độ tuổi từ 5 (năm) Tuổi trở lên: … |
| 4 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |
| 5 |  | `bv-angia-2016` · 4 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | 6. Tuổi được bảo hiểm Là tuổi của Người được bảo hiểm vào ngày có hiệu lực của Hợp đồng bảo hiểm tính theo lần sinh nhật liền trước ngày Hợp đồng có hiệu lực. 7… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 10 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM | Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lă… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) -… |
| 3 |  | `bv-taman-2019` · 4 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 6. Tuổi được bảo hiểm Là tuổi thực tế của Người được bảo hiểm tính theo ngày sinh nhật liền trước ngày bắt đầu hiệu lực hợp đồng bảo hiểm (đối với trường hợp th… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-angia-2016` · 9,10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | II. ĐỐI TƯỢNG THAM GIA BẢO HIỂM Điều kiện được tham gia bảo hiểm theo quy tắc bảo hiểm này: 1. Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoà… |

</details>

## G08 · table_lookup

**Câu hỏi:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công bao nhiêu?

**Đáp án chuẩn:** 300.000 đồng/ngày, không quá 60 ngày/năm.

- **E1**: `bv-taman-2019` · Bảng quyền lợi bảo hiểm sức khỏe Bảo Việt Tâm An - mục 8 · tr.22 · cần chứa: 'Trợ cấp bệnh viện công', '300.000/ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 3 | 1.00 |
| recursive | E1: 4 | 1.00 |
| structure_nobc | E1: 2 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 20,21 |  | ột quỵ) 5. Suy tim mất bù (bệnh tim giai đoạn cuối) 6. Phẫu thuật động mạch chủ/van tim 7. Bệnh Parkinson/Alzheimer 8. Phẫu thuật sọ não do bệnh của não bộ 9. H… |
| 2 |  | `bv-taman-2019` · 21,22 |  | \| 3.760.000 \| \| Từ 31 đến 40 tuổi \| 1.365.600 \| 2.960.000 \| 4.111.000 \| \| Từ 41 đến 50 tuổi \| 1.425.400 \| 3.090.000 \| 4.286.500 \| \| Từ 51 đến 60 tuổi \| 1.485.20… |
| 3 | ✅ E1 | `bv-taman-2019` · 22,23 |  | trong vòng 30 ngày trước khi nhập viện \| 2.000.000/năm \| 5.000.000/năm \| 7.500.000/năm \| \| 4. Chi phí tái khám và điều trị trong vòng 30 ngày sau khi xuất viện … |
| 4 |  | `bv-angia-2016` · 24-25,26 |  | Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| \| 4. Bảo hiểm Nha khoa Khám và chẩn đoán bệnh về răng Lấy cao răng Trám răng bằng các chất liệu thông t… |
| 5 |  | `bv-angia-2016` · 24-25 |  | /ngày Lên đến 100.000.000/năm không quá 60 ngày/năm \| 7.500.000/ngày Lên đến 150.000.000/năm không quá 60 ngày/năm \| 10.000.000/ngày Lên đến 200.000.000/ năm kh… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 6 |  | \| Chương trình bảo hiểm \| BẠC \| TITAN \| VÀNG \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\|---\|---\|---\| \| 2. Chi phí Phòng và Giường tại Khoa Chăm Sóc Đặc Biệt hoặc Giư… |
| 2 |  | `bv-angia-2016` · 24-25 |  | \| 6. Phục hồi chức năng \| 4.000.000/năm \| 6.000.000/năm \| 10.000.000/năm \| 15.000.000/năm \| 20.000.000/năm \| \| 7. Trợ cấp bệnh viện công \| 80.000/ ngày Không qu… |
| 3 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |
| 4 | ✅ E1 | `bv-taman-2019` · 1,2,3 |  | \| 7. Phục hồi chức năng \| 4.000.000/năm \| 10.000.000/năm \| 15.000.000/năm \| \| 8. Trợ cấp bệnh viện công \| 120.000/ ngày Không quá 60 ngày/năm \| 300.000/ngày Khô… |
| 5 |  | `bv-taman-2019` · 22 |  | \| QUYỀN LỢI BẢO HIỂM \| PHÚC \| LỘC \| THỌ \| \|---\|---\|---\|---\| \| Tổng hạn mức quyền lợi bảo hiểm /người/năm \| 193.800.000 \| 430.000.000 \| 842.000.000 \| \| Phạm vi l… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 2 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 3 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 6. Phục hồi chức năng — ĐỒNG: 4.000.000/năm; BẠC: 6.000.000/năm; VÀNG: 10.000.000/năm; BẠCH KIM: 15.000.000/năm; K… |
| 4 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › A. ĐIỀU KHOẢN BẢO HIỂM CHÍNH - Điều trị nội trú do ốm bệnh, tai nạn | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 35. Trợ cấp cho Người được bảo hiểm Là khoản tiền trợ cấp cho Người được bảo hiểm trong trường hợp Người được bảo hiểm mắc 01 hoặc nhiều hơn 01 bệnh trong 22 bệ… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |
| 2 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Tổng hạn mức quyền lợi bảo hiểm /người/năm — PHÚC: 193.800.000; LỘC: 430.000.000; THỌ: 842.000.000 - Phạm vi lãnh thổ — PHÚC: Việt Nam; … |
| 3 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 33. Trợ cấp bệnh viện công Là khoản tiền trợ cấp trong trường hợp Người được bảo hiểm nằm viện điều trị nội trú do ốm bệnh, tai nạn, biến chứng thai sản tại các… |
| 4 |  | `bv-taman-2019` · 21 | Bảo Việt Tâm An › BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - Từ 15 ngày tuổi đến dưới 1 tuổi — PHÚC: Không áp dụng; LỘC: Không áp dụng; THỌ: 11.623.000 - Từ 1 đến 3 tuổi — PHÚC: 2.635.000; LỘC: 5.7… |
| 5 |  | `bv-taman-2019` · 8 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG › I. THUẬT NGỮ | 35. Trợ cấp cho Người được bảo hiểm Là khoản tiền trợ cấp cho Người được bảo hiểm trong trường hợp Người được bảo hiểm mắc 01 hoặc nhiều hơn 01 bệnh trong 22 bệ… |

</details>

## G09 · multi_condition

**Câu hỏi:** Hồ sơ yêu cầu bồi thường Bảo Việt Tâm An phải nộp trong thời hạn nào và Bảo hiểm Bảo Việt giải quyết trong bao lâu?

**Đáp án chuẩn:** Nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng của đợt điều trị (hoặc ngày tử vong) và không quá 01 năm kể từ ngày xảy ra sự kiện bảo hiểm (không tính thời gian bất khả kháng). Bảo hiểm Bảo Việt giải quyết và chi trả trong vòng 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ.

- **E1** (nhóm thay thế `a`): `bv-taman-2019` · Phần I - IX. Thời hạn khiếu nại và trả tiền bảo hiểm · tr.12 · cần chứa: 'sáu mươi (60) ngày kể từ ngày điều trị cuối cùng', 'mười lăm (15) ngày'
- **E2** (nhóm thay thế `a`): `bv-taman-2019` · Phần V - Thủ tục yêu cầu trả tiền bảo hiểm · tr.18 · cần chứa: 'sáu mươi (60) ngày kể từ ngày điều trị cuối cùng'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 4, E2: 1 | 1.00 |
| recursive | E1: 1, E2: 1 | 1.00 |
| structure_nobc | E1: 1, E2: 1 | 1.00 |
| structure | E1: 1, E2: 1 | 1.00 |
| structure+ctx | E1: 1, E2: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bv-taman-2019` · 17,18 |  | tại bất kỳ bệnh viện nào. 40. Tử vong do nguyên nhân khác nguyên nhân tai nạn như định nghĩa. 17 ## PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN P… |
| 2 |  | `bv-angia-2016` · 19 |  | VÀ BẢO LÃNH ## a. Trường hợp ứng tiền trước, bồi thường sau: Trường hợp Người được bảo hiểm khám và điều trị tại các cơ sở y tế hợp pháp không thuộc hệ thống bả… |
| 3 |  | `bv-angia-2016` · 11,12 |  | hiểm, Người được bảo hiểm hoặc Người thụ hưởng quyền lợi bảo hiểm không trung thực và/hoặc không tuân thủ đúng các quy định trong Quy tắc bảo hiểm này, Bảo hiểm… |
| 4 | ✅ E1,E2 | `bv-taman-2019` · 12,13 |  | bảo hiểm và mọi chi phí liên quan đến việc cung cấp hồ sơ không thuộc trách nhiệm của Bảo hiểm Bảo Việt. 3. Ủy quyền cho Bảo hiểm Bảo Việt thay mặt Người được b… |
| 5 |  | `bv-taman-2019` · 19,20 |  | Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ và hợp lệ,… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 |  | ## IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt … |
| 2 | ✅ E2 | `bv-taman-2019` · 17,18 |  | 38. Các chi phí và điều trị cho đối tượng không đủ điều kiện tham gia bảo hiểm. 39. Việc điều trị thử nghiệm, điều trị không được khoa học công nhận và các dịch… |
| 3 |  | `bv-angia-2016` · 19 |  | và sẽ thuộc sở hữu của Bảo hiểm Bảo Việt sau khi khiếu nại đã được giải quyết. Hóa đơn mua thuốc/điều trị phải được xuất trong vòng 30 ngày kể từ ngày kê đơn th… |
| 4 |  | `bv-angia-2016` · 1,2,3 |  | 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự kiện bảo hiểm. 2. Bảo hiểm Bảo Việt có trách … |
| 5 |  | `bv-angia-2016` · 1,2,3 |  | ## PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH ## 1. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo hiểm Bảo Việt trả tiền bảo hiểm, Người được bảo h… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 3 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 4 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |
| 5 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 3 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1,E2 | `bv-taman-2019` · 12,13 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điề… |
| 2 | ✅ E2 | `bv-taman-2019` · 18 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ | I. HỒ SƠ YÊU CẦU TRẢ TIỀN BẢO HIỂM Khi yêu cầu Bảo Hiểm Bảo Việt trả tiền bảo hiểm, hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu … |
| 3 |  | `bv-taman-2019` · 19 | Bảo Việt Tâm An › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH VIỆN PHÍ › II. THỦ TỤC TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | 2. Thời hạn bồi thường Bảo Hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày kể từ ngày nhận được hồ sơ … |
| 4 |  | `bv-angia-2016` · 19 | Bảo Việt An Gia › PHẦN V: THỦ TỤC YÊU CẦU TRẢ TIỀN BẢO HIỂM VÀ BẢO LÃNH | b. Thời hạn bồi thường Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong thời hạn tối đa 15 (mười lăm) ngày làm việc kể từ ngày nhận đư… |
| 5 |  | `bv-angia-2016` · 11,12 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | IX. THỜI HẠN KHIẾU NẠI VÀ TRẢ TIỀN BẢO HIỂM 1. Thời hạn yêu cầu trả tiền bảo hiểm hoặc bồi thường theo hợp đồng bảo hiểm là một năm (01), kể từ ngày xảy ra sự k… |

</details>

## G10 · fact

**Câu hỏi:** Nếu tôi tự yêu cầu hủy hợp đồng Bảo Việt Tâm An thì được hoàn lại bao nhiêu phí?

**Đáp án chuẩn:** Bảo hiểm Bảo Việt hoàn trả 80% phí bảo hiểm của thời gian còn lại, với điều kiện trong thời gian hiệu lực chưa có khiếu nại đòi trả tiền bảo hiểm nào. (Nếu Bảo hiểm Bảo Việt yêu cầu hủy thì hoàn toàn bộ phí của thời gian còn lại; trường hợp gian lận chỉ hoàn 70% nếu chưa có bồi thường.)

- **E1**: `bv-taman-2019` · Phần I - III. Ký kết/hủy bỏ hợp đồng bảo hiểm · tr.11 · cần chứa: 'hoàn trả 80% phí bảo hiểm'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 2 | 1.00 |
| recursive | E1: 1 | 1.00 |
| structure_nobc | E1: 5 | 1.00 |
| structure | E1: 2 | 1.00 |
| structure+ctx | E1: 2 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 22,23 |  | trong vòng 30 ngày trước khi nhập viện \| 2.000.000/năm \| 5.000.000/năm \| 7.500.000/năm \| \| 4. Chi phí tái khám và điều trị trong vòng 30 ngày sau khi xuất viện … |
| 2 | ✅ E1 | `bv-taman-2019` · 23,24,25 |  | được bảo hiểm trong Hợp đồng) theo yêu cầu của Bên mua bảo hiểm/Người được bảo hiểm, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại đối vớ… |
| 3 |  | `bv-taman-2019` · 11 |  | bảo hiểm có bất kỳ khiếu nại nào thể hiện gian lận hay không trung thực hoặc nếu có hành vi gian dối hoặc có mưu kế trục lợi bảo hiểm về bất kì phương diện nào … |
| 4 |  | `bv-angia-2016` · 10 |  | /mẹ như đã đề cập ở trên - Chỉ được tham gia chương trình Bạch kim/Kim cương - Phí bảo hiểm bằng 150% phí của độ tuổi 1-3 theo chương trình tham gia tương ứng #… |
| 5 | ✅ E1 | `bv-taman-2019` · 22,23 |  | tế/bệnh viện công lập (trừ các khoa điều trị tự nguyện/điều trị theo yêu cầu của Bệnh viện công lập) ## GIẤY YÊU CẦU SỬA ĐỔI BỔ SUNG BẢO VIỆT TÂM AN ## I. THÔNG… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bv-taman-2019` · 1,2,3,4 |  | - [ ] Sửa đổi khác (với điều kiện được Bảo Việt chấp thuận) ## IV. CAM KẾT CỦA NGƯỜI YÊU CẦU SỬA ĐỔI BỔ SUNG Tôi xác nhận hiểu và đồng ý với những điểm sau: 1. … |
| 2 |  | `bv-angia-2016` · 10 |  | 1. Khi có yêu cầu tham gia bảo hiểm, Người được bảo hiểm phải kê khai trung thực đầy đủ nội dung trên Giấy yêu cầu bảo hiểm. Giấy yêu cầu bảo hiểm là một bộ phậ… |
| 3 |  | `bv-taman-2019` · 22,23 |  | ## QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%… |
| 4 | ✅ E1 | `bv-taman-2019` · 11 |  | 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung thực đầy đủ nội dung trên Giấy yêu cầu bảo hiểm. Giấy yêu cầu bảo h… |
| 5 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Người được bảo hiểm phải kê khai trung thực đầy đủ nội du… |
| 4 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | - (ii) Chấp nhận bảo hiểm có điều kiện theo Điều 4.6 của Quy tắc và Điều khoản này. - d. Chi phí hợp lý được xác định bằng tổng chi phí hợp lý của tất cả Tháng … |
| 5 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 4 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | V. PHÍ BẢO HIỂM VÀ SỐ TIỀN BẢO HIỂM Phí bảo hiểm quy định trong Biểu phí đính kèm Quy tắc bảo hiểm này, phí bảo hiểm phụ thuộc vào chương trình bảo hiểm, độ tuổ… |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 2 | ✅ E1 | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | III. KÝ KẾT/HỦY BỎ HỢP ĐỒNG BẢO HIỂM VÀ TÁI TỤC HỢP ĐỒNG BẢO HIỂM 1. Khi có yêu cầu tham gia bảo hiểm, Bên mua bảo hiểm/Người được bảo hiểm phải kê khai trung t… |
| 3 |  | `bv-angia-2016` · 10 | Bảo Việt An Gia › PHẦN I: QUY ĐỊNH CHUNG | - Nếu Bảo hiểm Bảo Việt yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả toàn bộ phí bảo hiểm của thời gian còn lại cho dù có khiếu nại đòi trả tiền bảo h… |
| 4 |  | `bv-taman-2019` · 11 | Bảo Việt Tâm An › PHẦN I: QUY ĐỊNH CHUNG | V. PHÍ BẢO HIỂM VÀ SỐ TIỀN BẢO HIỂM Phí bảo hiểm quy định trong Biểu phí đính kèm Quy tắc bảo hiểm này, phí bảo hiểm phụ thuộc vào chương trình bảo hiểm, độ tuổ… |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

## G11 · fact

**Câu hỏi:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là bao lâu?

**Đáp án chuẩn:** 270 ngày (Điều 8.1). Các sự kiện do tai nạn không áp dụng thời gian chờ.

- **E1**: `bvl-avsk-2022` · Điều 8.1 · tr.16 · cần chứa: 'Quyền lợi Thai sản: 270 ngày'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 3 | 1.00 |
| recursive | E1: 10 | 0.00 |
| structure_nobc | E1: 8 | 0.00 |
| structure | E1: 5 | 1.00 |
| structure+ctx | E1: 3 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 9,10 |  | Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản. - Các chi phí y tế liên quan đến thai sản (bao gồm việ… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 | ✅ E1 | `bvl-avsk-2022` · 16,17 |  | ngày; - Quyền lợi Thai sản: 270 ngày; - Với các sự kiện bảo hiểm do Tai nạn: không áp dụng Thời gian chờ. 8.2. Tại mỗi thời điểm, Bảo Việt Nhân thọ chỉ chấp nhậ… |
| 4 |  | `bvl-avsk-2022` · 14 |  | ---\|---\|---\| \| Quyền lợi Thai sản chỉ áp dụng với Người được bảo hiểm là nữ trong độ tuổi từ 18 đến 45 tại thời điểm sinh con hoặc xảy ra Biến chứng thai sản. \|… |
| 5 |  | `bvl-avsk-2022` · 10,11 |  | . - 1.39. "Thời gian chờ" là khoảng thời gian mà nếu xảy ra các sự kiện bảo hiểm trong thời gian đó thì Bảo Việt Nhân thọ sẽ không chi trả quyền lợi bảo hiểm. T… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 9,10 |  | ## Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai s… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 |  | `bv-angia-2016` · 15 |  | \| THAI SẢN \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\| \| Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm \| 21.000.000 \| 31.500.000 \| \| Phí bảo hiểm/ người/năm … |
| 4 |  | `bvl-avsk-2022` · 14 |  | \| V. Quyền lợi Thai sản \| V. Quyền lợi Thai sản \| V. Quyền lợi Thai sản \| V. Quyền lợi Thai sản \| V. Quyền lợi Thai sản \| \|---\|---\|---\|---\|---\| \| Quyền lợi Thai… |
| 5 |  | `bv-angia-2016` · 1,2,3 |  | ## ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN ## 1. Quyền lợi bảo hiểm Bảo hiểm Bảo Việt sẽ thanh toán cho Người được bảo hiểm tham g… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › Điều 2. THỜI GIAN CHỜ | Thời gian chờ không áp dụng đối với trường hợp: - a. Điều trị do Tai Nạn; hoặc - b. Thay đổi sang chương trình bảo hiểm thấp hơn; hoặc - c. Tái tục Sản Phẩm Bảo… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 4 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 5 |  | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản.… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 5 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 15 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN | 2. Hiệu lực bảo hiểm: Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. Đối với biến chứ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 3 | ✅ E1 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 5 |  | `bv-angia-2016` · 13,14 | Bảo Việt An Gia › ĐIỀU KHOẢN BỔ SUNG 1: ĐIỀU TRỊ NGOẠI TRÚ DO ỐM ĐAU, BỆNH TẬT, TAI NẠN | 2. Hiệu lực bảo hiểm Bảo hiểm có hiệu lực sau thời gian chờ dưới đây kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm: - 30 ngày đối … |

</details>

## G12 · table_lookup

**Câu hỏi:** Trong An Vui Sống Khỏe, chương trình nào được mua thêm quyền lợi điều trị ngoại trú và hạn mức là bao nhiêu?

**Đáp án chuẩn:** Chương trình Bạc không áp dụng. Vàng 10 triệu đồng/năm, Bạch Kim 20 triệu đồng/năm, Kim Cương 40 triệu đồng/năm. Người được bảo hiểm tự chi trả 20% chi phí y tế thực tế; giới hạn 10 lần khám/năm.

- **E1** (nhóm thay thế `a`): `bvl-avsk-2022` · Điều 4 - Bảng giới hạn bảo hiểm tối đa · tr.11 · cần chứa: 'B. Quyền lợi Điều trị Ngoại trú'
- **E2** (nhóm thay thế `a`): `bvl-avsk-2022` · Điều 6.2 Quyền lợi Điều trị Ngoại trú · tr.14 · cần chứa: 'Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 2, E2: — | 1.00 |
| recursive | E1: —, E2: 5 | 1.00 |
| structure_nobc | E1: 5, E2: 7 | 1.00 |
| structure | E1: 2, E2: 1 | 1.00 |
| structure+ctx | E1: 1, E2: 2 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 2 | ✅ E1 | `bvl-avsk-2022` · 11,12 |  | ---\|---\|---\|---\|---\|---\| \| Quyền lợi bổ sung tùy chọn \| B. Quyền lợi Điều trị Ngoại trú \| Không áp dụng \| 10 triệu đồng/năm \| 20 triệu đồng/năm \| 40 triệu đồng/… |
| 3 |  | `manulife-cssknc-2026` · 4,5 |  | kể từ thời điểm thay đổi, trừ trường hợp có thỏa thuận khác giữa Bên Mua Bảo Hiểm và Manulife. ## Minh họa về việc bổ sung thêm quyền lợi bảo hiểm Chị H. đang t… |
| 4 |  | `bvl-avsk-2022` · 14,15 |  | ăm \| 20.000.000 đồng/năm \| 40.000.000 đồng/năm \| \| Đồng chi trả Quyền lợi Điều trị Ngoại trú \| Người được bảo hiểm tự chi trả: 20% Chi phí y tế thực tế. \| Người… |
| 5 |  | `manulife-cssknc-2026` · 4 |  | Quyền lợi Điều Trị Nội Trú \| 1.1 Quyền lợi Điều Trị Nội Trú \| 1.1 Quyền lợi Điều Trị Nội Trú \| 1.1 Quyền lợi Điều Trị Nội Trú \| \| Quyền lợi lựa chọn thêm \| Khôn… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 2 |  | `bvl-avsk-2022` · 12 |  | \| Chương trình \| Bạc \| Vàng \| Bạch Kim \| Kim Cương \| \|---\|---\|---\|---\|---\| \| Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Nội trú \| 150.000.000 đồng/năm \| 25… |
| 3 |  | `manulife-cssknc-2026` · 1,2 |  | Chương trình bảo hiểm Bên Mua Bảo Hiểm lựa chọn được thể hiện trên Trang Hợp Đồng (Giấy Chứng Nhận Bảo Hiểm) hoặc Xác Nhận Thay Đổi Hợp Đồng, nếu có. Trong trườ… |
| 4 |  | `bv-angia-2016` · 17 |  | 24. Các hình thức thẩm mỹ, phẫu thuật thẩm mỹ, chỉnh hình. 25. Các điều trị tăng sắc tố (nám da), điều trị mụn trứng cá, điều trị chứng rụng tóc bị loại trừ riê… |
| 5 | ✅ E2 | `bvl-avsk-2022` · 14 |  | \| 4. Chi phí Phòng và Giường Tối đa 30 ngày/năm cho tổng Quyền lợi Thai sản \| Không áp dụng \| 1.250.000 đồng/ngày \| 2.500.000 đồng/ngày \| 5.000.000 đồng/ngày \| … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 5 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 2 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 3 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 5 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Giới hạn cho mỗi lần khám, điều trị Bao gồm: - Khám bệnh; - Thuốc điều trị; - Các kỹ thuật chẩn đoán; - Chi phí Điều … |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 11 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 4: Lựa chọn Chương trình bảo hiểm › Bảng Giới hạn bảo hiểm tối đa của mỗi Chương trình: | Bảng (Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú, Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm, Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm, C… |
| 2 | ✅ E2 | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 3 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Các Giới hạn phụ như sau: | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - I. Giới hạn cho mỗi lần khám, điều trị Bao gồm: - Khám bệnh; - Thuốc điều trị; - Các kỹ thuật chẩn đoán; - Chi phí Điều … |
| 4 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.11. Kiểm tra sức khỏe định kỳ, khám giám định y khoa, tiêm chủng Vắc-xin và tiêm các chế phẩm miễn dịch, thực hiện các xét nghiệm tầm soát; - 10.12. Điều t… |
| 5 |  | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |

</details>

## G13 · multi_condition

**Câu hỏi:** Bảo Việt Nhân thọ giải quyết quyền lợi bảo hiểm An Vui Sống Khỏe trong bao lâu, và tôi phải gửi hồ sơ trong thời hạn nào?

**Đáp án chuẩn:** Bảo Việt Nhân thọ giải quyết trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ (Điều 21). Hồ sơ phải gửi trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do bất khả kháng (Điều 20).

- **E1**: `bvl-avsk-2022` · Điều 20, Điều 21 · tr.22 · cần chứa: 'trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 2 | 1.00 |
| recursive | E1: 2 | 1.00 |
| structure_nobc | E1: 1 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 2 | ✅ E1 | `bvl-avsk-2022` · 22,23 |  | hiệu lực theo quy định của Sản phẩm chính. Phí bảo hiểm của Sản phẩm bổ trợ này sẽ không được khấu trừ từ Giá trị Tài khoản Hợp đồng, kể cả khi Sản phẩm chính c… |
| 3 |  | `bvl-avsk-2022` · 16,17 |  | ngày; - Quyền lợi Thai sản: 270 ngày; - Với các sự kiện bảo hiểm do Tai nạn: không áp dụng Thời gian chờ. 8.2. Tại mỗi thời điểm, Bảo Việt Nhân thọ chỉ chấp nhậ… |
| 4 |  | `bvl-avsk-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm sóc sức khỏe do … |
| 5 |  | `bvl-avsk-2022` · 3,4 |  | bảo hiểm \| 20 \| \| Điều 22: Hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm \| 20 \| 1 Quy tắc, Điều khoản Sản phẩm bổ trợ này là Thỏa thuận bổ sung kèm theo Sản phẩm … |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 2 | ✅ E1 | `bvl-avsk-2022` · 1 |  | ## CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM ## Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải l… |
| 3 |  | `bvl-avsk-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm sóc sức khỏe do … |
| 4 |  | `bvl-avsk-2022` · 1 |  | Việc tái tục các quyền lợi của Sản phẩm bổ trợ này từ tuổi 66 đến tuổi 69 chỉ được xem xét nếu Người được bảo hiểm đã tham gia liên tục ít nhất 5 năm. - 1.3. "C… |
| 5 |  | `daiichi-tktt2015-2025` · 1 |  | ## 15.3. Thời hạn nộp hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm Thời hạn nộp hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm là 01 (một) năm kể từ ngày xảy ra sự … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 4 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 |  | `bvl-avsk-2022` · 11,12 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 5: Phạm vi địa lý Bảo Việt Nhân thọ chi trả các quyền lợi bảo hiểm của Sản phẩm bổ trợ này khi Chi phí y tế thực tế phát sinh trong phạm vi lãnh thổ Việt N… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 2 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | - Các bằng chứng hoặc các giấy tờ bổ sung cần thiết khác (nếu có) theo yêu cầu của Bảo Việt Nhân thọ để phục vụ cho việc giải quyết quyền lợi bảo hiểm. - Trường… |
| 5 |  | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 22,23 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 21: Thời hạn giải quyết quyền lợi bảo hiểm Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy… |
| 2 |  | `bvl-avsk-2022` · 3 | An Vui Sống Khỏe | (Phê chuẩn theo Công văn số 2217/BTC-QLBH ngày 08 tháng 03 năm 2022 của Bộ Tài chính) |
| 3 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG V: THỦ TỤC GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | Điều 20: Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi … |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 5 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |

</details>

## G14 · fact

**Câu hỏi:** Nếu không có yêu cầu bồi thường trong 3 năm liên tục thì An Vui Sống Khỏe giảm phí bao nhiêu?

**Đáp án chuẩn:** Giảm 15% phí bảo hiểm của quyền lợi tương ứng cho một năm tái tục tiếp theo (1 năm: 5%, 2 năm: 10%). Chỉ áp dụng tỷ lệ cao nhất, không cộng dồn (Điều 7).

- **E1**: `bvl-avsk-2022` · Điều 7 · tr.16 · cần chứa: '03 năm tham gia liên tục'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 1 | 1.00 |
| recursive | E1: 1 | 1.00 |
| structure_nobc | E1: 2 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 15,16 |  | bảo hiểm nào theo Sản phẩm bổ trợ này, Bên mua bảo hiểm sẽ được giảm phí cho một năm tái tục tiếp theo. Tỉ lệ giảm phí bảo hiểm tái tục cho từng Quyền lợi bảo h… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 |  | `bv-taman-2019` · 20,21 |  | ột quỵ) 5. Suy tim mất bù (bệnh tim giai đoạn cuối) 6. Phẫu thuật động mạch chủ/van tim 7. Bệnh Parkinson/Alzheimer 8. Phẫu thuật sọ não do bệnh của não bộ 9. H… |
| 4 |  | `bv-taman-2019` · 22,23 |  | trong vòng 30 ngày trước khi nhập viện \| 2.000.000/năm \| 5.000.000/năm \| 7.500.000/năm \| \| 4. Chi phí tái khám và điều trị trong vòng 30 ngày sau khi xuất viện … |
| 5 |  | `bv-taman-2019` · 23,24,25 |  | được bảo hiểm trong Hợp đồng) theo yêu cầu của Bên mua bảo hiểm/Người được bảo hiểm, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại đối vớ… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 15,16 |  | ## Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với n… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 |  | `bv-taman-2019` · 21,22 |  | ## BIỂU PHÍ BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN (Ban hành theo Quyết định số 1808/QĐ-BHBV ngày 29 tháng 3 năm 2019 của Tổng Công ty Bảo hiểm Bảo Việt) Đơn vị: VNĐ… |
| 4 |  | `bv-taman-2019` · 1,2,3,4 |  | 31. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 32. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |
| 5 |  | `bv-taman-2019` · 22,23 |  | ## QUY ĐỊNH ĐỒNG CHI TRẢ ĐỐI VỚI TRẺ EM TỪ 15 NGÀY TUỔI ĐẾN 3 TUỔI - Tỷ lệ áp dụng đồng chi trả: 70/30 (Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG IV: PHÍ BẢO HIỂM | Điều 19: Gia hạn đóng phí bảo hiểm - 19.1. Trường hợp Bên mua bảo hiểm không đóng phí bảo hiểm theo đúng thời hạn đã thoả thuận, Phí bảo hiểm đến hạn của Sản ph… |
| 5 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 31. Điều trị kiểm soát trọng lượng cơ thể (tăng hoặc giảm cân); suy dinh dưỡng, còi xương, béo phì. 32. Điều trị bệnh rối loạn tâm thần và hành vi, bệnh tâm thầ… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |
| 5 |  | `bvl-avsk-2022` · 22 | An Vui Sống Khỏe › CHƯƠNG IV: PHÍ BẢO HIỂM | Điều 19: Gia hạn đóng phí bảo hiểm - 19.1. Trường hợp Bên mua bảo hiểm không đóng phí bảo hiểm theo đúng thời hạn đã thoả thuận, Phí bảo hiểm đến hạn của Sản ph… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | Bảng (Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo)) - Không phát sinh yêu cầu chi trả… |
| 2 |  | `bvl-avsk-2022` · 15,16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm 7.1. Trong khoảng thời gian một năm liền trước thời điểm xem xét hoặc đối với năm … |
| 3 |  | `bvl-avsk-2022` · 16 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 7: Quyền lợi giảm phí khi không có yêu cầu giải quyết quyền lợi bảo hiểm | 7.2. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục Sản phẩm bổ trợ này. Riêng đối với năm đầu tiên tham gia, khoảng thời gian xét giảm phí l… |
| 4 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | 2. Loại trừ trách nhiệm bảo hiểm Các trường hợp Bảo Việt Nhân thọ không trả quyền lợi bảo hiểm (loại trừ trách nhiệm bảo hiểm) được nêu tại Điều 10. 3. Thời hạn… |
| 5 |  | `bv-taman-2019` · 22 | Bảo Việt Tâm An › BẢNG QUYỀN LỢI BẢO HIỂM SỨC KHỎE BẢO VIỆT TÂM AN | Bảng (PHÚC, LỘC, THỌ) - 5. Dịch vụ xe cứu thương, xe cấp cứu bằng đường bộ — PHÚC: 5.000.000/năm; LỘC: 10.000.000/năm; THỌ: 10.000.000/năm - 6. Chi phí Phẫu thu… |

</details>

## G15 · exclusion

**Câu hỏi:** An Vui Sống Khỏe có chi trả điều trị đông y, châm cứu không?

**Đáp án chuẩn:** Không. Các phương pháp điều trị không phải Tây y (y học dân tộc, y học cổ truyền, châm cứu, điều trị tại khoa Đông y/Y học cổ truyền/Châm cứu) bị loại trừ theo Điều 10.18.

- **E1**: `bvl-avsk-2022` · Điều 10.18 · tr.18 · cần chứa: 'y học cổ truyền, châm cứu'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 9 | 0.00 |
| recursive | E1: — | 0.00 |
| structure_nobc | E1: 6 | 0.00 |
| structure | E1: 2 | 1.00 |
| structure+ctx | E1: 2 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 2 |  | `bvl-avsk-2022` · 10 |  | sĩ chỉ định để điều trị bệnh lý hoặc tổn thương thuộc phạm vi bảo hiểm và không thuộc các trường hợp loại trừ theo quy định tại Quy tắc, Điều khoản này. Thuốc đ… |
| 3 |  | `bvl-avsk-2022` · 8,9 |  | Phẫu thuật. - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao… |
| 4 |  | `bvl-avsk-2022` · 11,12 |  | ---\|---\|---\|---\|---\|---\| \| Quyền lợi bổ sung tùy chọn \| B. Quyền lợi Điều trị Ngoại trú \| Không áp dụng \| 10 triệu đồng/năm \| 20 triệu đồng/năm \| 40 triệu đồng/… |
| 5 |  | `bvl-avsk-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm sóc sức khỏe do … |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 2 |  | `bvl-avsk-2022` · 1 |  | Bảo Việt Nhân thọ chi trả chi phí cho vitamin và thuốc bổ (bao gồm Thuốc tăng cường miễn dịch), tối đa bằng 20% tổng chi phí thuốc thuộc phạm vi bảo hiểm, khi t… |
| 3 |  | `bvl-avsk-2022` · 10 |  | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 4 |  | `bvl-avsk-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm sóc sức khỏe do … |
| 5 |  | `bvl-avsk-2022` · 9 |  | Bảo Việt Nhân thọ chỉ chi trả cho một lần cấy ghép nội tạng trong toàn bộ thời gian tham gia Sản phẩm bổ trợ này, bao gồm cả thời gian tái tục của Sản phẩm bổ t… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |
| 3 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao gồm cả Điều… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 5 |  | `manulife-cssknc-2026` · 10,11 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | 14. Điều trị theo phương pháp Y Học Thay Thế đối với quyền lợi Điều Trị Nội Trú; phục hồi chức năng (ngoại trừ Vật Lý Trị Liệu) đối với quyền lợi Điều Trị Nội T… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 3 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao gồm cả Điều… |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | Các khoản Chi phí sinh thường (Khoản 1.32), Chi phí sinh mổ (Khoản 1.33), chi phí điều trị Biến chứng thai sản (Khoản 1.34) không bao gồm: chi phí khám thai địn… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 2 | ✅ E1 | `bvl-avsk-2022` · 17,18,19 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | - 10.17. Điều dưỡng, an dưỡng, phục hồi chức năng, Vật lý trị liệu (trừ Vật lý trị liệu thuộc Quyền lợi Điều trị Ngoại trú, nếu có tham gia); - 10.18. Các phươn… |
| 3 |  | `bvl-avsk-2022` · 3 | An Vui Sống Khỏe | (Phê chuẩn theo Công văn số 2217/BTC-QLBH ngày 08 tháng 03 năm 2022 của Bộ Tài chính) |
| 4 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - 1.28. "Chi phí điều trị ung thư" là chi phí xạ trị, hóa trị, liệu pháp trúng đích (ngoại trừ phương pháp Phẫu thuật) theo chỉ định của Bác sĩ, bao gồm cả Điều… |
| 5 |  | `bvl-avsk-2022` · 6,7,8,9,10 | An Vui Sống Khỏe › CHƯƠNG I: NHỮNG QUY ĐỊNH CHUNG › Điều 1: Định nghĩa và giải thích | - Các loại thuốc bổ và vitamin này được Bác sĩ điều trị chỉ định; - Hỗ trợ cho việc điều trị bệnh lý, tổn thương; - Trong danh sách thuốc phải có thuốc điều trị… |

</details>

## G16 · comparison

**Câu hỏi:** So sánh thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia, An Vui Sống Khỏe và Manulife Chăm Sóc Sức Khỏe Nâng Cao.

**Đáp án chuẩn:** Bảo Việt An Gia: sinh nở sau 635 ngày, biến chứng thai sản sau 90 ngày. An Vui Sống Khỏe (Bảo Việt Nhân thọ): 270 ngày. Manulife: 270 ngày.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5 · tr.15 · cần chứa: '635 ngày'
- **E2**: `bvl-avsk-2022` · Điều 8.1 · tr.16 · cần chứa: 'Quyền lợi Thai sản: 270 ngày'
- **E3**: `manulife-cssknc-2026` · Điều 2. Thời gian chờ · tr.10 · cần chứa: '270 ngày Thai sản'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: —, E2: 3, E3: 1 | 0.67 |
| recursive | E1: 5, E2: 9, E3: 1 | 0.67 |
| structure_nobc | E1: 6, E2: 7, E3: — | 0.00 |
| structure | E1: 6, E2: 4, E3: — | 0.33 |
| structure+ctx | E1: 6, E2: 5, E3: — | 0.33 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E3 | `manulife-cssknc-2026` · 9,10 |  | Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai sản. - Các chi phí y tế liên quan đến thai sản (bao gồm việ… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 | ✅ E2 | `bvl-avsk-2022` · 16,17 |  | ngày; - Quyền lợi Thai sản: 270 ngày; - Với các sự kiện bảo hiểm do Tai nạn: không áp dụng Thời gian chờ. 8.2. Tại mỗi thời điểm, Bảo Việt Nhân thọ chỉ chấp nhậ… |
| 4 |  | `manulife-cssknc-2026` · 24,25 |  | thường, xét nghiệm máu cơ bản, chi phí chích ngừa, siêu âm thai theo chỉ định của Bác Sĩ. Manulife không chi trả cho các chi phí xét nghiệm tầm soát trước khi s… |
| 5 |  | `bvl-avsk-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm sóc sức khỏe do … |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E3 | `manulife-cssknc-2026` · 9,10 |  | ## Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai s… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 |  | `manulife-cssknc-2026` · 24 |  | \| 36. Kiểm Tra Thai Định Kỳ \| Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu thông thường, xét … |
| 4 |  | `manulife-cssknc-2026` · 1,2 |  | ## 6.1. Người nhận quyền lợi bảo hiểm Trừ trường hợp có thỏa thuận khác giữa Manulife và Bên Mua Bảo Hiểm, các quyền lợi bảo hiểm nêu tại Sản Phẩm Bảo Hiểm này … |
| 5 | ✅ E1 | `bv-angia-2016` · 15 |  | \| THAI SẢN \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\| \| Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm \| 21.000.000 \| 31.500.000 \| \| Phí bảo hiểm/ người/năm … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 4 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |
| 5 |  | `manulife-cssknc-2026` · 13 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.1. Người nhận quyền lợi bảo hiểm Trừ trường hợp có thỏa thuận khác giữa Manulife và Bên Mua Bảo Hiểm, các quyền lợi bảo hiểm nêu tại Sản Phẩm Bảo Hiểm này sẽ … |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |
| 4 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |
| 5 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 10 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM | Điều 2. THỜI GIAN CHỜ Thời gian chờ là thời gian mà trong đó nếu ngày khám, ngày chẩn đoán Bệnh, ngày bắt đầu của Đợt Điều Trị xảy ra trong thời gian này, Manul… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 | An Vui Sống Khỏe | TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Chăm … |
| 3 |  | `manulife-cssknc-2026` · 14,15 | Chăm Sóc Sức Khỏe Nâng Cao › Chương III. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM › Điều 6. GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | 6.4. Thời hạn giải quyết quyền lợi bảo hiểm - a. Manulife có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 (ba mươi) ngày kể từ ngày nhận được đầy đủ … |
| 4 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 5 | ✅ E2 | `bvl-avsk-2022` · 16,17 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM | Điều 8: Nguyên tắc trả Quyền lợi bảo hiểm - 8.1. Bảo Việt Nhân thọ không trả quyền lợi nêu tại Điều 6 nếu sự kiện bảo hiểm phát sinh đối với Người được bảo hiểm… |

</details>

## G17 · comparison

**Câu hỏi:** Giới hạn quyền lợi thai sản của gói Kim Cương trong Bảo Việt An Gia khác gì so với gói Kim Cương của Manulife?

**Đáp án chuẩn:** An Gia Kim Cương: tối đa 31.500.000 đồng cho một thời hạn bảo hiểm (phí bảo hiểm thai sản 5.500.000 đồng/người/năm). Manulife Kim Cương: tối đa 70 triệu đồng cho mỗi lần mang thai (gồm sinh thường, sinh mổ, biến chứng thai sản), đồng chi trả 20%.

- **E1**: `bv-angia-2016` · Điều khoản bổ sung 5: Bảo hiểm thai sản · tr.15 · cần chứa: '31.500.000'
- **E2**: `manulife-cssknc-2026` · Điều 1.4 Quyền lợi thai sản · tr.9 · cần chứa: 'Giới hạn tối đa cho mỗi lần mang thai', '70 triệu'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 3, E2: 7 | 0.50 |
| recursive | E1: 2, E2: 8 | 0.50 |
| structure_nobc | E1: —, E2: 4 | 0.50 |
| structure | E1: —, E2: 9 | 0.00 |
| structure+ctx | E1: —, E2: — | 0.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 4,5 |  | kể từ thời điểm thay đổi, trừ trường hợp có thỏa thuận khác giữa Bên Mua Bảo Hiểm và Manulife. ## Minh họa về việc bổ sung thêm quyền lợi bảo hiểm Chị H. đang t… |
| 2 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 3 | ✅ E1 | `bv-angia-2016` · 15 |  | Ông Ích Khiêm, Thanh Khê, Đà Nẵng. ## ĐIỀU KHOẢN BỔ SUNG 5: BẢO HIỂM THAI SẢN - Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi - Người được bảo hiểm phải tham… |
| 4 |  | `manulife-cssknc-2026` · 11,12 |  | - Quyền lợi thai sản; và các trường hợp loại trừ khác được quy định trong các định nghĩa Bệnh Viện, Cấy Ghép Nội Tạng, Chi Phí Phẫu Thuật, Cơ Sở Y Tế, Điều Trị … |
| 5 |  | `manulife-cssknc-2026` · 24,25 |  | thường, xét nghiệm máu cơ bản, chi phí chích ngừa, siêu âm thai theo chỉ định của Bác Sĩ. Manulife không chi trả cho các chi phí xét nghiệm tầm soát trước khi s… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `manulife-cssknc-2026` · 9,10 |  | ## Lưu ý: - Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) tại thời điểm phát sinh chi phí thai s… |
| 2 | ✅ E1 | `bv-angia-2016` · 15 |  | \| THAI SẢN \| BẠCH KIM \| KIM CƯƠNG \| \|---\|---\|---\| \| Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm \| 21.000.000 \| 31.500.000 \| \| Phí bảo hiểm/ người/năm … |
| 3 |  | `bvl-avsk-tomtat-2022` · 1 |  | ## TÓM TẮT QUY TẮC, ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG KHI THAM GIA SẢN PHẨM BỔ TRỢ AN VUI SỐNG KHỎE - BẢO HIỂM CHĂM SÓC SỨC KHỎE Sản phẩm bổ trợ Bảo hiểm Ch… |
| 4 |  | `manulife-cssknc-2026` · 1,2 |  | Chương trình bảo hiểm Bên Mua Bảo Hiểm lựa chọn được thể hiện trên Trang Hợp Đồng (Giấy Chứng Nhận Bảo Hiểm) hoặc Xác Nhận Thay Đổi Hợp Đồng, nếu có. Trong trườ… |
| 5 |  | `manulife-cssknc-2026` · 24 |  | \| 36. Kiểm Tra Thai Định Kỳ \| Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu thông thường, xét … |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |
| 3 |  | `manulife-cssknc-2026` · 4 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM | Theo đó: - Quyền lợi Điều Trị Nội Trú là quyền lợi bảo hiểm mặc định cho tất cả các chương trình bảo hiểm; - Quyền lợi Điều Trị Ngoại Trú, quyền lợi Điều Trị Nh… |
| 4 | ✅ E2 | `manulife-cssknc-2026` · 9 | Chăm Sóc Sức Khỏe Nâng Cao › Chương I. QUYỀN LỢI BẢO HIỂM › ĐIỀU 1. QUYỀN LỢI BẢO HIỂM › Mức Đồng Chi Trả: | Bảng (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) - Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản (là tổng quyền lợi bảo hiểm… |
| 5 |  | `manulife-cssknc-2026` · 22 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 9. Bệnh Viện Tư Nhân — col1: Là Bệnh Viện được thành lập, sở hữu và quản lý bởi cá nhân, doanh nghiệp hoặc tổ chức không phải là tổ chức Nhà nước.… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 5 |  | `manulife-cssknc-2026` · 24 | Chăm Sóc Sức Khỏe Nâng Cao › Chương VII. CÁC THUẬT NGỮ CẦN BIẾT | Bảng (col1) - 36. Kiểm Tra Thai Định Kỳ — col1: Là Chi Phí Y Tế Thực Tế phát sinh cho việc kiểm tra thai định kỳ bao gồm các chi phí khám, xét nghiệm nước tiểu … |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Thai sản — Bạc: Không áp dụng; Vàng: 15.000.000 đồng/năm; Bạch Kim: 30.000.000 đồ… |
| 2 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - 1. Chi phí sinh thường — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/lần; Bạch Kim: 20.000.000 đồng/lần; Kim Cương: 30.000… |
| 3 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › Quyền lợi Thai sản chỉ áp dụng với Người được … | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn phụ trong Phần V — Bạc: Chi phí sinh thường, Chi phí sinh mổ, chi phí điều trị Biến chứng thai sản được chi trả… |
| 4 |  | `bvl-avsk-2022` · 14 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.2. Quyền lợi Điều trị Ngoại trú › Thai sản C… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.… |
| 5 |  | `bvl-avsk-2022` · 15 | An Vui Sống Khỏe › CHƯƠNG II: QUYỀN LỢI BẢO HIỂM › Điều 6: Quyền lợi bảo hiểm › 6.1. Quyền lợi Điều trị Nội trú › 6.3. Quyền lợi Điều trị Nha khoa › Chương trìn… | Bảng (Bạc, Vàng, Bạch Kim, Kim Cương) - Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Nha khoa — Bạc: Không áp dụng; Vàng: 3.000.000 đồng/năm; Bạch Kim: 5.000… |

</details>

## G18 · versioning

**Câu hỏi:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) của Dai-ichi Life hiện được ban hành theo văn bản nào?

**Đáp án chuẩn:** Sản phẩm được Bộ Tài chính phê chuẩn theo công văn 14187/BTC-QLBH ngày 09/10/2015 (và công văn 8361/BTC-QLBH ngày 23/06/2017, 623/BTC-QLBH ngày 16/01/2020). Quy tắc và Điều khoản hiện hành được sửa đổi và ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025.

- **E1**: `daiichi-tktt2015-2025` · Trang bìa Quy tắc và Điều khoản · tr.4 · cần chứa: '424/GD/Dai-ichi/2025'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 1 | 1.00 |
| recursive | E1: 2 | 1.00 |
| structure_nobc | E1: 1 | 1.00 |
| structure | E1: 1 | 1.00 |
| structure+ctx | E1: 1 | 1.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 3,4,5 |  | thoại (028) 38 100 888, bấm phím số 1 hoặc tra cứu thông tin tại địa chỉ website https://dai-ichi-life.com.vn. ## QUY TẮC VÀ ĐIỀU KHOẢN SẢN PHẨM BẢO HIỂM NHÂN T… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 |  | ## TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG SẢN PHẨM BẢO HIỂM NHÂN THỌ TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) Đây là tài liệu tóm tắt các nội dung cơ b… |
| 3 |  | `daiichi-tktt2015-2025` · 6,7 |  | ảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015)". ## CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm n… |
| 4 |  | `daiichi-tktt2015-2025` · 5,6,7 |  | : CHẤM DỨT HỢP ĐỒNG BẢO HIỂM ............................................................................... 11 \| \| Điều 8: GIẢI QUYẾT TRANH CHẤP ..............… |
| 5 |  | `daiichi-tktt2015-2025` · 13,14 |  | (iii) Các điều kiện bảo hiểm khác theo quy định của Dai-ichi Life Việt Nam và quy định pháp luật tại từng thời điểm. - b. Dai-ichi Life Việt Nam sẽ gửi thông bá… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 6,7 |  | Quy tắc và Điều khoản sản phẩm bảo hiểm này ("Quy tắc và Điều khoản") là một phần không thể tách rời của Hợp đồng bảo hiểm giữa Dai-ichi Life Việt Nam và Bên mu… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 |  | ## TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG SẢN PHẨM BẢO HIỂM NHÂN THỌ TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) Đây là tài liệu tóm tắt các nội dung cơ b… |
| 3 | ✅ E1 | `daiichi-tktt2015-2025` · 1 |  | ## VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC ## Ngoài các nội dung nêu trên, Quý khách cần lưu ý một số nội dung sau: - Tuân thủ nghĩa vụ đóng phí bảo hiểm đầy đủ, đúng hạn … |
| 4 |  | `daiichi-tktt2015-2025` · 1 |  | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 5 |  | `daiichi-tktt2015-2025` · 1 |  | ## CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ Trong toàn bộ Hợp đồng bảo hiểm này, các thuật ngữ và từ ngữ viết tắt được hiểu và g… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) | TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG SẢN PHẨM BẢO HIỂM NHÂN THỌ TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) Đây là tài liệu tóm tắt các nội dung cơ bản … |
| 4 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 5 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | - (iii) Các điều kiện bảo hiểm khác theo quy định của Dai-ichi Life Việt Nam và quy định pháp luật tại từng thời điểm. - b. Dai-ichi Life Việt Nam sẽ gửi thông … |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.6. Chấp nhận bảo hiểm có điều kiện - a. Trường hợp Bên mua bảo hiểm và/hoặc Người được bảo hiểm vi phạm nghĩa vụ cung cấp đối với bất kỳ thông tin nào về sức … |
| 5 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.1. Nghĩa vụ cung cấp thông tin của Bên mua bảo hiểm, Người được bảo hiểm - a. Bên mua bảo hiểm và Người được bảo hiểm có nghĩa vụ cung cấp đầy đủ và chính xác… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E1 | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 2 | ✅ E1 | `daiichi-tktt2015-2025` · 4 | Tử kỳ tái tục hàng tháng (2015) › VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC | TỬ KỲ TÁI TỤC HÀNG THÁNG (2015) (Sản phẩm bảo hiểm nhân thọ Tử kỳ tái tục hàng tháng (2015) được phê chuẩn theo công văn số 14187/BTC-QLBH ngày 09/10/2015, công… |
| 3 |  | `daiichi-tktt2015-2025` · 7,8,9,10 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ | - 1.11. Ngày gia hạn tháng hợp đồng: là ngày lặp lại hàng tháng của Ngày hiệu lực hợp đồng. Nếu tháng không có ngày này thì ngày cuối cùng của tháng đó sẽ là Ng… |
| 4 |  | `daiichi-tktt2015-2025` · 13,14 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.6. Chấp nhận bảo hiểm có điều kiện - a. Trường hợp Bên mua bảo hiểm và/hoặc Người được bảo hiểm vi phạm nghĩa vụ cung cấp đối với bất kỳ thông tin nào về sức … |
| 5 |  | `daiichi-tktt2015-2025` · 11,12 | Tử kỳ tái tục hàng tháng (2015) › CHƯƠNG 1: NHỮNG ĐIỀU KHOẢN CHUNG Điều 1: ĐỊNH NGHĨA VÀ GIẢI THÍCH TỪ NGỮ › Điều 4: NGHĨA VỤ CUNG CẤP THÔNG TIN | 4.1. Nghĩa vụ cung cấp thông tin của Bên mua bảo hiểm, Người được bảo hiểm - a. Bên mua bảo hiểm và Người được bảo hiểm có nghĩa vụ cung cấp đầy đủ và chính xác… |

</details>

## G19 · no_diacritics

**Câu hỏi:** thoi han bao hiem cua tu ky tai tuc hang thang dai ichi la bao lau, NDBH toi da bao nhieu tuoi

**Đáp án chuẩn:** Thời hạn bảo hiểm là 01 tháng kể từ ngày hiệu lực hợp đồng và được gia hạn hàng tháng nếu hợp đồng không chấm dứt theo Điều 7 (Điều 1.21). Người được bảo hiểm từ 18 đến 75 tuổi khi tham gia; tuổi tối đa khi kết thúc thời hạn bảo hiểm là 76 tuổi (Điều 1.13).

- **E1**: `daiichi-tktt2015-2025` · Điều 1.21 · tr.9 · cần chứa: '1.21. Thời hạn bảo hiểm'
- **E2**: `daiichi-tktt2015-2025` · Điều 1.13 · tr.8 · cần chứa: '76 (bảy mươi sáu) tuổi'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: —, E2: — | 0.00 |
| recursive | E1: —, E2: — | 0.00 |
| structure_nobc | E1: —, E2: — | 0.00 |
| structure | E1: —, E2: — | 0.00 |
| structure+ctx | E1: —, E2: — | 0.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 1,2 |  | QTĐK \| \| SỰ KIỆN BẢO HIỂM \| QUYỀN LỢI \| \|---\|---\|---\| \| Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn \| NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ v… |
| 2 |  | `daiichi-tktt2015-2025` · 2 |  | ý hoặc có tính toán của Người thụ hưởng hoặc của BMBH hoặc của NĐBH; • Tham gia vào các hoạt động bất hợp pháp; • Chấn thương do tham gia các cuộc đua, các loại… |
| 3 |  | `manulife-cssknc-2026` · 2,3 |  | Bảo Hiểm này được đính kèm sẽ áp dụng cho Sản Phẩm Bảo Hiểm này. Trong trường hợp có sự khác biệt, Quy Tắc, Điều Kiện và Điều Khoản của Sản Phẩm Bảo Hiểm này sẽ… |
| 4 |  | `bv-angia-2016` · 18,19 |  | là người thừa kế/người thụ hưởng/người được chỉ định trên GCNBH/ người được ủy quyền hợp pháp của NĐBH kê khai và ký tên (trừ trường hợp trẻ em do bố mẹ/người g… |
| 5 |  | `bv-angia-2016` · 26,27,28 |  | 0,2% STBH \| 0,2% STBH \| 0,2% STBH \| \| Từ 1 đến \| Từ 1 đến \| 600.000 \| 600.000 \| 1.500.000 \| 2.600.000 \| 3.900.000 \| \| 4. Bảo hiểm Nha khoa \| 18 tuổi Từ 19 đến 6… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 1,2,3 |  | \| 2. BH Tai nạn cá nhân \| 2. BH Tai nạn cá nhân \| 0,09% STBH \| 0,09% TBH \| 0,09% STBH \| 0,09% STBH \| 0,09% STBH \| \| 3. BH Sinh mạng cá nhân \| 3. BH Sinh mạng cá… |
| 2 |  | `daiichi-tktt2015-2025` · 1 |  | ## I. QUYỀN LỢI BẢO HIỂM Quy định chi tiết tại Điều 13 của QTĐK \| \| SỰ KIỆN BẢO HIỂM \| QUYỀN LỢI \| \|---\|---\|---\| \| Quyền lợi Tử vong hoặc Thương tật toàn bộ và … |
| 3 |  | `daiichi-tktt2015-2025` · 1 |  | ## VII. CÁC ĐIỂM CẦN LƯU Ý KHÁC ## Ngoài các nội dung nêu trên, Quý khách cần lưu ý một số nội dung sau: - Tuân thủ nghĩa vụ đóng phí bảo hiểm đầy đủ, đúng hạn … |
| 4 |  | `manulife-cssknc-2026` · 3 |  | \| Chương I. QUYỀN LỢI BẢO HIỂM \| Chương I. QUYỀN LỢI BẢO HIỂM \| 4 \| \|---\|---\|---\| \| Điều 1. \| QUYỀN LỢI BẢO HIỂM \| 4 \| \| \| 1.1. Quyền lợi Điều Trị Nội Trú \| 5 \|… |
| 5 |  | `daiichi-tktt2015-2025` · 1 |  | Quy định chi tiết tại Điều 14 của QTĐK Dai-ichi Life Việt Nam sẽ không chi trả quyền lợi bảo hiểm nếu sự kiện bảo hiểm xảy ra do bất cứ lý do nào sau đây: \| TRƯ… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |
| 2 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 3 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 4 |  | `daiichi-tktt2015-2025` · 3 | Tử kỳ tái tục hàng tháng (2015) | VI. TRƯỜNG HỢP CHẤM DỨT HỢP ĐỒNG BẢO HIỂM TRƯỚC HẠN Quy định chi tiết tại Điều 7 của QTĐK HĐBH được chấm dứt trước hạn theo yêu cầu của BMBH hoặc khi Phí bảo hi… |
| 5 |  | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 3 | Tử kỳ tái tục hàng tháng (2015) | VI. TRƯỜNG HỢP CHẤM DỨT HỢP ĐỒNG BẢO HIỂM TRƯỚC HẠN Quy định chi tiết tại Điều 7 của QTĐK HĐBH được chấm dứt trước hạn theo yêu cầu của BMBH hoặc khi Phí bảo hi… |
| 2 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |
| 3 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 5. Các hành động đánh nhau của Người được bảo hiểm, trừ khi chứng minh được hành động đánh nhau đó chỉ với mục đích tự vệ. 6. Hậu quả của tai nạn xảy ra ngoài t… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 3 | Tử kỳ tái tục hàng tháng (2015) | VI. TRƯỜNG HỢP CHẤM DỨT HỢP ĐỒNG BẢO HIỂM TRƯỚC HẠN Quy định chi tiết tại Điều 7 của QTĐK HĐBH được chấm dứt trước hạn theo yêu cầu của BMBH hoặc khi Phí bảo hi… |
| 2 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |
| 3 |  | `bv-taman-2019` · 14,15,16,17 | Bảo Việt Tâm An | 5. Các hành động đánh nhau của Người được bảo hiểm, trừ khi chứng minh được hành động đánh nhau đó chỉ với mục đích tự vệ. 6. Hậu quả của tai nạn xảy ra ngoài t… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |

</details>

## G20 · no_diacritics

**Câu hỏi:** STBH bao hiem tai nan ca nhan trong An Gia toi da bao nhieu va phi tinh the nao

**Đáp án chuẩn:** Số tiền bảo hiểm tai nạn cá nhân tối đa 1 tỷ đồng/người/vụ (mọi chương trình). Phí bằng 0,09% STBH/năm.

- **E1**: `bv-angia-2016` · Bảng quyền lợi - B.2 Bảo hiểm tai nạn cá nhân · tr.24-25 · cần chứa: 'Tai nạn cá nhân', 'Tối đa 1 tỷ đồng'
- **E2**: `bv-angia-2016` · Biểu phí - B.2 BH tai nạn cá nhân · tr.26 · cần chứa: '0,09% STBH'

| Chiến lược | Hạng bằng chứng | recall@5 |
|---|---|---|
| fixed | E1: 5, E2: — | 0.50 |
| recursive | E1: 3, E2: 1 | 1.00 |
| structure_nobc | E1: 7, E2: 3 | 0.50 |
| structure | E1: 7, E2: 6 | 0.00 |
| structure+ctx | E1: 7, E2: 6 | 0.00 |

<details><summary>fixed: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 26,27,28 |  | 0,2% STBH \| 0,2% STBH \| 0,2% STBH \| \| Từ 1 đến \| Từ 1 đến \| 600.000 \| 600.000 \| 1.500.000 \| 2.600.000 \| 3.900.000 \| \| 4. Bảo hiểm Nha khoa \| 18 tuổi Từ 19 đến 6… |
| 2 |  | `manulife-cssknc-2026` · 2,3 |  | Bảo Hiểm này được đính kèm sẽ áp dụng cho Sản Phẩm Bảo Hiểm này. Trong trường hợp có sự khác biệt, Quy Tắc, Điều Kiện và Điều Khoản của Sản Phẩm Bảo Hiểm này sẽ… |
| 3 |  | `bv-angia-2016` · 16,17 |  | bệnh bẩm sinh, bệnh di truyền/dị tật/khuyết tật bẩm sinh, bệnh dị dạng về gen và mọi biến chứng, hậu quả liên quan đến những bệnh này, những chỉ định phẫu thuật… |
| 4 |  | `daiichi-tktt2015-2025` · 2 |  | ý hoặc có tính toán của Người thụ hưởng hoặc của BMBH hoặc của NĐBH; • Tham gia vào các hoạt động bất hợp pháp; • Chấn thương do tham gia các cuộc đua, các loại… |
| 5 | ✅ E1 | `bv-angia-2016` · 24-25 |  | /vụ \| 500.000/vụ \| 500.000/vụ \| \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG \| B. ĐIỀU KHOẢN BẢO HIỂM BỔ S… |

</details>

<details><summary>recursive: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 | ✅ E2 | `bv-angia-2016` · 1,2,3 |  | \| 2. BH Tai nạn cá nhân \| 2. BH Tai nạn cá nhân \| 0,09% STBH \| 0,09% TBH \| 0,09% STBH \| 0,09% STBH \| 0,09% STBH \| \| 3. BH Sinh mạng cá nhân \| 3. BH Sinh mạng cá… |
| 2 |  | `bv-angia-2016` · 17 |  | - sinh, tất cả các hình thức tiêm chủng, vắcxin và thuốc phòng ngừa (trừ trường hợp tiêm vắc-xin sau khi bị tai nạn hay súc vật, côn trùng cắn). 19. Kiểm tra th… |
| 3 | ✅ E1 | `bv-angia-2016` · 24-25 |  | \| 2. Bảo hiểm Tai nạn cá nhân STBH /người/vụ \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| Tối đa 1 tỷ đồng \| \| 3. Bảo hiểm Sinh… |
| 4 |  | `manulife-cssknc-2026` · 11 |  | 6. Điều dưỡng trừ trường hợp các phương pháp điều trị này là một phần cần thiết của việc Điều Trị Nội Trú theo chỉ định của Bác Sĩ và việc điều trị này phải đượ… |
| 5 |  | `manulife-cssknc-2026` · 3 |  | \| Chương I. QUYỀN LỢI BẢO HIỂM \| Chương I. QUYỀN LỢI BẢO HIỂM \| 4 \| \|---\|---\|---\| \| Điều 1. \| QUYỀN LỢI BẢO HIỂM \| 4 \| \| \| 1.1. Quyền lợi Điều Trị Nội Trú \| 5 \|… |

</details>

<details><summary>structure_nobc: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 2 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 3 | ✅ E2 | `bv-angia-2016` · 26 | Bảo Việt An Gia › BIỂU PHÍ BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 2. BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09%… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |

</details>

<details><summary>structure: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |

</details>

<details><summary>structure+ctx: top-5</summary>

| # | Đúng | Tài liệu · trang | Breadcrumb | Nội dung (đầu chunk) |
|---|---|---|---|---|
| 1 |  | `bv-angia-2016` · 16,17,18 | Bảo Việt An Gia | 19. Kiểm tra thị lực, đục thủy tinh thể, thính giác thông thường, lão hóa, thoái hóa, điều trị suy biến tự nhiên/không phải vì lý do bệnh lý của cho việc suy gi… |
| 2 |  | `bv-angia-2016` · 24-25 | Bảo Việt An Gia › BẢNG QUYỀN LỢI BẢO HIỂM "BẢO VIỆT AN GIA" › B. ĐIỀU KHOẢN BẢO HIỂM BỔ SUNG | Bảng (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) - 3. Bảo hiểm Sinh mạng cá nhân STBH/người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồn… |
| 3 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › TÓM TẮT QUY TẮC VÀ ĐIỀU KHOẢN VÀ MỘT SỐ LƯU Ý QUAN TRỌNG | Bảng (col1) - HĐBH — col1: Hợp đồng bảo hiểm - Bên mua bảo hiểm — col1: BMBH - Người được bảo hiểm — col1: NĐBH - Quy tắc và Điều khoản được ban hành theo Quyết… |
| 4 |  | `daiichi-tktt2015-2025` · 1 | Tử kỳ tái tục hàng tháng (2015) › I. QUYỀN LỢI BẢO HIỂM | Bảng (SỰ KIỆN BẢO HIỂM, QUYỀN LỢI) - Quyền lợi Tử vong hoặc Thương tật toàn bộ và vĩnh viễn — SỰ KIỆN BẢO HIỂM: NĐBH tử vong; hoặc NĐBH bị Thương tật toàn bộ và… |
| 5 |  | `daiichi-tktt2015-2025` · 2 | Tử kỳ tái tục hàng tháng (2015) › II. ĐIỀU KHOẢN LOẠI TRỪ TRÁCH NHIỆM BẢO HIỂM | Bảng (ĐIỀU KHOẢN LOẠI TRỪ) - Trường hợp tử vong — ĐIỀU KHOẢN LOẠI TRỪ: • Tự tử; • Nhiễm HIV/AIDS hay các bệnh có liên quan đến HIV/AIDS; • Sử dụng ma túy, sử dụ… |

</details>

