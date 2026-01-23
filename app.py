from image_generation.image_fetcher import fetch_image_url
import streamlit as st
from nlp.keyword_extractor import extract_keywords
from ui.styles import apply_dyslexia_style

st.set_page_config(page_title="EduLex", layout="centered")

st.markdown(apply_dyslexia_style(), unsafe_allow_html=True)

st.title("📘 EduLex")
st.subheader("AI-Driven Multimedia Learning for Dyslexic Students")

st.write("Enter a learning prompt. EduLex will break it into easy-to-understand concepts.")

user_input = st.text_input(
    "Learning prompt",
    placeholder="Example: A barber cutting a man's hair"
)

if user_input:
    keywords = extract_keywords(user_input)

    st.markdown("### 🔑 Key Concepts Identified")
    cols = st.columns(2)

    for idx, kw in enumerate(keywords):
        with cols[idx % 2]:
            st.markdown(f"**{kw.capitalize()}**")

            image_url = fetch_image_url(kw)
            st.image(image_url, use_container_width=True)


