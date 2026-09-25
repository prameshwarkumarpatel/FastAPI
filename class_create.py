from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str
    rollno: int


@app.post("/user")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "rollno": user.rollno
    }