import streamlit as st

st.set_page_config(page_title="APP CHO VAY ONLINE KHÁCH HÀNG CÁ NHÂN_ĐỀ TÀI 4_NGUYỄN NGỌC MINH THƯ", page_icon="🏦")

st.title("🏦 Ứng dụng thẩm định tín dụng cá nhân")

# Nhập dữ liệu
STV = st.number_input("Nhập số tiền muốn vay (triệu đồng)", min_value=0.0)

TGV = st.number_input("Nhập thời gian vay (năm)", min_value=0.0)

LSV = st.number_input("Nhập lãi suất cho vay (dạng thập phân, ví dụ 0.12)", min_value=0.0)

TN = st.number_input("Nhập thu nhập hàng tháng (triệu đồng)", min_value=0.0)

SNTGD = st.number_input("Nhập số người trong gia đình", min_value=0.0)

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ mỗi tháng (triệu đồng)",
    min_value=0.0
)

GTTSDB = st.number_input(
    "Nhập giá trị tài sản đảm bảo (triệu đồng)",
    min_value=0.0
)

TUOI = st.number_input(
    "Nhập tuổi của khách hàng",
    min_value=18,
    max_value=100
)

if st.button("ĐÁNH GIÁ HỒ SƠ"):
    CPSH = 5

    PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))

    TNKD = TN - SNTGD * CPSH

    if TNKD <= 0:
        st.error("Thu nhập khả dụng không hợp lệ!")
    elif GTTSDB <= 0:
        st.error("Giá trị tài sản đảm bảo phải lớn hơn 0!")
    else:
        DTI = (PTMC + PTMM) / TNKD
        LTV = STV / GTTSDB

        st.subheader("Kết quả thẩm định")

        st.write(f"**DTI:** {DTI*100:.2f}%")
        st.write(f"**LTV:** {LTV*100:.2f}%")

        if DTI <= 0.7 and LTV <= 0.7 and 18 <= TUOI <= 70:
            st.success("✅ ĐƯỢC CHO VAY")
        else:
            st.error("❌ KHÔNG ĐƯỢC CHO VAY")
