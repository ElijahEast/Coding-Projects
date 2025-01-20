import streamlit as st
import random
import string

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