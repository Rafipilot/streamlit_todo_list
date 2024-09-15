import streamlit as st

st.title("Homework")

# Initialize the lists and expanded state in session_state if they don't exist
if 'todo' not in st.session_state:
    st.session_state.todo = []

if 'doing' not in st.session_state:
    st.session_state.doing = []

if 'done' not in st.session_state:
    st.session_state.done = []

if 'expanded_item' not in st.session_state:
    st.session_state.expanded_item = None  # Track the expanded state for item options




# Function to toggle the expanded state for an item
def toggle_expanded_item(index):
    if st.session_state.expanded_item == index:
        st.session_state.expanded_item = None  # Collapse the options if already expanded
    else:
        st.session_state.expanded_item = index  # Expand the options for this item

# Create columns
todo_col, doing_col, done_col = st.columns([9,9,3])

# Todo Column
with todo_col:
    st.write("Todo")
    
    # Display the todo list
    for i in range(len(st.session_state.todo)):
        col1, col2 = st.columns([3, 1])  # Adjust column sizes
        item = st.session_state.todo[i]  # Correctly access the item
        
        with col1:
            st.write(item)  # Display the item
        
        with col2:
            # "More" button to expand/collapse options
            if st.button("⋮", key=f'more_todo_{i}'):
                toggle_expanded_item(f'todo_{i}')
        
        # Show additional options if the "more" button is clicked
        if st.session_state.expanded_item == f'todo_{i}':
            st.write("Options:")
            delete_col, move_col, rename_col = st.columns(3)
            
            # Delete button
            with delete_col:
                if st.button("Delete", key=f'delete_todo_{i}'):
                    st.session_state.todo.pop(i)
                    st.rerun()  # Rerun the app to reflect changes
            
            # Move button (e.g., move to 'doing')
            with move_col:
                if st.button("Move", key=f'move_todo_{i}'):
                    st.session_state.doing.append(item)
                    st.session_state.todo.pop(i)
                    st.rerun()  # Rerun the app to reflect changes

            # Rename button
            with rename_col:
                if st.button("Rename", key=f'rename_todo_{i}'):
                    new_name = st.text_input(f"Rename {item}:", key=f'rename_input_{i}')
                    if new_name:
                        print(new_name)
                        st.session_state.todo[i] = new_name
                        st.rerun()  # Rerun to update the renamed item

    # Input to add new items to the todo list
    input = st.chat_input("Add more: ")
    if input:
        st.session_state.todo.append(input)
        st.rerun()

# Doing Column (similar logic for "Doing" column)
with doing_col:
    st.write("Doing")
    for i in range(len(st.session_state.doing)):
        col1, col2 = st.columns([3, 1])
        item = st.session_state.doing[i]
        
        with col1:
            st.write(item)
        
        with col2:
            if st.button("⋮", key=f'more_doing_{i}'):
                toggle_expanded_item(f'doing_{i}')
        
        if st.session_state.expanded_item == f'doing_{i}':
            st.write("Options:")
            delete_col, move_col, rename_col = st.columns(3)
            
            with delete_col:
                if st.button("Delete", key=f'delete_doing_{i}'):
                    st.session_state.doing.pop(i)
                    st.rerun()

            with move_col:
                if st.button("Move", key=f'move_doing_{i}'):
                    st.session_state.done.append(item)
                    st.session_state.doing.pop(i)
                    st.rerun()

            with rename_col:
                if st.button("Rename", key=f'rename_doing_{i}'):
                    new_name = st.text_input(f"Rename {item}:", key=f'rename_input_doing_{i}')
                    if new_name:
                        st.session_state.doing[i] = new_name
                        st.rerun()

# Done Column (similar logic for "Done" column)
with done_col:
    st.write("Done")
    for i in range(len(st.session_state.done)):
        col1, col2 = st.columns([3, 1])
        item = st.session_state.done[i]
        
        with col1:
            st.write(item)
        
        with col2:
            if st.button("⋮", key=f'more_done_{i}'):
                toggle_expanded_item(f'done_{i}')
        
        if st.session_state.expanded_item == f'done_{i}':
            st.write("Options:")
            delete_col, rename_col = st.columns(2)
            
            with delete_col:
                if st.button("Delete", key=f'delete_done_{i}'):
                    st.session_state.done.pop(i)
                    st.rerun()

            with rename_col:
                if st.button("Rename", key=f'rename_done_{i}'):
                    new_name = st.text_input(f"Rename {item}:", key=f'rename_input_done_{i}')
                    if new_name:
                        st.session_state.done[i] = new_name
                        st.rerun()
