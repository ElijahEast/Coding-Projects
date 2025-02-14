import streamlit as st

if "number_list" not in st.session_state:
    st.session_state.number_list = []

st.title("Modifiable Number List")

num_type = st.selectbox("Would you like the list to be made of integers, decimal numbers, or both?", ("Integers", "Decimals", "Both"))

def convert_list(num_type):
    if num_type == "Integers":
        st.session_state.number_list = [int(num) for num in st.session_state.number_list]
    elif num_type == "Decimals":
        st.session_state.number_list = [float(num) for num in st.session_state.number_list]
    else:
        pass

convert_list(num_type)

new_number = st.number_input("Add a number to the list: ", step=1 if num_type == "Integers" else 1.0)

if st.button("Add number"):
    if num_type == "Both":
        if new_number == int(new_number):
            new_number = int(new_number)
    st.session_state.number_list.append(new_number)
    st.success(f"Added {new_number} to list")

remove_index = st.number_input("Type in the index (position starting from 0) of the number you want to remove: ", min_value = 0, max_value = len(st.session_state.number_list)-1 if st.session_state.number_list else 0, step=1, key = "remove_index")

if st.button("Remove number"):
    if 0 <= remove_index < len(st.session_state.number_list):
        removed_number = st.session_state.number_list.pop(remove_index)
        st.success(f"Removed {removed_number} from list!")
    else:
        st.error("Invalid index")

st.write("### Current number list: ")

sorted_list = sorted(st.session_state.number_list)
reverse_sorted_list = sorted(st.session_state.number_list, reverse= True)
sort = st.selectbox("How would you like the list to be sorted?", ("Unsorted", "Least to greatest", "Greatest to least"))
if sort == "Least to greatest":
    st.write(sorted_list)
    final_list = sorted_list
    
elif sort == "Greatest to least":
    st.write(reverse_sorted_list)
    final_list = reverse_sorted_list

else: 
    st.write(st.session_state.number_list)
    final_list = st.session_state.number_list

list_as_string = ", ".join(map(str, final_list))

# Add a copy-to-clipboard button
st.write("### Copy the List:")
st.code(list_as_string, language="text")

