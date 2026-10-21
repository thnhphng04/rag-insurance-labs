# Lab 4 – Câu trả lời (prompt `naive`)

Sinh tự động. Mỗi câu: câu hỏi, đáp án chuẩn, câu trả lời của hệ thống, trích dẫn và kết quả hậu kiểm.

## G01 · table_lookup · `tra_loi`

**Câu hỏi:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là bao nhiêu một năm?

**Đáp án chuẩn:** 1.887.600 đồng/người/năm (biểu phí An Gia, điều khoản chính, nhóm tuổi từ 31 đến 40).

**Hệ thống:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là 1.887.600 đồng một năm [C3].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: False · quote chặt: 0.0 · quote từng phần: 0.0 · id sửa lại: {'C3': 'C2'} · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C3 | `bv-angia-2016` · tr.26 | Từ 31 đến 40 tuổi — ĐỒNG: 1.315.600; BẠC: 1.887.600; VÀNG: 2.860.000; BẠCH KIM: 3.861.000; KIM CƯƠNG: 4.719.000 |

## G02 · table_lookup · `tra_loi`

**Câu hỏi:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là bao nhiêu?

**Đáp án chuẩn:** 230.000.000 đồng/người/năm. Lưu ý bảng quyền lợi gốc in là "230.00 0.000/ng/năm".

**Hệ thống:** Tổng hạn mức quyền lợi bảo hiểm chính/người/năm của gói Vàng trong Bảo Việt An Gia là 230.000.000 đồng/người/năm [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.24-25 | Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ĐỒNG: 93.800.000/ng/năm; BẠC: 137.600.000/ng/năm; VÀNG: 230.00 0.000/ng/năm; BẠCH KIM: 342.000.000/ng/năm; KIM CƯƠNG: 454.000.000/ng/năm |

## G03 · table_lookup · `tra_loi`

**Câu hỏi:** Với quyền lợi thai sản của Manulife Chăm Sóc Sức Khỏe Nâng Cao, chi phí sinh được chi trả như thế nào?

**Đáp án chuẩn:** Chi phí sinh được chi trả theo Chi Phí Y Tế Thực Tế, nằm trong giới hạn tối đa cho mỗi lần mang thai (Titan 12 triệu, Vàng 25 triệu, Bạch Kim 35 triệu, Kim Cương 70 triệu), áp dụng mức đồng chi trả 20%; chỉ chi trả cho người được bảo hiểm từ đủ 18 đến 45 tuổi.

**Hệ thống:** Chi phí sinh thuộc quyền lợi thai sản và được chi trả theo chương trình bảo hiểm mà Bên Mua Bảo Hiểm lựa chọn, sau khi áp dụng mức đồng chi trả. Mức chi trả cụ thể cho chi phí sinh được quy định trong các mức bảo hiểm như TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG với các hạn mức khác nhau. Quyền lợi thai sản chỉ áp dụng cho Người Được Bảo Hiểm từ đủ 18 đến 45 tuổi tại thời điểm phát sinh chi phí thai sản [C1][C3][C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: False · trích đúng đoạn bằng chứng: False · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `manulife-cssknc-2026` · tr.4 | Quyền lợi thai sản là quyền lợi bảo hiểm có thể được lựa chọn thêm theo yêu cầu của Bên Mua Bảo Hiểm |
| C3 | `manulife-cssknc-2026` · tr.9 | Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 (mười tám) đến 45 (bốn mươi lăm) |
| C4 | `manulife-cssknc-2026` · tr.9 | E. Chi phí sinh |

## G04 · multi_condition · `tra_loi`

**Câu hỏi:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho ai và sau bao lâu thì được chi trả chi phí sinh nở?

**Đáp án chuẩn:** Người được bảo hiểm từ 18 đến 45 tuổi, phải tham gia điều khoản chính tương đương chương trình Bạch Kim hoặc Kim Cương. Chi phí sinh nở chỉ được chi trả sau 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản sau 90 ngày. Giới hạn tối đa 21.000.000 (Bạch Kim) / 31.500.000 (Kim Cương) cho một thời hạn bảo hiểm.

**Hệ thống:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi và phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương. Quyền lợi bảo hiểm chi trả cho chi phí sinh nở được áp dụng sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 0.5 · quote từng phần: 0.5 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C4 | `bv-angia-2016` · tr.15 | Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương. |
| C1 | `bv-angia-2016` · tr.15 | Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. |

## G05 · fact · `tra_loi`

**Câu hỏi:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ nào?

**Đáp án chuẩn:** Áp dụng đồng chi trả 70/30: Bảo Việt chi trả 70%, người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (trừ khoa điều trị tự nguyện/theo yêu cầu của bệnh viện công lập).

**Hệ thống:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ đồng chi trả 70/30, trong đó Bảo Việt chi trả 70% và người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại các cơ sở y tế/bệnh viện công lập (trừ các khoa điều trị tự nguyện/điều trị theo yêu cầu của Bệnh viện công lập) [C1]. Tỷ lệ đồng chi trả này áp dụng cho cả chi phí y tế nội trú và ngoại trú [C2][C3][C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.24-25 | Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) |
| C2 | `bv-angia-2016` · tr.9,10 | Đối tượng trẻ em từ 15 ngày tuổi đến 3 tuổi, quyền lợi chi phí y tế nội trú và ngoại trú áp dụng theo tỷ lệ đồng chi trả được quy định |
| C3 | `bv-angia-2016` · tr.13 | Đối tượng trẻ em từ 15 ngày tuổi đến 3 tuổi, quyền lợi này áp dụng theo tỷ lệ đồng chi trả được quy định |
| C4 | `bv-angia-2016` · tr.12 | Đối tượng trẻ em từ 15 ngày tuổi đến 3 tuổi, quyền lợi này áp dụng theo tỷ lệ đồng chi trả được quy định |

## G06 · fact · `tra_loi`

**Câu hỏi:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là bao lâu?

**Đáp án chuẩn:** 01 năm đối với bệnh có sẵn (và các bệnh tại điểm loại trừ chung số 36), 01 năm đối với bệnh đặc biệt. Ngoài ra: ốm đau bệnh tật 30 ngày, biến chứng thai sản 90 ngày, trẻ em đến 6 tuổi bị viêm phế quản/tiểu phế quản/viêm phổi 06 tháng.

**Hệ thống:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.13,14 | 01 năm đối với bệnh có sẵn và các bệnh được liệt kê tại Điểm loại trừ chung số 36 của Quy tắc bảo hiểm này. - 01 năm đối với bệnh đặc biệt theo định nghĩa. |

## G07 · fact · `tra_loi`

**Câu hỏi:** Bảo Việt Tâm An nhận bảo hiểm cho người ở độ tuổi nào?

**Đáp án chuẩn:** Từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 đến 63 tuổi chỉ được tham gia mới nếu có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ.

**Hệ thống:** Bảo Việt Tâm An nhận bảo hiểm cho người từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực của hợp đồng bảo hiểm và không quá 65 tuổi tại ngày kết thúc hợp đồng bảo hiểm. Trường hợp người được bảo hiểm trên 60 tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực thì chỉ được phép tham gia mới với điều kiện có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ [C2].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bv-taman-2019` · tr.10 | Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lăm (15) ngày tuổi đến sáu mươi ba (63) tuổi tại thời điểm bắt đầu hiệu lực của Hợp đồng bảo hiểm và không quá sáu mươi lăm (65) tuổi tại ngày kết thúc hợp đồng bảo hiểm. |

## G08 · table_lookup · `tra_loi`

**Câu hỏi:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công bao nhiêu?

**Đáp án chuẩn:** 300.000 đồng/ngày, không quá 60 ngày/năm.

**Hệ thống:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công là 300.000 đồng/ngày, không quá 60 ngày/năm [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-taman-2019` · tr.22 | Trợ cấp bệnh viện công — PHÚC: 120.000/ ngày Không quá 60 ngày/năm; LỘC: 300.000/ngày Không quá 60 ngày/năm; THỌ: 450.000/ngày Không quá 60 ngày/năm |

## G09 · multi_condition · `tra_loi`

**Câu hỏi:** Hồ sơ yêu cầu bồi thường Bảo Việt Tâm An phải nộp trong thời hạn nào và Bảo hiểm Bảo Việt giải quyết trong bao lâu?

**Đáp án chuẩn:** Nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng của đợt điều trị (hoặc ngày tử vong) và không quá 01 năm kể từ ngày xảy ra sự kiện bảo hiểm (không tính thời gian bất khả kháng). Bảo hiểm Bảo Việt giải quyết và chi trả trong vòng 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ.

**Hệ thống:** Hồ sơ yêu cầu bồi thường phải được gửi tới Bảo hiểm Bảo Việt trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điều trị của Người được bảo hiểm hoặc ngày Người được bảo hiểm tử vong và không quá một (01) năm kể từ ngày xảy ra sự kiện bảo hiểm [C1]. Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng mười lăm (15) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ, hợp lệ [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 0.0 · quote từng phần: 0.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-taman-2019` · tr.12,13 | Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng của một đợt điều trị của Người được bảo hiểm hoặc ngày Người được bảo hiểm tử vong và không quá một (01) năm kể từ ngày xảy ra sự kiện bảo hiểm. Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng mười lăm (15) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ, hợp lệ. |

## G10 · fact · `tra_loi`

**Câu hỏi:** Nếu tôi tự yêu cầu hủy hợp đồng Bảo Việt Tâm An thì được hoàn lại bao nhiêu phí?

**Đáp án chuẩn:** Bảo hiểm Bảo Việt hoàn trả 80% phí bảo hiểm của thời gian còn lại, với điều kiện trong thời gian hiệu lực chưa có khiếu nại đòi trả tiền bảo hiểm nào. (Nếu Bảo hiểm Bảo Việt yêu cầu hủy thì hoàn toàn bộ phí của thời gian còn lại; trường hợp gian lận chỉ hoàn 70% nếu chưa có bồi thường.)

**Hệ thống:** Nếu Bên mua bảo hiểm/Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại với điều kiện trong thời gian hiệu lực của Hợp đồng bảo hiểm chưa có khiếu nại đòi trả tiền bảo hiểm nào xảy ra [C2].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bv-taman-2019` · tr.11 | Nếu Bên mua bảo hiểm/Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại |

## G11 · fact · `tra_loi`

**Câu hỏi:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là bao lâu?

**Đáp án chuẩn:** 270 ngày (Điều 8.1). Các sự kiện do tai nạn không áp dụng thời gian chờ.

**Hệ thống:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là 270 ngày [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.16,17 | Quyền lợi Thai sản: 270 ngày; |

## G12 · table_lookup · `tra_loi`

**Câu hỏi:** Trong An Vui Sống Khỏe, chương trình nào được mua thêm quyền lợi điều trị ngoại trú và hạn mức là bao nhiêu?

**Đáp án chuẩn:** Chương trình Bạc không áp dụng. Vàng 10 triệu đồng/năm, Bạch Kim 20 triệu đồng/năm, Kim Cương 40 triệu đồng/năm. Người được bảo hiểm tự chi trả 20% chi phí y tế thực tế; giới hạn 10 lần khám/năm.

**Hệ thống:** Trong An Vui Sống Khỏe, các chương trình Vàng, Bạch Kim và Kim Cương được mua thêm quyền lợi điều trị ngoại trú với hạn mức lần lượt là 10 triệu đồng/năm, 20 triệu đồng/năm và 40 triệu đồng/năm. Chương trình Bạc không áp dụng quyền lợi điều trị ngoại trú bổ sung này [C1][C3].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.14 | Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.000.000 đồng/năm; Kim Cương: 40.000.000 đồng/năm |
| C3 | `bvl-avsk-2022` · tr.11 | Quyền lợi bổ sung tùy chọn — Quyền lợi bảo hiểm / A. Quyền lợi Điều trị Nội trú: B. Quyền lợi Điều trị Ngoại trú; Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm: Không áp dụng; Chương trình bảo hiểm / Vàng / 250 triệu đồng/năm: 10 triệu đồng/năm; Chương trình bảo hiểm / Bạch Kim / 500 triệu đồng/năm: 20 triệu đồng/năm; Chương trình bảo hiểm / Kim Cương / 1 tỷ đồng/năm: 40 triệu đồng/năm |

## G13 · multi_condition · `tra_loi`

**Câu hỏi:** Bảo Việt Nhân thọ giải quyết quyền lợi bảo hiểm An Vui Sống Khỏe trong bao lâu, và tôi phải gửi hồ sơ trong thời hạn nào?

**Đáp án chuẩn:** Bảo Việt Nhân thọ giải quyết trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ (Điều 21). Hồ sơ phải gửi trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do bất khả kháng (Điều 20).

**Hệ thống:** Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ. Người yêu cầu giải quyết quyền lợi bảo hiểm phải gửi hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm [C2][C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bvl-avsk-2022` · tr.22,23 | Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ. |
| C1 | `bvl-avsk-2022` · tr.22 | Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi tới Bảo Việt Nhân thọ trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm. |

## G14 · fact · `tra_loi`

**Câu hỏi:** Nếu không có yêu cầu bồi thường trong 3 năm liên tục thì An Vui Sống Khỏe giảm phí bao nhiêu?

**Đáp án chuẩn:** Giảm 15% phí bảo hiểm của quyền lợi tương ứng cho một năm tái tục tiếp theo (1 năm: 5%, 2 năm: 10%). Chỉ áp dụng tỷ lệ cao nhất, không cộng dồn (Điều 7).

**Hệ thống:** Nếu không phát sinh yêu cầu chi trả theo Quyền lợi điều trị tương ứng trong 03 năm tham gia liên tục liền trước thời điểm xem xét, An Vui Sống Khỏe sẽ được giảm phí 15% phí bảo hiểm cho một năm tái tục tiếp theo [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.16 | Không phát sinh yêu cầu chi trả theo Quyền lợi điều trị tương ứng trong 03 năm tham gia liên tục liền trước thời điểm xem xét — Tỉ lệ giảm phí (% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 cho một năm tái tục tiếp theo): 15% |

## G15 · exclusion · `tra_loi`

**Câu hỏi:** An Vui Sống Khỏe có chi trả điều trị đông y, châm cứu không?

**Đáp án chuẩn:** Không. Các phương pháp điều trị không phải Tây y (y học dân tộc, y học cổ truyền, châm cứu, điều trị tại khoa Đông y/Y học cổ truyền/Châm cứu) bị loại trừ theo Điều 10.18.

**Hệ thống:** Sản phẩm An Vui Sống Khỏe không chi trả các phương pháp điều trị không phải Tây y như điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ truyền, khoa Y dược cổ truyền, khoa Châm cứu của các Cơ sở y tế [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.17,18,19 | Các phương pháp điều trị không phải Tây y như điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ truyền, khoa Y dược cổ truyền, khoa Châm cứu của các Cơ sở y tế |

## G16 · comparison · `tra_loi`

**Câu hỏi:** So sánh thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia, An Vui Sống Khỏe và Manulife Chăm Sóc Sức Khỏe Nâng Cao.

**Đáp án chuẩn:** Bảo Việt An Gia: sinh nở sau 635 ngày, biến chứng thai sản sau 90 ngày. An Vui Sống Khỏe (Bảo Việt Nhân thọ): 270 ngày. Manulife: 270 ngày.

**Hệ thống:** Thời gian chờ để được chi trả quyền lợi thai sản của Bảo Việt An Gia là 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực [C2]. Đối với An Vui Sống Khỏe, thời gian chờ quyền lợi thai sản là 270 ngày [C3]. Manulife Chăm Sóc Sức Khỏe Nâng Cao cũng áp dụng thời gian chờ 270 ngày cho quyền lợi thai sản [C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bv-angia-2016` · tr.15 | Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. |
| C3 | `bvl-avsk-2022` · tr.16,17 | Quyền lợi Thai sản: 270 ngày; |
| C4 | `manulife-cssknc-2026` · tr.10 | 270 ngày Thai sản |

## G17 · comparison · `tra_loi`

**Câu hỏi:** Giới hạn quyền lợi thai sản của gói Kim Cương trong Bảo Việt An Gia khác gì so với gói Kim Cương của Manulife?

**Đáp án chuẩn:** An Gia Kim Cương: tối đa 31.500.000 đồng cho một thời hạn bảo hiểm (phí bảo hiểm thai sản 5.500.000 đồng/người/năm). Manulife Kim Cương: tối đa 70 triệu đồng cho mỗi lần mang thai (gồm sinh thường, sinh mổ, biến chứng thai sản), đồng chi trả 20%.

**Hệ thống:** Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm của gói Kim Cương trong Bảo Việt An Gia là 31.500.000 đồng mỗi năm. Trong khi đó, gói Kim Cương của Manulife có giới hạn tối đa cho mỗi lần mang thai là 70 triệu đồng, bao gồm sinh thường, sinh mổ và biến chứng thai sản. Ngoài ra, Manulife còn chi trả chi phí phòng và giường/ngày nằm viện tối đa 10 triệu đồng và chi phí kiểm tra thai định kỳ 3 triệu đồng mỗi lần thăm khám [C1][C4][C5].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 0.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.15 | Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — KIM CƯƠNG: 31.500.000 |
| C4 | `bv-angia-2016` · tr.24-25 | BẢO HIỂM Thai sản — KIM CƯƠNG: 31.500.000/năm |
| C5 | `manulife-cssknc-2026` · tr.9 | Giới hạn tối đa cho mỗi lần mang thai bao gồm: Sinh Thường, Sinh Mổ và Biến Chứng Thai Sản — KIM CƯƠNG: 70 triệu |

## G18 · versioning · `tra_loi`

**Câu hỏi:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) của Dai-ichi Life hiện được ban hành theo văn bản nào?

**Đáp án chuẩn:** Sản phẩm được Bộ Tài chính phê chuẩn theo công văn 14187/BTC-QLBH ngày 09/10/2015 (và công văn 8361/BTC-QLBH ngày 23/06/2017, 623/BTC-QLBH ngày 16/01/2020). Quy tắc và Điều khoản hiện hành được sửa đổi và ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025.

**Hệ thống:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) của Dai-ichi Life hiện được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `daiichi-tktt2015-2025` · tr.4 | Quy tắc và Điều khoản này được sửa đổi và được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam. |

## G19 · no_diacritics · `tra_loi`

**Câu hỏi:** thoi han bao hiem cua tu ky tai tuc hang thang dai ichi la bao lau, NDBH toi da bao nhieu tuoi

**Đáp án chuẩn:** Thời hạn bảo hiểm là 01 tháng kể từ ngày hiệu lực hợp đồng và được gia hạn hàng tháng nếu hợp đồng không chấm dứt theo Điều 7 (Điều 1.21). Người được bảo hiểm từ 18 đến 75 tuổi khi tham gia; tuổi tối đa khi kết thúc thời hạn bảo hiểm là 76 tuổi (Điều 1.13).

**Hệ thống:** Thời hạn bảo hiểm của Tử kỳ tái tục hàng tháng Dai-ichi là đến khi Người được bảo hiểm đạt 76 tuổi. Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 tuổi tính theo tuổi sinh nhật vừa qua tại thời điểm tham gia bảo hiểm [C1].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `daiichi-tktt2015-2025` · tr.7,8,9,10 | Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 (bảy mươi sáu) tuổi. |

## G20 · no_diacritics · `tra_loi`

**Câu hỏi:** STBH bao hiem tai nan ca nhan trong An Gia toi da bao nhieu va phi tinh the nao

**Đáp án chuẩn:** Số tiền bảo hiểm tai nạn cá nhân tối đa 1 tỷ đồng/người/vụ (mọi chương trình). Phí bằng 0,09% STBH/năm.

**Hệ thống:** Số tiền bảo hiểm tai nạn cá nhân tối đa trong An Gia là 1 tỷ đồng cho tất cả các gói ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG. Phí bảo hiểm tai nạn cá nhân được tính bằng 0,09% số tiền bảo hiểm (STBH) cho tất cả các gói này [C1][C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote chặt: 1.0 · quote từng phần: 1.0 · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.24-25 | Bảo hiểm Tai nạn cá nhân STBH /người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồng; BẠCH KIM: Tối đa 1 tỷ đồng; KIM CƯƠNG: Tối đa 1 tỷ đồng |
| C4 | `bv-angia-2016` · tr.26 | BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09% STBH |

## O01 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Phí bảo hiểm bắt buộc trách nhiệm dân sự xe ô tô của Bảo Việt năm 2026 là bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối và chuyển tư vấn viên.

**Hệ thống:** Tài liệu cung cấp không có thông tin về phí bảo hiểm bắt buộc trách nhiệm dân sự xe ô tô của Bảo Việt năm 2026.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote chặt: nan · quote từng phần: nan · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O02 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Sản phẩm An Phúc Gia Lộc của Bảo Việt Nhân thọ có quyền lợi đáo hạn bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối và chuyển tư vấn viên.

**Hệ thống:** Tài liệu cung cấp không đề cập đến quyền lợi đáo hạn của sản phẩm An Phúc Gia Lộc của Bảo Việt Nhân thọ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote chặt: nan · quote từng phần: nan · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O03 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Lãi suất tiền gửi kỳ hạn 12 tháng của Ngân hàng Bảo Việt hiện nay là bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối.

**Hệ thống:** Tài liệu cung cấp không đề cập đến lãi suất tiền gửi kỳ hạn 12 tháng của Ngân hàng Bảo Việt hiện nay.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote chặt: nan · quote từng phần: nan · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O04 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Hợp đồng bảo hiểm số BV-2023-004512 của tôi hiện đang ở trạng thái nào và còn bao nhiêu hạn mức?

**Đáp án chuẩn:** Tài liệu quy tắc không chứa dữ liệu hợp đồng cá nhân. Hệ thống phải từ chối và hướng dẫn tra cứu qua kênh có xác thực (tư vấn viên/cổng khách hàng).

**Hệ thống:** Không có thông tin về trạng thái hiện tại của hợp đồng bảo hiểm số BV-2023-004512 và hạn mức còn lại trong các tài liệu được cung cấp.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote chặt: nan · quote từng phần: nan · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O05 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Manulife có bán bảo hiểm cho thú cưng không, phí bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối.

**Hệ thống:** Tài liệu không đề cập đến việc Manulife có bán bảo hiểm cho thú cưng hay không, cũng như không cung cấp thông tin về mức phí bảo hiểm cho thú cưng.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote chặt: nan · quote từng phần: nan · id sửa lại: không · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

