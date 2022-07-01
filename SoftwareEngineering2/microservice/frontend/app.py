# Import the required packages.
import streamlit as st
from api import *

# Set the configuration.
st.set_page_config(
    page_title = "Student Information System | Monolithic",
    initial_sidebar_state = "expanded",
    menu_items = None 
)


# Title of the page.    
st.title("Student Information System | Monolithic")


# Have the space for the 3 buttons.
col1, col2, col3, _ = st.columns([1, 1, 1, 5])
with col1:
    students = st.button("Students")
with col2:
    subjects = st.button("Subjects")
with col3:
    marks = st.button("Marks")


# Tell streamlit which screen to show.
if "page" not in st.session_state or students:
    st.session_state["page"] = "students"
if subjects:
    st.session_state["page"] = "subjects"
if marks:
    st.session_state["page"] = "marks"


# What to show if 'Subject' is selected.
if st.session_state.page == "subjects":
    # Display what is already saved in the database.
    st.table(get_subjects())

    # Add a new record.
    with st.sidebar.form("subject-data", clear_on_submit=True):
        subject = st.text_input("Subject Name")
        upload = st.form_submit_button("Add Subject")
        st.write("")

        if upload and subject:
            insert_subject(subject)
            st.experimental_rerun() # Refresh the page to show the newly added item.


# What to show if 'Marks' is selected.
elif st.session_state.page == "marks":
    st.table(get_marks())

    with st.sidebar.form("marks-data", clear_on_submit=True):
        student = st.selectbox("Student", get_students().Student)
        subject = st.selectbox("Subject", get_subjects().Subject)
        marks = st.number_input("Marks")
        upload = st.form_submit_button("Add Marks")
        st.write("")

        if upload and student and subject and marks:
            insert_marks(student, subject, int(marks))
            st.experimental_rerun()


# What to show if somethign else is selected.
else:
    st.table(get_students())

    with st.sidebar.form("student-data", clear_on_submit=True):
        student = st.text_input("Student Name")
        age = st.text_input("Student Age")
        upload = st.form_submit_button("Add Student")
        st.write("")

        if upload and student and age:
            insert_student(student, age)
            st.experimental_rerun()
