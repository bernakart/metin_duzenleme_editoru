import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompt import create_prompt

# .env dosyasını yükle
load_dotenv()
default_api_key = os.getenv("OPENAI_API_KEY")

st.title("📝 Yapay Zeka Yazı Editörü")

# API Key Seçimi
use_custom_key = st.checkbox("🔐 Kendi OpenAI API anahtarımı girmek istiyorum")
if use_custom_key:
    user_api_key = st.text_input("API Anahtarınızı giriniz:", type="password")
    api_key = user_api_key if user_api_key else None
else:
    api_key = default_api_key

client = OpenAI(api_key=api_key) if api_key else None

metin = st.text_area("✍️ Metni Giriniz:", height=200)

tarz_mesajlari = {
    "kurumsal": "Metni profesyonel ve resmi algılanan bir dil ile yeniden yaz.",
    "akademik": "Metni akademik, tarafsız ve bilimsel bir dille yeniden yaz.",
    "samimi": "Metni doğal, sıcak ve arkadaşça bir dille yeniden yaz.",
    "mail": "Metni düzgün, resmi ve etkili bir e-posta haline getir.",
    "hicbiri": "Metni olduğu gibi koru, yalnızca çeviri, başlık ve özet işlemleri yap."
}
dil_mesajlari = {
    "türkce": "Metni Türkçe olarak sun.",
    "ingilizce": "Metni İngilizce olarak sun.",
    "almanca": "Metni Almanca olarak sun.",
    "diğer": "Metni kullanıcı tarafından belirtilen farklı bir dile çevir."
}

tarz = st.selectbox("🎯 Yazı Tarzı:", ["SEÇİNİZ"] + list(tarz_mesajlari.keys()))
dil = st.selectbox("🌐 Hedef Dil:", ["SEÇİNİZ"] + list(dil_mesajlari.keys()))
baslik = st.checkbox("🏷️ Başlık eklensin")
ozet = st.checkbox("✂️ Özetlensin")

if st.button("✅ Metni Düzenle"):
    if not api_key:
        st.error("API anahtarı tanımlı değil.")
    elif not metin.strip():
        st.warning("Lütfen metin giriniz.")
    elif tarz == "SEÇİNİZ":
        st.warning("Lütfen bir yazı tarzı seçiniz.")
    elif dil == "SEÇİNİZ":
        st.warning("Lütfen bir hedef dil seçiniz.")
    else:
        # Kendi fonksiyonunu kullan
        sistem_prompt = create_prompt(dil_mesajlari, tarz_mesajlari, dil, tarz, baslik, ozet)
        mesajlar = [
            {"role": "system", "content": sistem_prompt},
            {"role": "user", "content": metin}
        ]
        try:
            cevap = client.chat.completions.create(
                model="gpt-4o",
                messages=mesajlar,
                temperature=0.7,
                max_tokens=800
            )
            st.subheader("📄 Düzenlenmiş Metin:")
            st.text_area("", cevap.choices[0].message.content.strip(), height=300)
        except Exception as e:
            st.error(f"Hata: {str(e)}")
