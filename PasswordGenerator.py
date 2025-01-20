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

# Add a button to copy the password to the clipboard
if st.session_state.password:  # Only show the button if a password is generated
    # Add an HTML-based copy button
    copy_code = f"""
        <input type="text" value="{st.session_state.password}" id="passwordField" readonly>
        <button onclick="copyToClipboard()" style="margin-left: 10px;">Copy Password</button>
        <script>
        function copyToClipboard() {{
            var copyText = document.getElementById("passwordField");
            copyText.select();
            copyText.setSelectionRange(0, 99999); /* For mobile devices */
            navigator.clipboard.writeText(copyText.value);
            alert("Password copied to clipboard!");
        }}
        </script>
    """
    st.markdown(copy_code, unsafe_allow_html=True)
