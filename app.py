import streamlit as st
from groq import Groq

st.set_page_config(page_title="PLACEMENT PRACTICE", layout="centered")
st.title("AI ASSISTANT INTERVIEWER")
st.caption("Practice and prepare for your interviews")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API Key is missing. Add it in Advanced settings.")
    st.stop()
