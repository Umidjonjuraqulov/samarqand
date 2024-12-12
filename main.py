import streamlit as st 

def show_history_page():
    st.title("Samarqand Shahri Tarixi")
    st.write("Samarqand - Markaziy Osiyodagi eng qadimiy shaharlardan biri...")
    st.image("https://avatars.mds.yandex.net/i?id=dbe15ea2c155b98a9503f6ef8c4b213c546962dd-4236999-images-thumbs&n=13", caption="Samarqandning qadimiy surati")

# Page 2: Mashhur obidalar
def show_landmarks_page():
    st.title("Samarqandning Mashhur Obidalari")
    st.write("Samarqandda ko‘plab tarixiy obidalar mavjud, jumladan:")
    st.image("https://7d9e88a8-f178-4098-bea5-48d960920605.selcdn.net/55526e78-4c2d-44d5-b974-99af51df9864/-/resize/x600/-/quality/smart_retina/", caption="Registon maydoni")
    st.image("https://avatars.mds.yandex.net/i?id=3dd3885bab35bd5272dceedff69be4e4_l-12605172-images-thumbs&n=13", caption="Shohi Zinda majmuasi")

# Navigatsiya
page = st.sidebar.selectbox("Sahifani tanlang", ["Samarqand tarixi", "Mashhur obidalar"])

if page == "Samarqand tarixi":
    show_history_page()
elif page == "Mashhur obidalar":
    show_landmarks_page()
