import streamlit as st 

def show_history_page():
    st.title("Samarqand Shahri Tarixi")
    st.write("""Samarqand – dunyodagi eng qadimiy shaharlaridan biri bo‘lib, uning tarixi 2750 yildan oshadi. Bu shahar Markaziy Osiyoning ilmiy, madaniy va savdo markazi sifatida tarixda chuqur iz qoldirgan.

Qadimgi davrlar
Samarqandning ilk poydevori eramizdan avvalgi VII asrlarda qo‘yilgan. U Sug‘diyona davlati tarkibida bo‘lib, qadimda “Marokanda” nomi bilan tanilgan. Samarqandning strategik joylashuvi uni Buyuk ipak yo‘lining muhim qismiga aylantirgan.

Aleksandr Makedonskiy davri
Eramizdan avvalgi 329-yilda Aleksandr Makedonskiy Samarqandni bosib oldi va uni o‘z imperiyasi tarkibiga qo‘shdi. U shaharni o‘zining eng go‘zal manzillaridan biri sifatida ta’riflagan.

Islom davri va Somoniylar
VIII asrda arablar tomonidan zabt etilganidan so‘ng, Samarqand Islom dunyosining muhim markaziga aylandi. X asrda Somoniylar sulolasi hukmronligi ostida shahar madaniy va iqtisodiy taraqqiyotga erishdi.

Amir Temur davri
XIV asrda Samarqand buyuk sarkarda Amir Temur tomonidan boshqarilgan. U Samarqandni o‘z imperiyasining poytaxti deb e’lon qildi va shaharni yuksak taraqqiyotga yetkazdi. Ushbu davrda Registon maydoni, Shohi Zinda majmuasi va Ulug‘bek rasadxonasi kabi inshootlar qurildi.

Rus imperiyasi va zamonaviy davr
XIX asrda Samarqand Rossiya imperiyasi tarkibiga kirdi. Bu davrda shahar sanoat va infratuzilma rivoji jihatidan o‘zgarishlarga yuz tutdi. Bugungi kunda Samarqand – O‘zbekistonning eng mashhur tarixiy va sayyohlik shaharlaridan biri.

Samarqandning bugungi ahamiyati
Hozirgi kunda Samarqand YuNESKOning Jahon merosi ro‘yxatiga kiritilgan bo‘lib, ko‘plab sayyohlarni o‘ziga jalb qiladi. Shahar boy tarixi va maftunkor me’morchiligi bilan dunyo madaniy merosining ajralmas qismi hisoblanadi."")
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
