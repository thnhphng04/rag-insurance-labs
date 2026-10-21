# Lab 4 – Câu trả lời (prompt `basic`)

Sinh tự động. Mỗi câu: câu hỏi, đáp án chuẩn, câu trả lời của hệ thống, trích dẫn và kết quả hậu kiểm.

## G01 · table_lookup · `tra_loi`

**Câu hỏi:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là bao nhiêu một năm?

**Đáp án chuẩn:** 1.887.600 đồng/người/năm (biểu phí An Gia, điều khoản chính, nhóm tuổi từ 31 đến 40).

**Hệ thống:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc cho người 35 tuổi là 1.887.600 đồng một năm.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: False · quote nguyên văn: 0.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C3 | `bv-angia-2016` · tr.26 | Từ 31 đến 40 tuổi — BẠC: 1.887.600 |

## G02 · table_lookup · `tra_loi`

**Câu hỏi:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là bao nhiêu?

**Đáp án chuẩn:** 230.000.000 đồng/người/năm. Lưu ý bảng quyền lợi gốc in là "230.00 0.000/ng/năm".

**Hệ thống:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là 230.000.000/người/năm.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.24-25 | Tổng hạn mức quyền lợi bảo hiểm chính/người/năm — ... VÀNG: 230.00 0.000/ng/năm |

## G03 · table_lookup · `tra_loi`

**Câu hỏi:** Với quyền lợi thai sản của Manulife Chăm Sóc Sức Khỏe Nâng Cao, chi phí sinh được chi trả như thế nào?

**Đáp án chuẩn:** Chi phí sinh được chi trả theo Chi Phí Y Tế Thực Tế, nằm trong giới hạn tối đa cho mỗi lần mang thai (Titan 12 triệu, Vàng 25 triệu, Bạch Kim 35 triệu, Kim Cương 70 triệu), áp dụng mức đồng chi trả 20%; chỉ chi trả cho người được bảo hiểm từ đủ 18 đến 45 tuổi.

**Hệ thống:** Chi phí sinh trong quyền lợi thai sản được chi trả theo mức đồng chi trả tương ứng với chương trình bảo hiểm (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) như ghi trong mục E của bảng mức đồng chi trả, tuy nhiên tài liệu không nêu rõ chi tiết cụ thể mức chi trả. Ngoài ra, chi phí điều trị cấp cứu cho thai sản do tai nạn được chi trả theo Chi Phí Y Tế Thực Tế trong tất cả các chương trình bảo hiểm [C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: False · trích đúng đoạn bằng chứng: False · quote nguyên văn: 0.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C4 | `manulife-cssknc-2026` · tr.9 | E. Chi phí sinh; F. Chi phí Điều Trị Cấp Cứu cho thai sản do Tai Nạn — TITAN: Chi Phí Y Tế Thực Tế; VÀNG: Chi Phí Y Tế Thực Tế; BẠCH KIM: Chi Phí Y Tế Thực Tế; KIM CƯƠNG: Chi Phí Y Tế Thực Tế |

## G04 · multi_condition · `tra_loi`

**Câu hỏi:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho ai và sau bao lâu thì được chi trả chi phí sinh nở?

**Đáp án chuẩn:** Người được bảo hiểm từ 18 đến 45 tuổi, phải tham gia điều khoản chính tương đương chương trình Bạch Kim hoặc Kim Cương. Chi phí sinh nở chỉ được chi trả sau 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản sau 90 ngày. Giới hạn tối đa 21.000.000 (Bạch Kim) / 31.500.000 (Kim Cương) cho một thời hạn bảo hiểm.

**Hệ thống:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi và phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương. Quyền lợi bảo hiểm chi trả chi phí sinh nở sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C4 | `bv-angia-2016` · tr.15 | Người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi |
| C4 | `bv-angia-2016` · tr.15 | Người được bảo hiểm phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương |
| C1 | `bv-angia-2016` · tr.15 | Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực |

## G05 · fact · `tra_loi`

**Câu hỏi:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ nào?

**Đáp án chuẩn:** Áp dụng đồng chi trả 70/30: Bảo Việt chi trả 70%, người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (trừ khoa điều trị tự nguyện/theo yêu cầu của bệnh viện công lập).

**Hệ thống:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ đồng chi trả 70% do Bảo Việt chi trả và 30% người được bảo hiểm tự chi trả, trừ khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (ngoại trừ khoa điều trị tự nguyện/điều trị theo yêu cầu) thì không áp dụng quy định này.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.24-25 | Tỷ lệ áp đồng chi trả : 70/30 ( Bảo Việt chi trả 70%, Người được bảo hiểm tự chi trả 30%) |
| C1 | `bv-angia-2016` · tr.24-25 | Qui định này không áp dụng trong trường hợp Người được bảo hiểm khám và điều trị tại các cơ sở y tế/bệnh viện công lập |

## G06 · fact · `tra_loi`

**Câu hỏi:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là bao lâu?

**Đáp án chuẩn:** 01 năm đối với bệnh có sẵn (và các bệnh tại điểm loại trừ chung số 36), 01 năm đối với bệnh đặc biệt. Ngoài ra: ốm đau bệnh tật 30 ngày, biến chứng thai sản 90 ngày, trẻ em đến 6 tuổi bị viêm phế quản/tiểu phế quản/viêm phổi 06 tháng.

**Hệ thống:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.6666666666666666 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.13,14 | 01 năm đối với bệnh có sẵn và các bệnh được liệt kê tại Điểm loại trừ chung số 36 |
| C2 | `bv-angia-2016` · tr.13 | 01 năm đối với bệnh có sẵn và các bệnh được liệt kê tại Điểm loại trừ chung số 36 |
| C3 | `bv-angia-2016` · tr.16,17,18 | Bệnh có sẵn như định nghĩa trong Quy tắc này chỉ được bảo hiểm từ năm thứ hai tham gia liên tục. Bệnh đặc biệt như định nghĩa trong Quy tắc này chỉ được bảo hiểm từ năm thứ hai tham gia liên tục. |

## G07 · fact · `tra_loi`

**Câu hỏi:** Bảo Việt Tâm An nhận bảo hiểm cho người ở độ tuổi nào?

**Đáp án chuẩn:** Từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 đến 63 tuổi chỉ được tham gia mới nếu có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ.

**Hệ thống:** Bảo Việt Tâm An nhận bảo hiểm cho người từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực hợp đồng và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 tuổi đến 63 tuổi phải có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ để được tham gia mới.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bv-taman-2019` · tr.10 | Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ mười lăm (15) ngày tuổi đến sáu mươi ba (63) tuổi tại thời điểm bắt đầu hiệu lực của Hợp đồng bảo hiểm và không quá sáu mươi lăm (65) tuổi tại ngày kết thúc hợp đồng bảo hiểm. |

## G08 · table_lookup · `tra_loi`

**Câu hỏi:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công bao nhiêu?

**Đáp án chuẩn:** 300.000 đồng/ngày, không quá 60 ngày/năm.

**Hệ thống:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công 300.000 đồng/ngày, không quá 60 ngày/năm.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-taman-2019` · tr.22 | Trợ cấp bệnh viện công — LỘC: 300.000/ngày Không quá 60 ngày/năm |

## G09 · multi_condition · `tra_loi`

**Câu hỏi:** Hồ sơ yêu cầu bồi thường Bảo Việt Tâm An phải nộp trong thời hạn nào và Bảo hiểm Bảo Việt giải quyết trong bao lâu?

**Đáp án chuẩn:** Nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng của đợt điều trị (hoặc ngày tử vong) và không quá 01 năm kể từ ngày xảy ra sự kiện bảo hiểm (không tính thời gian bất khả kháng). Bảo hiểm Bảo Việt giải quyết và chi trả trong vòng 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ.

**Hệ thống:** Hồ sơ yêu cầu bồi thường phải nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng hoặc ngày tử vong và không quá 1 năm kể từ ngày xảy ra sự kiện bảo hiểm. Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng 15 ngày kể từ ngày nhận hồ sơ đầy đủ, hợp lệ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.5 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-taman-2019` · tr.12,13 | Thời hạn nộp hồ sơ yêu cầu bồi thường trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng... không quá một (01) năm kể từ ngày xảy ra sự kiện bảo hiểm |
| C1 | `bv-taman-2019` · tr.12,13 | Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng mười lăm (15) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ, hợp lệ |

## G10 · fact · `tra_loi`

**Câu hỏi:** Nếu tôi tự yêu cầu hủy hợp đồng Bảo Việt Tâm An thì được hoàn lại bao nhiêu phí?

**Đáp án chuẩn:** Bảo hiểm Bảo Việt hoàn trả 80% phí bảo hiểm của thời gian còn lại, với điều kiện trong thời gian hiệu lực chưa có khiếu nại đòi trả tiền bảo hiểm nào. (Nếu Bảo hiểm Bảo Việt yêu cầu hủy thì hoàn toàn bộ phí của thời gian còn lại; trường hợp gian lận chỉ hoàn 70% nếu chưa có bồi thường.)

**Hệ thống:** Nếu Bên mua bảo hiểm/Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại với điều kiện chưa có khiếu nại đòi trả tiền bảo hiểm nào xảy ra trong thời gian hiệu lực hợp đồng.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bv-taman-2019` · tr.11 | Nếu Bên mua bảo hiểm/Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại |

## G11 · fact · `tra_loi`

**Câu hỏi:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là bao lâu?

**Đáp án chuẩn:** 270 ngày (Điều 8.1). Các sự kiện do tai nạn không áp dụng thời gian chờ.

**Hệ thống:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là 270 ngày.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.16,17 | Quyền lợi Thai sản: 270 ngày |

## G12 · table_lookup · `tra_loi`

**Câu hỏi:** Trong An Vui Sống Khỏe, chương trình nào được mua thêm quyền lợi điều trị ngoại trú và hạn mức là bao nhiêu?

**Đáp án chuẩn:** Chương trình Bạc không áp dụng. Vàng 10 triệu đồng/năm, Bạch Kim 20 triệu đồng/năm, Kim Cương 40 triệu đồng/năm. Người được bảo hiểm tự chi trả 20% chi phí y tế thực tế; giới hạn 10 lần khám/năm.

**Hệ thống:** Chương trình Vàng, Bạch Kim và Kim Cương được mua thêm quyền lợi Điều trị Ngoại trú với hạn mức lần lượt là 10 triệu đồng/năm, 20 triệu đồng/năm và 40 triệu đồng/năm. Chương trình Bạc không áp dụng quyền lợi này.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.5 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.14 | Giới hạn bảo hiểm tối đa cho Quyền lợi Điều trị Ngoại trú — Bạc: Không áp dụng; Vàng: 10.000.000 đồng/năm; Bạch Kim: 20.000.000 đồng/năm; Kim Cương: 40.000.000 đồng/năm |
| C3 | `bvl-avsk-2022` · tr.11 | Chương trình bảo hiểm / Bạc / 150 triệu đồng/năm: Không áp dụng; Vàng / 250 triệu đồng/năm: 10 triệu đồng/năm; Bạch Kim / 500 triệu đồng/năm: 20 triệu đồng/năm; Kim Cương / 1 tỷ đồng/năm: 40 triệu đồng/năm |

## G13 · multi_condition · `tra_loi`

**Câu hỏi:** Bảo Việt Nhân thọ giải quyết quyền lợi bảo hiểm An Vui Sống Khỏe trong bao lâu, và tôi phải gửi hồ sơ trong thời hạn nào?

**Đáp án chuẩn:** Bảo Việt Nhân thọ giải quyết trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ (Điều 21). Hồ sơ phải gửi trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do bất khả kháng (Điều 20).

**Hệ thống:** Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ. Người yêu cầu giải quyết quyền lợi bảo hiểm phải gửi hồ sơ trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do sự kiện bất khả kháng hoặc trở ngại khách quan.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.22 | Người yêu cầu giải quyết quyền lợi bảo hiểm phải lập hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm và gửi tới Bảo Việt Nhân thọ trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm. |
| C2 | `bvl-avsk-2022` · tr.22,23 | Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ. |

## G14 · fact · `tra_loi`

**Câu hỏi:** Nếu không có yêu cầu bồi thường trong 3 năm liên tục thì An Vui Sống Khỏe giảm phí bao nhiêu?

**Đáp án chuẩn:** Giảm 15% phí bảo hiểm của quyền lợi tương ứng cho một năm tái tục tiếp theo (1 năm: 5%, 2 năm: 10%). Chỉ áp dụng tỷ lệ cao nhất, không cộng dồn (Điều 7).

**Hệ thống:** Nếu không có yêu cầu chi trả theo Quyền lợi điều trị tương ứng trong 03 năm tham gia liên tục liền trước thời điểm xem xét, tỉ lệ giảm phí cho một năm tái tục tiếp theo là 15% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.16 | Không phát sinh yêu cầu chi trả theo Quyền lợi điều trị tương ứng trong 03 năm tham gia liên tục liền trước thời điểm xem xét — Tỉ lệ giảm phí ... 15% |

## G15 · exclusion · `tra_loi`

**Câu hỏi:** An Vui Sống Khỏe có chi trả điều trị đông y, châm cứu không?

**Đáp án chuẩn:** Không. Các phương pháp điều trị không phải Tây y (y học dân tộc, y học cổ truyền, châm cứu, điều trị tại khoa Đông y/Y học cổ truyền/Châm cứu) bị loại trừ theo Điều 10.18.

**Hệ thống:** Sản phẩm An Vui Sống Khỏe không chi trả chi phí điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ truyền, khoa Y dược cổ truyền, khoa Châm cứu của các Cơ sở y tế.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bvl-avsk-2022` · tr.17,18,19 | Các phương pháp điều trị không phải Tây y như điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ truyền, khoa Y dược cổ truyền, khoa Châm cứu của các Cơ sở y tế |

## G16 · comparison · `tra_loi`

**Câu hỏi:** So sánh thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia, An Vui Sống Khỏe và Manulife Chăm Sóc Sức Khỏe Nâng Cao.

**Đáp án chuẩn:** Bảo Việt An Gia: sinh nở sau 635 ngày, biến chứng thai sản sau 90 ngày. An Vui Sống Khỏe (Bảo Việt Nhân thọ): 270 ngày. Manulife: 270 ngày.

**Hệ thống:** Thời gian chờ quyền lợi thai sản/sinh con của Bảo Việt An Gia là 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản là 90 ngày [C2]. An Vui Sống Khỏe áp dụng thời gian chờ 270 ngày cho quyền lợi thai sản [C3]. Manulife Chăm Sóc Sức Khỏe Nâng Cao cũng áp dụng thời gian chờ 270 ngày cho quyền lợi thai sản [C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.6666666666666666 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C2 | `bv-angia-2016` · tr.15 | Đối với sinh nở: Quyền lợi bảo hiểm này được chi trả với điều kiện sau 635 ngày |
| C3 | `bvl-avsk-2022` · tr.16,17 | Thời gian chờ... - 270 ngày Thai sản |
| C4 | `manulife-cssknc-2026` · tr.10 | - 270 ngày Thai sản |

## G17 · comparison · `tra_loi`

**Câu hỏi:** Giới hạn quyền lợi thai sản của gói Kim Cương trong Bảo Việt An Gia khác gì so với gói Kim Cương của Manulife?

**Đáp án chuẩn:** An Gia Kim Cương: tối đa 31.500.000 đồng cho một thời hạn bảo hiểm (phí bảo hiểm thai sản 5.500.000 đồng/người/năm). Manulife Kim Cương: tối đa 70 triệu đồng cho mỗi lần mang thai (gồm sinh thường, sinh mổ, biến chứng thai sản), đồng chi trả 20%.

**Hệ thống:** Giới hạn trách nhiệm tối đa cho quyền lợi thai sản gói Kim Cương trong Bảo Việt An Gia là 31.500.000 đồng/năm [C1], trong khi gói Kim Cương của Manulife có giới hạn tối đa cho mỗi lần mang thai là 70 triệu đồng, bao gồm sinh thường, sinh mổ và biến chứng thai sản [C5].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 0.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.15 | Giới hạn trách nhiệm tối đa cho một thời hạn bảo hiểm — KIM CƯƠNG: 31.500.000 |
| C5 | `manulife-cssknc-2026` · tr.9 | Giới hạn tối đa cho mỗi lần mang thai bao gồm: ... KIM CƯƠNG: 70 triệu |

## G18 · versioning · `tra_loi`

**Câu hỏi:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) của Dai-ichi Life hiện được ban hành theo văn bản nào?

**Đáp án chuẩn:** Sản phẩm được Bộ Tài chính phê chuẩn theo công văn 14187/BTC-QLBH ngày 09/10/2015 (và công văn 8361/BTC-QLBH ngày 23/06/2017, 623/BTC-QLBH ngày 16/01/2020). Quy tắc và Điều khoản hiện hành được sửa đổi và ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025.

**Hệ thống:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `daiichi-tktt2015-2025` · tr.4 | Quy tắc và Điều khoản này được sửa đổi và được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam. |

## G19 · no_diacritics · `tra_loi`

**Câu hỏi:** thoi han bao hiem cua tu ky tai tuc hang thang dai ichi la bao lau, NDBH toi da bao nhieu tuoi

**Đáp án chuẩn:** Thời hạn bảo hiểm là 01 tháng kể từ ngày hiệu lực hợp đồng và được gia hạn hàng tháng nếu hợp đồng không chấm dứt theo Điều 7 (Điều 1.21). Người được bảo hiểm từ 18 đến 75 tuổi khi tham gia; tuổi tối đa khi kết thúc thời hạn bảo hiểm là 76 tuổi (Điều 1.13).

**Hệ thống:** Thời hạn bảo hiểm của Tử kỳ tái tục hàng tháng Dai-ichi là đến khi Người được bảo hiểm đạt 76 tuổi. Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 tuổi tính theo tuổi sinh nhật vừa qua tại thời điểm tham gia bảo hiểm.

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `daiichi-tktt2015-2025` · tr.7,8,9,10 | Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 (bảy mươi sáu) tuổi. |
| C2 | `daiichi-tktt2015-2025` · tr.14 | Vào Ngày gia hạn tháng hợp đồng ngay sau khi Người được bảo hiểm đạt 76 tuổi; |

## G20 · no_diacritics · `tra_loi`

**Câu hỏi:** STBH bao hiem tai nan ca nhan trong An Gia toi da bao nhieu va phi tinh the nao

**Đáp án chuẩn:** Số tiền bảo hiểm tai nạn cá nhân tối đa 1 tỷ đồng/người/vụ (mọi chương trình). Phí bằng 0,09% STBH/năm.

**Hệ thống:** Số tiền bảo hiểm (STBH) tai nạn cá nhân tối đa là 1 tỷ đồng cho tất cả các gói (ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG) [C1]. Phí bảo hiểm tai nạn cá nhân được tính là 0,09% STBH cho tất cả các gói [C4].

*Hậu kiểm:* ngữ cảnh có bằng chứng: True · trích đúng đoạn bằng chứng: True · quote nguyên văn: 1.0 · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|
| C1 | `bv-angia-2016` · tr.24-25 | Bảo hiểm Tai nạn cá nhân STBH /người/vụ — ĐỒNG: Tối đa 1 tỷ đồng; BẠC: Tối đa 1 tỷ đồng; VÀNG: Tối đa 1 tỷ đồng; BẠCH KIM: Tối đa 1 tỷ đồng; KIM CƯƠNG: Tối đa 1 tỷ đồng |
| C4 | `bv-angia-2016` · tr.26 | BH Tai nạn cá nhân — ĐỒNG: 0,09% STBH; BẠC: 0,09% TBH; VÀNG: 0,09% STBH; BẠCH KIM: 0,09% STBH; KIM CƯƠNG: 0,09% STBH |

## O01 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Phí bảo hiểm bắt buộc trách nhiệm dân sự xe ô tô của Bảo Việt năm 2026 là bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối và chuyển tư vấn viên.

**Hệ thống:** Chưa có thông tin về phí bảo hiểm bắt buộc trách nhiệm dân sự xe ô tô của Bảo Việt năm 2026 trong tài liệu được cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote nguyên văn: nan · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O02 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Sản phẩm An Phúc Gia Lộc của Bảo Việt Nhân thọ có quyền lợi đáo hạn bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối và chuyển tư vấn viên.

**Hệ thống:** Chưa có thông tin về quyền lợi đáo hạn của sản phẩm An Phúc Gia Lộc trong các đoạn tài liệu được cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote nguyên văn: nan · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O03 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Lãi suất tiền gửi kỳ hạn 12 tháng của Ngân hàng Bảo Việt hiện nay là bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối.

**Hệ thống:** Chưa có thông tin về lãi suất tiền gửi kỳ hạn 12 tháng của Ngân hàng Bảo Việt trong tài liệu đã cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote nguyên văn: nan · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O04 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Hợp đồng bảo hiểm số BV-2023-004512 của tôi hiện đang ở trạng thái nào và còn bao nhiêu hạn mức?

**Đáp án chuẩn:** Tài liệu quy tắc không chứa dữ liệu hợp đồng cá nhân. Hệ thống phải từ chối và hướng dẫn tra cứu qua kênh có xác thực (tư vấn viên/cổng khách hàng).

**Hệ thống:** Chưa có thông tin về trạng thái hợp đồng bảo hiểm số BV-2023-004512 và hạn mức trong các đoạn tài liệu được cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote nguyên văn: nan · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

## O05 · out_of_scope · `khong_du_thong_tin`

**Câu hỏi:** Manulife có bán bảo hiểm cho thú cưng không, phí bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối.

**Hệ thống:** Trong các đoạn tài liệu được cung cấp không có thông tin về việc Manulife có bán bảo hiểm cho thú cưng hay mức phí của loại bảo hiểm này. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Hậu kiểm:* ngữ cảnh có bằng chứng: None · trích đúng đoạn bằng chứng: None · quote nguyên văn: nan · id không tồn tại: không

| Trích dẫn | Tài liệu · trang | Quote |
|---|---|---|

