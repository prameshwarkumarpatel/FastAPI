from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

pawan = []


class User(BaseModel):
    name: str
    age: int
    email: str
    result: bool


@app.post("/user")
def create_user(user: User):
    user_id = len(pawan) + 1

    new_user = {
        "user_id": user_id,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "result": user.result
    }

    pawan.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }