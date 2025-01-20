import streamlit as st
import random
import string
import pyperclip

# Define available characters for the password
characters = string.ascii_letters + string.digits + string.punctuation

# Streamlit app layout
st.title("Random Password Generator")
st.write("How many characters do you want in your password?")

# Input for the number of characters in the password
num = st.number_input("Enter the number of characters", min_value=1, max_value=16, value=12, step=1)

# Ensure session state for the password
if "password" not in st.session_state:
    st.session_state.password = ""

# Generate password on button click
if st.button("Generate Password"):
    st.session_state.password = "".join(random.choice(characters) for _ in range(num))
    st.write(f"Your password is: `{st.session_state.password}`")

# Add a button to copy the password
if st.session_state.password:  # Only show the button if a password is generated
    if st.button("Copy Password"):
        pyperclip.copy(st.session_state.password)
        st.success("Password copied to clipboard!")