import streamlit as st
import random
import os

# Title for the app
st.title("Random Number Generator")

# Description
st.write("Generate a random number within your chosen range!")
st.write("Current working directory:", os.getcwd())

# Input fields for the range
min_value = st.number_input("Enter the minimum value", value=0, step=1)
max_value = st.number_input("Enter the maximum value", value=100, step=1)

# Button to generate a random number
if st.button("Generate Random Number"):
    if min_value >= max_value:
        st.error("Minimum value must be less than the maximum value!")
    else:
        random_number = random.randint(min_value, max_value)
        st.success(f"Your random number is: {random_number}")
