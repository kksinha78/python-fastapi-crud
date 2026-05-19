from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
# to run use command : fastapi dev myapi.py

#So endpoint creation means:“Defining a URL path and telling FastAPI which function should execute when that URL is called.”
app = FastAPI()
students = {
    1:{
        "name" : "Shreyansh",
        "Age": 8,
        "year"  : "year 12"
    }
}

class Student(BaseModel):
    name : str
    age  : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None


# amazon.com/create-user
@app.get("/")
def index():
    return {"name" : "Krishna"}

# @app.get("/get-student/{student_id}/{student_name}") #fastAPI is helping you create a URL (API endpoint) that users or applications can call.This line creates the endpoint
# def get_student(student_id:int,student_name : str):
#     return {
#         "student_id" : student_id,
#         "student_name" : student_name
#     }
#using Path parameter
@app.get("/get-student/{student_id}") #fastAPI is helping you create a URL (API endpoint) that users or applications can call.This line creates the endpoint
def get_student(student_id:int=Path(description="ID of student",gt =0,lt=3)):
    return  students[student_id]

#using query paramter
#google.com/results?search=Python

@app.get("/get-by-name")
def get_student(name:Optional[str]=None): # if str = None then it will not be required in 
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"data":"No data found"}

#combining path and query parameters together

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id : int,name:Optional[str]=None,test :Optional[int]=None): # if str = None then it will not be required in 
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"data":"No data found"}

#request body and Post method
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"error" : "Student Exhist"}
    students[student_id] = student
    return students[student_id]

#Put method
@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"error" : "Student ID does not exist"}
    if student.name != None:
        students[student_id].name= student.name
    if student.age != None:
        students[student_id].age= student.age
    if student.year != None:
        students[student_id].year= student.year
   
    return students[student_id]

#Delete method
@app.delete("/delete-student/{student_id}")
def update_student(student_id:int):
    if student_id not in students:
        return {"error" : "Student ID does not exist"}
    del students[student_id]
    return {"Message" : " Student deleted sucessfully"}


