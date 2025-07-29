import streamlit as st
from utils.extract_pdf import extract_text_from_pdf

st.set_page_config(page_title="ProtoFormAI", layout="centered")
st.title("ProtoFormAI — Protocol to CRF Generator")

uploaded_file = st.file_uploader("Upload a Clinical Trial Protocol (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting protocol text..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Protocol Text")
    st.text_area("View Extracted Text", text[:3000], height=400)
