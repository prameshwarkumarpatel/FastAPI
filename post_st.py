from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

pawan = []


class User(BaseModel):
    name: str
    age: int
    email: str
    result: bool


# CREATE
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


# READ BY USER ID
@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in pawan:
        if user["user_id"] == user_id:
            return user

    return {
        "message": "User not found"
    }


# READ BY EMAIL
@app.get("/user")
def get_user_by_email(email: str):
    for user in pawan:
        if user["email"] == email:
            return user

    return {
        "message": "User not found"
    }
@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    for existing_user in pawan:
        if existing_user["user_id"]==user_id:
            existing_user["name"] = user.name
            existing_user["age"]= user.age
            existing_user["email"] = user.email
            existing_user["result"] = user.result
            return {
                "message": "user updated successfully",
                "user": existing_user
            }
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for existing_user in pawan:
        if existing_user["user_id"]==user_id:
            pawan.remove(existing_user)
            return {
                "message": "user deleted successfully",
                "user": existing_user
            }