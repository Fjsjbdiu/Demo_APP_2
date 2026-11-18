import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="PLACEMENT PRACTICE",
    layout="centered",
)

st.title("AI ASSISTANT INTERVIEWER")
st.caption("Practice and prepare for your interviews")

try:
    api_key = st.secrets["GROQ_API_KEY"]
except (KeyError, FileNotFoundError):
    st.error("GROQ_API_KEY is missing. Add it under App Settings → Secrets.")
    st.stop()

if not api_key:
    st.error("GROQ_API_KEY cannot be empty.")
    st.stop()

try:
    client = Groq(api_key=api_key)
except Exception as exc:
    st.error(f"Failed to initialize Groq: {exc}")
    st.stop()
