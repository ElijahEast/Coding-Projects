import streamlit as st

st.title("Calculator")

# Initialize session state variables
if "num" not in st.session_state:
    st.session_state.num = "0"  # Store as a string to handle decimals
if "stored_num" not in st.session_state:
    st.session_state.stored_num = None  # None indicates no stored number
if "operation" not in st.session_state:
    st.session_state.operation = None  # Stores the operation ('+', '-', 'x', '÷')
if "new_number" not in st.session_state:
    st.session_state.new_number = False  # Flag to start a new number

def append_number_to_string(original_number, number_to_append):
    """Appends a digit or decimal point to the current number (stored as a string)."""

    if st.session_state.new_number:
        original_number = "0"  # Reset to start fresh
        st.session_state.new_number = False  # Reset flag

    if number_to_append == ".":
        if "." not in original_number:  # Ensure only one decimal point
            return original_number + "."
        else:
            return original_number  # Ignore if already has a decimal
    else:
        if original_number == "0":
            return str(number_to_append)
        else:
            return original_number + str(number_to_append)

c1, c2, c3, c4, c5, c6 = st.columns(6)

# Number buttons
with c1:
    if st.button("1"):
        st.session_state.num = append_number_to_string(st.session_state.num, 1)
    if st.button("4"):
        st.session_state.num = append_number_to_string(st.session_state.num, 4)
    if st.button("7"):
        st.session_state.num = append_number_to_string(st.session_state.num, 7)

with c2:
    if st.button("2"):
        st.session_state.num = append_number_to_string(st.session_state.num, 2)
    if st.button("5"):
        st.session_state.num = append_number_to_string(st.session_state.num, 5)
    if st.button("8"):
        st.session_state.num = append_number_to_string(st.session_state.num, 8)
    if st.button("0"):
        st.session_state.num = append_number_to_string(st.session_state.num, 0)

with c3:
    if st.button("3"):
        st.session_state.num = append_number_to_string(st.session_state.num, 3)
    if st.button("6"):
        st.session_state.num = append_number_to_string(st.session_state.num, 6)
    if st.button("9"):
        st.session_state.num = append_number_to_string(st.session_state.num, 9)
    if st.button("."):
        st.session_state.num = append_number_to_string(st.session_state.num, ".")

# Backspace
with c4:
    if st.button("←"):
        if st.session_state.num == "Error":
            st.session_state.num = 0
        else:
            st.session_state.num = st.session_state.num[:-1] if len(st.session_state.num) > 1 else "0"
    if st.button("C"):
        st.session_state.num = "0"
        st.session_state.stored_num = None
    if st.button("="):
        if st.session_state.operation and st.session_state.stored_num is not None:
            try:
                if st.session_state.operation == "+":
                    st.session_state.num = str(st.session_state.stored_num + float(st.session_state.num))
                elif st.session_state.operation == "-":
                    st.session_state.num = str(st.session_state.stored_num - float(st.session_state.num))
                elif st.session_state.operation == "x":
                    st.session_state.num = str(st.session_state.stored_num * float(st.session_state.num))
                elif st.session_state.operation == "÷":
                    if float(st.session_state.num) == 0:
                        st.session_state.num = "Error"  # Avoid division by zero
                    else:
                        st.session_state.num = str(st.session_state.stored_num / float(st.session_state.num))
            except ValueError:
                st.session_state.num = "Error"

            # Reset operation
            st.session_state.stored_num = None
            st.session_state.operation = None
            st.session_state.new_number = True  # Allow new input
            if st.session_state.num != "Error":
                if float(st.session_state.num) % 1 == 0:
                    st.session_state.num = st.session_state.num[:-2] if len(st.session_state.num) > 1 else "0"

# Operations
with c5:
    if st.button("(+)"):
        st.session_state.stored_num = float(st.session_state.num)  # Convert to float
        st.session_state.num = "0"
        st.session_state.operation = "+"
        st.session_state.new_number = True  # Expect new number input

    if st.button("(-)"):
        st.session_state.stored_num = float(st.session_state.num)  # Convert to float
        st.session_state.num = "0"
        st.session_state.operation = "-"
        st.session_state.new_number = True  # Expect new number input
        
    if st.button("(x)"):
        st.session_state.stored_num = float(st.session_state.num)  # Convert to float
        st.session_state.num = "0"
        st.session_state.operation = "x"
        st.session_state.new_number = True  # Expect new number input

    if st.button("(÷)"):
        st.session_state.stored_num = float(st.session_state.num)  # Convert to float
        st.session_state.num = "0"
        st.session_state.operation = "÷"
        st.session_state.new_number = True  # Expect new number input


# Display current numbers and operation
st.text(f"Current number: {st.session_state.num}")
st.text(f"Stored number: {st.session_state.stored_num if st.session_state.stored_num is not None else 'None'} (for operation: {st.session_state.operation})")