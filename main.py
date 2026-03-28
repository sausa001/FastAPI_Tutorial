from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": "Welcome to FastAPI! Jyoti is learning FastAPI. Cool!"}

@app.get("/greet")
def greet():
    return {"Message": "That's great! Keep learning FastAPI, Jyoti!"}


#Path Parameter
# @app.get("/greet/{name}")
# def greet_name(name: str):
#     return {"Message": f"Hello, {name}! Welcome to FastAPI!"}

#Query Parameter
# @app.get("/greet/{name}")
# def greet_name(name: str, age: int):
#     return {"Message": f"Hello, {name}! Welcome to FastAPI! You are {age} years old"}


#Optional Query Parameter
# @app.get("/greet/{name}")
# def greet_name(name: str, age: Optional[int] = None):
#     return {"Message": f"Hello, {name}! Welcome to FastAPI! You are {age} years old"}


#Multiple Query Parameter
@app.get("/greet/")
def greet_name(name: str, age: Optional[int] = None):
    return {"Message": f"Hello, {name}! Welcome to FastAPI! You are {age} years old"}


#Post Request
class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
        return {
           "name": student.name,
           "age": student.age,
           "roll": student.roll
        }