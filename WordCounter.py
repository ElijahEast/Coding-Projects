import streamlit as st

txt = st.text_input("Paste your text")

words = len(txt.split())  # Automatically handles multiple spaces

st.text(f"{words} word(s)")