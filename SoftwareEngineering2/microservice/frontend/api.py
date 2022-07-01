from urllib import response
from requests import get, post
import pandas as pd


# Instead of interacting directly with the database, we have to work with the API now!

def get_students():
    response = get("http://127.0.0.1:8000/students")
    return pd.DataFrame(response.json(), columns=["Student", "Age"])

def get_subjects():
    response = get("http://127.0.0.1:8000/subjects")
    return pd.DataFrame(response.json(), columns=["Subject"])
    
def get_marks():
    response = get("http://127.0.0.1:8000/marks")
    return pd.DataFrame(response.json(), columns=["Student", "Subject", "Marks"])

def insert_student(name, age):
    return post(f"http://127.0.0.1:8000/student?name={name}&age={age}")

def insert_subject(subject):
    return post(f"http://127.0.0.1:8000/subject?subject={subject}")
    
def insert_marks(student, subject, marks):
    return post(f"http://127.0.0.1:8000/mark?student={student}&subject={subject}&marks={marks}")
