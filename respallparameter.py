from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Users(BaseModel):
    name: str
    age: int
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    name: str
    age: int
    username: str
    email: str


@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "name": "pawan kumar",
        "age": "two",
        "username": "pawan123",
        "email": "pawan@example.com",
        "password": "password123"
    }