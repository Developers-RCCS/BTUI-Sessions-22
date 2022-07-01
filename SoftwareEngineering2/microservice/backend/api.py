from fastapi import FastAPI
from data import *

app = FastAPI()


@app.get("/")
def read_root():
    return "Hi! API service is running"

@app.get("/students")
def fetch_students():
    return get_students()

@app.post("/student")
def post_student(name, age):
    return insert_student(name, age)

    
@app.get("/subjects")
def fetch_subjects():
    return get_subjects()
    
@app.post("/subject")
def post_subject(subject):
    return insert_subject(subject)


@app.get("/marks")
def fetch_marks():
    return get_marks()
    
@app.post("/mark")
def post_mark(student, subject, marks):
    return insert_marks(student, subject, marks)
