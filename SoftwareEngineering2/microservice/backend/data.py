# Import the required packages.
import mysql.connector
import pandas as pd


# Connect to our database.
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="students" #Ignore prior to creating the database.
)
cursor = connection.cursor()

# Adding a new student.
def insert_student(name, age):
    _sql = "INSERT INTO students (StudentName, StudentAge) VALUES (%s, %s)"
    _val = (name, age)
    cursor.execute(_sql, _val)
    connection.commit()
    

def insert_subject(subject):
    _sql = f"INSERT INTO subjects (Subjectname) VALUES ('{subject}')"
    cursor.execute(_sql)
    connection.commit()      
    

def insert_marks(student, subject, marks):
    _sql = "INSERT INTO marks (StudentName, Subjectname, Marks) VALUES (%s, %s, %s)"
    _val = (student, subject, marks)
    cursor.execute(_sql, _val)
    connection.commit()

# Getting all the students.
def get_students():
    _sql = "SELECT * FROM students"
    cursor.execute(_sql)

    _result = []
    for i in cursor.fetchall():
        _result.append((i[1], i[2]))
    
    return _result

def get_subjects():
    _sql = "SELECT * FROM subjects"
    cursor.execute(_sql)

    _result = []
    for i in cursor.fetchall():
        _result.append((i[1]))
    
    return _result

def get_marks():
    _sql = "SELECT * FROM marks"
    cursor.execute(_sql)

    _result = []
    for i in cursor.fetchall():
        _result.append((i[1], i[2], i[3]))
    
    return _result
