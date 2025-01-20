import streamlit as st
import pyperclip

# Text to copy
text_to_copy = "This text is copied automatically!"

# Streamlit button to trigger the copy
if st.button("Copy Text"):
    pyperclip.copy(text_to_copy)
    st.success("Text copied to clipboard!")