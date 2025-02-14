import streamlit as st

st.title("Word Counter (press enter to update)")

txt = st.text_input("Paste your text")

words = len(txt.split())  # Automatically handles multiple spaces

st.text(f"{words} word(s)")