# Lab 6 – Câu trả lời của đồ thị CRAG-lite

Sinh tự động. Mỗi câu: đường đi qua đồ thị, câu trả lời, nhãn judge (so với Lab 4).

## G01 · table_lookup · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là bao nhiêu một năm?

**Đáp án chuẩn:** 1.887.600 đồng/người/năm (biểu phí An Gia, điều khoản chính, nhóm tuổi từ 31 đến 40).

**Đồ thị:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là 1.887.600 đồng một năm [C1].

**Lab 4:** Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là 1.887.600 đồng một năm [C3].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Phí bảo hiểm điều khoản chính (điều trị nội trú) gói Bạc của Bảo Việt An Gia cho người 35 tuổi là 1.887.600 đồng một năm | duoc_ho_tro |

## G02 · table_lookup · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là bao nhiêu?

**Đáp án chuẩn:** 230.000.000 đồng/người/năm. Lưu ý bảng quyền lợi gốc in là "230.00 0.000/ng/năm".

**Đồ thị:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là 230.000.000/người/năm [C1].

**Lab 4:** Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là 230.000.000/người/năm [C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Tổng hạn mức quyền lợi bảo hiểm chính của gói Vàng trong Bảo Việt An Gia là 230.000.000/người/năm | duoc_ho_tro |

## G03 · table_lookup · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Với quyền lợi thai sản của Manulife Chăm Sóc Sức Khỏe Nâng Cao, chi phí sinh được chi trả như thế nào?

**Đáp án chuẩn:** Chi phí sinh được chi trả theo Chi Phí Y Tế Thực Tế, nằm trong giới hạn tối đa cho mỗi lần mang thai (Titan 12 triệu, Vàng 25 triệu, Bạch Kim 35 triệu, Kim Cương 70 triệu), áp dụng mức đồng chi trả 20%; chỉ chi trả cho người được bảo hiểm từ đủ 18 đến 45 tuổi.

**Đồ thị:** Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 đến 45 tại thời điểm phát sinh chi phí thai sản [C2]. Chi phí sinh được chi trả theo mức Chi Phí Y Tế Thực Tế tùy theo chương trình bảo hiểm (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) [C3].

**Lab 4:** Chi phí sinh trong quyền lợi thai sản được chi trả theo mức đồng chi trả tương ứng với chương trình bảo hiểm mà Bên Mua Bảo Hiểm đã lựa chọn. Cụ thể, mức đồng chi trả cho chi phí sinh được quy định trong bảng mức đồng chi trả của các chương trình TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG. Ví dụ, chi phí sinh được chi trả theo Chi Phí Y Tế Thực Tế sau khi áp dụng mức đồng chi trả, không vượt quá giới hạn bảo hiểm của chương trình bảo hiểm tương ứng [C1][C4][C5].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Quyền lợi thai sản chỉ được chi trả cho Người Được Bảo Hiểm có Tuổi từ đủ 18 đến 45 tại thời điểm phát sinh chi phí thai sản | duoc_ho_tro |
| Chi phí sinh được chi trả theo mức Chi Phí Y Tế Thực Tế tùy theo chương trình bảo hiểm (TITAN, VÀNG, BẠCH KIM, KIM CƯƠNG) | duoc_ho_tro |

## G04 · multi_condition · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho ai và sau bao lâu thì được chi trả chi phí sinh nở?

**Đáp án chuẩn:** Người được bảo hiểm từ 18 đến 45 tuổi, phải tham gia điều khoản chính tương đương chương trình Bạch Kim hoặc Kim Cương. Chi phí sinh nở chỉ được chi trả sau 635 ngày kể từ ngày hợp đồng có hiệu lực; biến chứng thai sản sau 90 ngày. Giới hạn tối đa 21.000.000 (Bạch Kim) / 31.500.000 (Kim Cương) cho một thời hạn bảo hiểm.

**Đồ thị:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi và phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương [C4]. Chi phí sinh nở được chi trả sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực [C1].

**Lab 4:** Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi và phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương. Quyền lợi bảo hiểm chi trả cho chi phí sinh nở được áp dụng sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực [C4][C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Bảo hiểm thai sản của Bảo Việt An Gia áp dụng cho người được bảo hiểm có độ tuổi từ 18 đến 45 tuổi và phải tham gia Điều khoản chính, tương đương chương trình Bạch Kim hoặc chương trình Kim Cương. | duoc_ho_tro |
| Chi phí sinh nở được chi trả sau 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. | duoc_ho_tro |

## G05 · fact · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ nào?

**Đáp án chuẩn:** Áp dụng đồng chi trả 70/30: Bảo Việt chi trả 70%, người được bảo hiểm tự chi trả 30%. Quy định này không áp dụng khi khám và điều trị tại cơ sở y tế/bệnh viện công lập (trừ khoa điều trị tự nguyện/theo yêu cầu của bệnh viện công lập).

**Đồ thị:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ đồng chi trả 70/30, trong đó Bảo Việt chi trả 70% và người được bảo hiểm tự chi trả 30% [C1]. Tỷ lệ đồng chi trả này áp dụng cho quyền lợi chi phí y tế nội trú và ngoại trú [C2][C3][C4]. Qui định này không áp dụng khi người được bảo hiểm khám và điều trị tại các cơ sở y tế/bệnh viện công lập (trừ các khoa điều trị tự nguyện/điều trị theo yêu cầu của Bệnh viện công lập) [C1].

**Lab 4:** Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được áp dụng tỷ lệ đồng chi trả 70/30, trong đó Bảo Việt chi trả 70% và người được bảo hiểm tự chi trả 30%. Qui định này không áp dụng khi khám và điều trị tại các cơ sở y tế/bệnh viện công lập (trừ các khoa điều trị tự nguyện/điều trị theo yêu cầu của Bệnh viện công lập) [C1]. Quyền lợi chi phí y tế nội trú và ngoại trú của đối tượng này cũng áp dụng theo tỷ lệ đồng chi trả được quy định trong Bảng Quyền lợi bảo hiểm đính kèm [C2][C3][C4].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Trẻ em từ 15 ngày tuổi đến 3 tuổi tham gia Bảo Việt An Gia được chi trả theo tỷ lệ đồng chi trả 70/30, trong đó Bảo Việt chi trả 70% và người được bảo hiểm tự chi trả 30%. | duoc_ho_tro |
| Tỷ lệ đồng chi trả này áp dụng cho quyền lợi chi phí y tế nội trú và ngoại trú. | duoc_ho_tro |
| Qui định này không áp dụng khi người được bảo hiểm khám và điều trị tại các cơ sở y tế/bệnh viện công lập (trừ các khoa điều trị tự nguyện/điều trị theo yêu cầu của Bệnh viện công lập). | duoc_ho_tro |

## G06 · fact · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là bao lâu?

**Đáp án chuẩn:** 01 năm đối với bệnh có sẵn (và các bệnh tại điểm loại trừ chung số 36), 01 năm đối với bệnh đặc biệt. Ngoài ra: ốm đau bệnh tật 30 ngày, biến chứng thai sản 90 ngày, trẻ em đến 6 tuổi bị viêm phế quản/tiểu phế quản/viêm phổi 06 tháng.

**Đồ thị:** Thời gian chờ đối với bệnh có sẵn là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm. Thời gian chờ đối với bệnh đặc biệt cũng là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm [C1][C2].

**Lab 4:** Thời gian chờ đối với bệnh có sẵn và bệnh đặc biệt trong quy tắc Bảo Việt An Gia là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm [C1][C2].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Thời gian chờ đối với bệnh có sẵn là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm. | duoc_ho_tro |
| Thời gian chờ đối với bệnh đặc biệt cũng là 01 năm kể từ ngày bắt đầu thời hạn bảo hiểm quy định trên Giấy chứng nhận bảo hiểm. | duoc_ho_tro |

## G07 · fact · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Bảo Việt Tâm An nhận bảo hiểm cho người ở độ tuổi nào?

**Đáp án chuẩn:** Từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực và không quá 65 tuổi tại ngày kết thúc hợp đồng. Người trên 60 đến 63 tuổi chỉ được tham gia mới nếu có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ.

**Đồ thị:** Bảo Việt Tâm An nhận bảo hiểm cho người từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực hợp đồng và không quá 65 tuổi tại ngày kết thúc hợp đồng bảo hiểm. Người trên 60 tuổi đến 63 tuổi chỉ được tham gia khi có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ. Người phụ thuộc là con từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang học dài hạn và chưa kết hôn. Người dưới 1 tuổi chỉ được tham gia chương trình Thọ và phải tham gia cùng bố/mẹ. Người dưới 18 tuổi phải tham gia cùng bố/mẹ hoặc có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực để được tham gia độc lập.

**Lab 4:** Người được bảo hiểm là mọi công dân Việt Nam hoặc người nước ngoài cư trú tại Việt Nam từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực của Hợp đồng bảo hiểm và không quá 65 tuổi tại ngày kết thúc hợp đồng bảo hiểm. Trường hợp người được bảo hiểm trên 60 tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực thì chỉ được phép tham gia mới với điều kiện có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ [C2]. Người phụ thuộc là con theo luật pháp của Bên mua bảo hiểm/Người được bảo hiểm, có độ tuổi từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang theo học các khóa học dài hạn và chưa kết hôn [C3].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Bảo Việt Tâm An nhận bảo hiểm cho người từ 15 ngày tuổi đến 63 tuổi tại thời điểm bắt đầu hiệu lực hợp đồng và không quá 65 tuổi tại ngày kết thúc hợp đồng bảo hiểm. | duoc_ho_tro |
| Người trên 60 tuổi đến 63 tuổi chỉ được tham gia khi có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực tại Bảo Việt Nhân thọ. | duoc_ho_tro |
| Người phụ thuộc là con từ 15 ngày tuổi đến 18 tuổi hoặc 24 tuổi nếu đang học dài hạn và chưa kết hôn. | duoc_ho_tro |
| Người dưới 1 tuổi chỉ được tham gia chương trình Thọ và phải tham gia cùng bố/mẹ. | duoc_ho_tro |
| Người dưới 18 tuổi phải tham gia cùng bố/mẹ hoặc có hợp đồng Bảo hiểm Nhân thọ còn hiệu lực để được tham gia độc lập. | duoc_ho_tro |

## G08 · table_lookup · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công bao nhiêu?

**Đáp án chuẩn:** 300.000 đồng/ngày, không quá 60 ngày/năm.

**Đồ thị:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công 300.000 đồng/ngày, không quá 60 ngày/năm [C1].

**Lab 4:** Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công 300.000 đồng/ngày, không quá 60 ngày/năm [C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Chương trình Lộc của Bảo Việt Tâm An trợ cấp bệnh viện công 300.000 đồng/ngày, không quá 60 ngày/năm | duoc_ho_tro |

## G09 · multi_condition · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Hồ sơ yêu cầu bồi thường Bảo Việt Tâm An phải nộp trong thời hạn nào và Bảo hiểm Bảo Việt giải quyết trong bao lâu?

**Đáp án chuẩn:** Nộp trong vòng 60 ngày kể từ ngày điều trị cuối cùng của đợt điều trị (hoặc ngày tử vong) và không quá 01 năm kể từ ngày xảy ra sự kiện bảo hiểm (không tính thời gian bất khả kháng). Bảo hiểm Bảo Việt giải quyết và chi trả trong vòng 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ.

**Đồ thị:** Hồ sơ yêu cầu bồi thường phải được gửi trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng hoặc ngày Người được bảo hiểm tử vong và không quá một (01) năm kể từ ngày xảy ra sự kiện bảo hiểm [C1][C3]. Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng mười lăm (15) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ, hợp lệ [C1][C2].

**Lab 4:** Hồ sơ yêu cầu bồi thường phải được gửi trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng hoặc ngày Người được bảo hiểm tử vong và không quá một (01) năm kể từ ngày xảy ra sự kiện bảo hiểm [C1][C3]. Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng mười lăm (15) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ, hợp lệ [C1][C2].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Hồ sơ yêu cầu bồi thường phải được gửi trong vòng sáu mươi (60) ngày kể từ ngày điều trị cuối cùng hoặc ngày Người được bảo hiểm tử vong và không quá một (01) năm kể từ ngày xảy ra sự kiện bảo hiểm | duoc_ho_tro |
| Bảo hiểm Bảo Việt có trách nhiệm giải quyết và chi trả tiền bảo hiểm trong vòng mười lăm (15) ngày kể từ ngày nhận được hồ sơ yêu cầu bồi thường đầy đủ, hợp lệ | duoc_ho_tro |

## G10 · fact · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Nếu tôi tự yêu cầu hủy hợp đồng Bảo Việt Tâm An thì được hoàn lại bao nhiêu phí?

**Đáp án chuẩn:** Bảo hiểm Bảo Việt hoàn trả 80% phí bảo hiểm của thời gian còn lại, với điều kiện trong thời gian hiệu lực chưa có khiếu nại đòi trả tiền bảo hiểm nào. (Nếu Bảo hiểm Bảo Việt yêu cầu hủy thì hoàn toàn bộ phí của thời gian còn lại; trường hợp gian lận chỉ hoàn 70% nếu chưa có bồi thường.)

**Đồ thị:** Nếu Bên mua bảo hiểm/Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại với điều kiện trong thời gian hiệu lực của Hợp đồng bảo hiểm chưa có khiếu nại đòi trả tiền bảo hiểm nào xảy ra [C2].

**Lab 4:** Nếu Bên mua bảo hiểm hoặc Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại với điều kiện trong thời gian hiệu lực của Hợp đồng bảo hiểm chưa có khiếu nại đòi trả tiền bảo hiểm nào xảy ra [C2].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Nếu Bên mua bảo hiểm/Người được bảo hiểm yêu cầu huỷ bỏ Hợp đồng, Bảo hiểm Bảo Việt sẽ hoàn trả 80% phí bảo hiểm của thời gian còn lại với điều kiện trong thời gian hiệu lực của Hợp đồng bảo hiểm chưa | duoc_ho_tro |

## G11 · fact · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là bao lâu?

**Đáp án chuẩn:** 270 ngày (Điều 8.1). Các sự kiện do tai nạn không áp dụng thời gian chờ.

**Đồ thị:** Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là 270 ngày [C1].

**Lab 4:** Thời gian chờ của quyền lợi Thai sản trong sản phẩm An Vui Sống Khỏe là 270 ngày [C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Thời gian chờ của quyền lợi thai sản trong sản phẩm An Vui Sống Khỏe là 270 ngày | duoc_ho_tro |

## G12 · table_lookup · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Trong An Vui Sống Khỏe, chương trình nào được mua thêm quyền lợi điều trị ngoại trú và hạn mức là bao nhiêu?

**Đáp án chuẩn:** Chương trình Bạc không áp dụng. Vàng 10 triệu đồng/năm, Bạch Kim 20 triệu đồng/năm, Kim Cương 40 triệu đồng/năm. Người được bảo hiểm tự chi trả 20% chi phí y tế thực tế; giới hạn 10 lần khám/năm.

**Đồ thị:** Trong An Vui Sống Khỏe, quyền lợi điều trị ngoại trú là quyền lợi bổ sung tùy chọn và chỉ được áp dụng cho các chương trình Vàng, Bạch Kim và Kim Cương. Hạn mức bảo hiểm tối đa cho quyền lợi điều trị ngoại trú là 10 triệu đồng/năm cho chương trình Vàng, 20 triệu đồng/năm cho chương trình Bạch Kim và 40 triệu đồng/năm cho chương trình Kim Cương [C2].

**Lab 4:** Chương trình Vàng, Bạch Kim và Kim Cương được mua thêm quyền lợi Điều trị Ngoại trú. Hạn mức bảo hiểm tối đa cho quyền lợi này lần lượt là 10.000.000 đồng/năm, 20.000.000 đồng/năm và 40.000.000 đồng/năm [C1][C3].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Quyền lợi điều trị ngoại trú là quyền lợi bổ sung tùy chọn. | duoc_ho_tro |
| Chỉ được áp dụng cho các chương trình Vàng, Bạch Kim và Kim Cương. | duoc_ho_tro |
| Hạn mức bảo hiểm tối đa cho quyền lợi điều trị ngoại trú là 10 triệu đồng/năm cho chương trình Vàng, 20 triệu đồng/năm cho chương trình Bạch Kim và 40 triệu đồng/năm cho chương trình Kim Cương. | duoc_ho_tro |

## G13 · multi_condition · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** Bảo Việt Nhân thọ giải quyết quyền lợi bảo hiểm An Vui Sống Khỏe trong bao lâu, và tôi phải gửi hồ sơ trong thời hạn nào?

**Đáp án chuẩn:** Bảo Việt Nhân thọ giải quyết trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ (Điều 21). Hồ sơ phải gửi trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm, không tính thời gian trì hoãn do bất khả kháng (Điều 20).

**Đồ thị:** Người yêu cầu giải quyết quyền lợi bảo hiểm phải gửi hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm tới Bảo Việt Nhân thọ trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm [C1]. Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ [C2].

**Lab 4:** Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ. Người yêu cầu giải quyết quyền lợi bảo hiểm phải gửi hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm [C2][C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Người yêu cầu giải quyết quyền lợi bảo hiểm phải gửi hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm tới Bảo Việt Nhân thọ trong thời hạn một năm kể từ ngày xảy ra sự kiện bảo hiểm. | duoc_ho_tro |
| Bảo Việt Nhân thọ có trách nhiệm giải quyết quyền lợi bảo hiểm trong vòng 30 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ. | duoc_ho_tro |

## G14 · fact · route `answer` · judge lab4 `thieu_y` → lab6 `dung_du`

**Câu hỏi:** Nếu không có yêu cầu bồi thường trong 3 năm liên tục thì An Vui Sống Khỏe giảm phí bao nhiêu?

**Đáp án chuẩn:** Giảm 15% phí bảo hiểm của quyền lợi tương ứng cho một năm tái tục tiếp theo (1 năm: 5%, 2 năm: 10%). Chỉ áp dụng tỷ lệ cao nhất, không cộng dồn (Điều 7).

**Đồ thị:** Nếu không có yêu cầu chi trả trong 3 năm liên tục, An Vui Sống Khỏe sẽ được giảm phí 15% cho một năm tái tục tiếp theo. Tỷ lệ giảm phí này áp dụng cho Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6. Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục sản phẩm bổ trợ và chỉ áp dụng tỷ lệ giảm phí cao nhất cho từng Quyền lợi bảo hiểm, không cộng dồn các tỷ lệ giảm phí.

**Lab 4:** Nếu không phát sinh yêu cầu chi trả theo Quyền lợi điều trị tương ứng trong 03 năm tham gia liên tục liền trước thời điểm xem xét, tỉ lệ giảm phí cho một năm tái tục tiếp theo là 15% phí bảo hiểm của Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6 [C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Nếu không có yêu cầu chi trả trong 3 năm liên tục, An Vui Sống Khỏe sẽ được giảm phí 15% cho một năm tái tục tiếp theo. | duoc_ho_tro |
| Tỷ lệ giảm phí này áp dụng cho Quyền lợi bảo hiểm nêu tại Khoản 6.1, 6.2, 6.3 Điều 6. | duoc_ho_tro |
| Thời điểm xem xét là ngày Bảo Việt Nhân thọ đánh giá việc tái tục sản phẩm bổ trợ và chỉ áp dụng tỷ lệ giảm phí cao nhất cho từng Quyền lợi bảo hiểm, không cộng dồn các tỷ lệ giảm phí. | duoc_ho_tro |

## G15 · exclusion · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** An Vui Sống Khỏe có chi trả điều trị đông y, châm cứu không?

**Đáp án chuẩn:** Không. Các phương pháp điều trị không phải Tây y (y học dân tộc, y học cổ truyền, châm cứu, điều trị tại khoa Đông y/Y học cổ truyền/Châm cứu) bị loại trừ theo Điều 10.18.

**Đồ thị:** Sản phẩm An Vui Sống Khỏe không chi trả các phương pháp điều trị không phải Tây y như điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ truyền, khoa Y dược cổ truyền, khoa Châm cứu của các Cơ sở y tế [C1].

**Lab 4:** Sản phẩm không chi trả các phương pháp điều trị không phải Tây y như điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ truyền, khoa Y dược cổ truyền, khoa Châm cứu của các Cơ sở y tế [C1].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Sản phẩm An Vui Sống Khỏe không chi trả các phương pháp điều trị không phải Tây y như điều trị bằng phương pháp y học dân tộc, y học cổ truyền, châm cứu hoặc điều trị tại khoa Đông y, khoa Y học cổ tr | duoc_ho_tro |

## G16 · comparison · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** So sánh thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia, An Vui Sống Khỏe và Manulife Chăm Sóc Sức Khỏe Nâng Cao.

**Đáp án chuẩn:** Bảo Việt An Gia: sinh nở sau 635 ngày, biến chứng thai sản sau 90 ngày. An Vui Sống Khỏe (Bảo Việt Nhân thọ): 270 ngày. Manulife: 270 ngày.

**Đồ thị:** Thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia là 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực [C1]. Thời gian chờ của An Vui Sống Khỏe là 270 ngày [C2]. Hiện tại chưa có thông tin về thời gian chờ của Manulife Chăm Sóc Sức Khỏe Nâng Cao trong các đoạn tài liệu được cung cấp.

**Lab 4:** Thời gian chờ quyền lợi thai sản của Bảo Việt An Gia là 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực [C2]. Thời gian chờ quyền lợi thai sản của An Vui Sống Khỏe là 270 ngày [C3]. Thời gian chờ quyền lợi thai sản của Manulife Chăm Sóc Sức Khỏe Nâng Cao cũng là 270 ngày [C4].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Thời gian chờ để được chi trả quyền lợi thai sản/sinh con của Bảo Việt An Gia là 635 ngày kể từ ngày hợp đồng bảo hiểm có hiệu lực. | duoc_ho_tro |
| Thời gian chờ của An Vui Sống Khỏe là 270 ngày. | duoc_ho_tro |
| Hiện tại chưa có thông tin về thời gian chờ của Manulife Chăm Sóc Sức Khỏe Nâng Cao trong các đoạn tài liệu được cung cấp. | duoc_ho_tro |

## G17 · comparison · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Giới hạn quyền lợi thai sản của gói Kim Cương trong Bảo Việt An Gia khác gì so với gói Kim Cương của Manulife?

**Đáp án chuẩn:** An Gia Kim Cương: tối đa 31.500.000 đồng cho một thời hạn bảo hiểm (phí bảo hiểm thai sản 5.500.000 đồng/người/năm). Manulife Kim Cương: tối đa 70 triệu đồng cho mỗi lần mang thai (gồm sinh thường, sinh mổ, biến chứng thai sản), đồng chi trả 20%.

**Đồ thị:** Giới hạn trách nhiệm tối đa cho quyền lợi bảo hiểm thai sản của gói Kim Cương trong Bảo Việt An Gia là 31.500.000 đồng mỗi năm [C1][C4]. Trong khi đó, giới hạn tối đa cho mỗi lần mang thai của gói Kim Cương trong Manulife là 70 triệu đồng, bao gồm sinh thường, sinh mổ và biến chứng thai sản [C6].

**Lab 4:** Giới hạn trách nhiệm tối đa cho quyền lợi bảo hiểm thai sản của gói Kim Cương trong Bảo Việt An Gia là 31.500.000 đồng mỗi năm [C1][C4]. Trong khi đó, gói Kim Cương của Manulife có giới hạn tối đa cho mỗi lần mang thai là 70 triệu đồng, bao gồm sinh thường, sinh mổ và biến chứng thai sản [C5].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Giới hạn trách nhiệm tối đa cho quyền lợi bảo hiểm thai sản của gói Kim Cương trong Bảo Việt An Gia là 31.500.000 đồng mỗi năm | duoc_ho_tro |
| Giới hạn tối đa cho mỗi lần mang thai của gói Kim Cương trong Manulife là 70 triệu đồng, bao gồm sinh thường, sinh mổ và biến chứng thai sản | duoc_ho_tro |

## G18 · versioning · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) của Dai-ichi Life hiện được ban hành theo văn bản nào?

**Đáp án chuẩn:** Sản phẩm được Bộ Tài chính phê chuẩn theo công văn 14187/BTC-QLBH ngày 09/10/2015 (và công văn 8361/BTC-QLBH ngày 23/06/2017, 623/BTC-QLBH ngày 16/01/2020). Quy tắc và Điều khoản hiện hành được sửa đổi và ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025.

**Đồ thị:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam [C1][C2].

**Lab 4:** Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam [C1][C2].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Quy tắc và Điều khoản sản phẩm Tử kỳ tái tục hàng tháng (2015) được ban hành theo Quyết định số 424/GD/Dai-ichi/2025 ngày 30/06/2025 của Tổng Giám đốc Công ty TNHH BHNT Dai-ichi Việt Nam. | duoc_ho_tro |

## G19 · no_diacritics · route `answer` · judge lab4 `thieu_y` → lab6 `thieu_y`

**Câu hỏi:** thoi han bao hiem cua tu ky tai tuc hang thang dai ichi la bao lau, NDBH toi da bao nhieu tuoi

**Đáp án chuẩn:** Thời hạn bảo hiểm là 01 tháng kể từ ngày hiệu lực hợp đồng và được gia hạn hàng tháng nếu hợp đồng không chấm dứt theo Điều 7 (Điều 1.21). Người được bảo hiểm từ 18 đến 75 tuổi khi tham gia; tuổi tối đa khi kết thúc thời hạn bảo hiểm là 76 tuổi (Điều 1.13).

**Đồ thị:** Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 tuổi [C1].

**Lab 4:** Thời hạn bảo hiểm của Tử kỳ tái tục hàng tháng Dai-ichi là đến khi Người được bảo hiểm đạt 76 tuổi. Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 tuổi tính theo tuổi sinh nhật vừa qua tại thời điểm tham gia bảo hiểm [C1][C2].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Tuổi tối đa của Người được bảo hiểm khi kết thúc Thời hạn bảo hiểm là 76 tuổi | duoc_ho_tro |

## G20 · no_diacritics · route `answer` · judge lab4 `dung_du` → lab6 `dung_du`

**Câu hỏi:** STBH bao hiem tai nan ca nhan trong An Gia toi da bao nhieu va phi tinh the nao

**Đáp án chuẩn:** Số tiền bảo hiểm tai nạn cá nhân tối đa 1 tỷ đồng/người/vụ (mọi chương trình). Phí bằng 0,09% STBH/năm.

**Đồ thị:** Số tiền bảo hiểm tai nạn cá nhân tối đa trong Bảo Việt An Gia là 1 tỷ đồng cho tất cả các mức ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG [C1]. Phí bảo hiểm tai nạn cá nhân được tính bằng 0,09% số tiền bảo hiểm (STBH) cho tất cả các mức này [C2].

**Lab 4:** Số tiền bảo hiểm tai nạn cá nhân tối đa trong Bảo Việt An Gia là 1 tỷ đồng cho tất cả các gói ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG [C1]. Phí bảo hiểm tai nạn cá nhân được tính bằng 0,09% số tiền bảo hiểm (STBH) cho tất cả các gói ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG [C4].

*Đường đi:* prepare → retrieve → grade_documents → generate → check_grounding → finish

| Ý | Kết luận grounding |
|---|---|
| Số tiền bảo hiểm tai nạn cá nhân tối đa trong Bảo Việt An Gia là 1 tỷ đồng cho tất cả các mức ĐỒNG, BẠC, VÀNG, BẠCH KIM, KIM CƯƠNG | duoc_ho_tro |
| Phí bảo hiểm tai nạn cá nhân được tính bằng 0,09% số tiền bảo hiểm (STBH) cho tất cả các mức này | duoc_ho_tro |

## O01 · out_of_scope · route `fallback` · judge lab4 `tu_choi` → lab6 `tu_choi`

**Câu hỏi:** Phí bảo hiểm bắt buộc trách nhiệm dân sự xe ô tô của Bảo Việt năm 2026 là bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối và chuyển tư vấn viên.

**Đồ thị:** Hiện tài liệu quy tắc, điều khoản chưa có đủ thông tin để trả lời chính xác câu hỏi này. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

**Lab 4:** Chưa có thông tin về phí bảo hiểm bắt buộc trách nhiệm dân sự xe ô tô của Bảo Việt năm 2026 trong các đoạn tài liệu đã cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Đường đi:* prepare → retrieve → grade_documents → transform_query → retrieve → grade_documents → transform_query → retrieve → grade_documents → fallback

## O02 · out_of_scope · route `fallback` · judge lab4 `tu_choi` → lab6 `tu_choi`

**Câu hỏi:** Sản phẩm An Phúc Gia Lộc của Bảo Việt Nhân thọ có quyền lợi đáo hạn bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối và chuyển tư vấn viên.

**Đồ thị:** Hiện tài liệu quy tắc, điều khoản chưa có đủ thông tin để trả lời chính xác câu hỏi này. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

**Lab 4:** Chưa có thông tin về sản phẩm An Phúc Gia Lộc và quyền lợi đáo hạn trong các đoạn tài liệu được cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Đường đi:* prepare → retrieve → grade_documents → transform_query → retrieve → grade_documents → transform_query → fallback

## O03 · out_of_scope · route `fallback` · judge lab4 `tu_choi` → lab6 `tu_choi`

**Câu hỏi:** Lãi suất tiền gửi kỳ hạn 12 tháng của Ngân hàng Bảo Việt hiện nay là bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối.

**Đồ thị:** Hiện tài liệu quy tắc, điều khoản chưa có đủ thông tin để trả lời chính xác câu hỏi này. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

**Lab 4:** Chưa có thông tin về lãi suất tiền gửi kỳ hạn 12 tháng của Ngân hàng Bảo Việt trong các đoạn tài liệu đã cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

*Đường đi:* prepare → retrieve → grade_documents → transform_query → retrieve → grade_documents → transform_query → retrieve → grade_documents → fallback

## O04 · out_of_scope · route `answer` · judge lab4 `tu_choi` → lab6 `tu_choi`

**Câu hỏi:** Hợp đồng bảo hiểm số BV-2023-004512 của tôi hiện đang ở trạng thái nào và còn bao nhiêu hạn mức?

**Đáp án chuẩn:** Tài liệu quy tắc không chứa dữ liệu hợp đồng cá nhân. Hệ thống phải từ chối và hướng dẫn tra cứu qua kênh có xác thực (tư vấn viên/cổng khách hàng).

**Đồ thị:** Chưa có thông tin về trạng thái hợp đồng bảo hiểm số BV-2023-004512 và hạn mức trong tài liệu. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

**Lab 4:** Chưa có thông tin về trạng thái hợp đồng bảo hiểm số BV-2023-004512 và hạn mức còn lại trong các đoạn tài liệu được cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ chi tiết.

*Đường đi:* prepare → retrieve → grade_documents → transform_query → retrieve → grade_documents → generate → check_grounding → finish

## O05 · out_of_scope · route `fallback` · judge lab4 `tu_choi` → lab6 `tu_choi`

**Câu hỏi:** Manulife có bán bảo hiểm cho thú cưng không, phí bao nhiêu?

**Đáp án chuẩn:** Không có thông tin trong tài liệu. Hệ thống phải từ chối.

**Đồ thị:** Hiện tài liệu quy tắc, điều khoản chưa có đủ thông tin để trả lời chính xác câu hỏi này. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ.

**Lab 4:** Chưa có thông tin về việc Manulife có bán bảo hiểm cho thú cưng hay mức phí liên quan trong các đoạn tài liệu được cung cấp. Quý khách vui lòng liên hệ tư vấn viên để được hỗ trợ chi tiết.

*Đường đi:* prepare → retrieve → grade_documents → transform_query → retrieve → grade_documents → transform_query → retrieve → grade_documents → fallback

