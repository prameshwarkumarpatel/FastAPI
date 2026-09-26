from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    name: str
    age: int
    email: str
    result: bool


# CREATE
@app.post("/user")
def create_user(user: User):
    user_id = len(users) + 1

    new_user = {
        "user_id": user_id,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "result": user.result
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }


# READ ALL USERS
@app.get("/user")
def get_users():
    return {
        "users": users
    }


# READ ONE USER
@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["user_id"] == user_id:
            return user

    return {
        "message": "User not found"
    }


# UPDATE
@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    for existing_user in users:
        if existing_user["user_id"] == user_id:
            existing_user["name"] = user.name
            existing_user["age"] = user.age
            existing_user["email"] = user.email
            existing_user["result"] = user.result

            return {
                "message": "User updated successfully",
                "user": existing_user
            }

    return {
        "message": "User not found"
    }


# DELETE
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["user_id"] == user_id:
            users.remove(user)

            return {
                "message": "User deleted successfully",
                "user": user
            }

    return {
        "message": "User not found"
    }