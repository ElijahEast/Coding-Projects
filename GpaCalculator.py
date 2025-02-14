import streamlit as st

grades_total = 0
final_grade = 0

# Initialize session state for assignment list if not exists
if "assignments" not in st.session_state:
    st.session_state.assignments = [""]  # Start with one input field

if "grades" not in st.session_state:
    st.session_state.grades = [""]

# Function to add a new assignment field
def add_assignment():
    st.session_state.assignments.append("")
    st.session_state.grades.append("")  # Add a new empty input field

# Function to remove the last assignment field
def remove_assignment():
    if len(st.session_state.assignments) > 1:  # Ensure at least one input remains
        st.session_state.assignments.pop()  # Remove the last input field
    if len(st.session_state.grades) > 1:  # Ensure at least one input remains
        st.session_state.grades.pop()


c1, c2 = st.columns(2)

with c1:
    st.header("Assignment Name")

    # Display input fields dynamically from session state
    for i in range(len(st.session_state.assignments)):
        st.session_state.assignments[i] = st.text_input(f"Assignment {i+1}", value=st.session_state.assignments[i], key=f"assignment_{i}")

    # Add and Remove buttons using on_click callbacks
    st.button("(+)", on_click=add_assignment)
    st.button("(-)", on_click=remove_assignment)

with c2:
    st.header("Grade (%)")

    for i in range(len(st.session_state.assignments)):
        st.session_state.grades[i] = st.number_input(f"Grade {i+1}", min_value = 0.00, max_value = 100.00, step = 1.00, key=f"grade_{i}")

if st.button("Calculate Grade"):
    for i in range(len(st.session_state.grades)):
         grades_total += st.session_state.grades[i]
    num_of_assignments = len(st.session_state.grades)
    final_grade = grades_total/num_of_assignments
    st.text(f"Final grade: {final_grade}%")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)