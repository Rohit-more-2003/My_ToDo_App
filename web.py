import streamlit as st
import functions

todos = functions.get_todos()

def add_todo(): #to add new_todo
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

#if sequence of statements changed the same will happen with the web page
#i.e. title after subheader then same change with web page
st.title("My To-Do App")            #for title of web page
st.subheader("This is my todo app") #for subheader of web page
st.write("This app is to increase your productivity") #for content of web page

for index, todo in enumerate(todos):
    todo = todo.strip()

    checkbox = st.checkbox(todo, key=todo) #for creating checkboxes
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo") #for creating an input box

#Any time the web page is refreshed, the code is rerun

#st.session_state