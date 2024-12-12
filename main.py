import streamlit as st 

def show_history_page():
    st.title("Samarqand Shahri Tarixi")
    st.write("Samarqand - Markaziy Osiyodagi eng qadimiy shaharlardan biri...")
    st.image("images/samarqand_history.jpg", caption="Samarqandning qadimiy surati")

# Page 2: Mashhur obidalar
def show_landmarks_page():
    st.title("Samarqandning Mashhur Obidalari")
    st.write("Samarqandda ko‘plab tarixiy obidalar mavjud, jumladan:")
    st.image("images/registan.jpg", caption="Registon maydoni")
    st.image("images/shohi_zinda.jpg", caption="Shohi Zinda majmuasi")

# Navigatsiya
page = st.sidebar.selectbox("Sahifani tanlang", ["Samarqand tarixi", "Mashhur obidalar"])

if page == "Samarqand tarixi":
    show_history_page()
elif page == "Mashhur obidalar":
    show_landmarks_page()
