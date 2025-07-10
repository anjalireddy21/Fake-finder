import streamlit as st
from model import detect_fake_text

st.set_page_config(page_title="FakeFinder", page_icon="🕵️")
st.title("🕵️ FakeFinder – AI Fake Content Detector")
st.write("Paste a news headline, claim, or message below. This tool will analyze it using an AI model.")

user_input = st.text_area("📰 Enter text to verify:", height=150)

if st.button("Check Authenticity"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            label, score = detect_fake_text(user_input)
            if label == "FAKE":
                st.error(f"🚨 Likely Fake – Confidence: {score:.2f}")
            else:
                st.success(f"✅ Possibly Real – Confidence: {score:.2f}")
    else:
        st.warning("Please enter some text.")
