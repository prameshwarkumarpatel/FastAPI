from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

add = []


class TodoList(BaseModel):
    name: str
    roll: int
    email: str


# CREATE
@app.post("/user")
def create_user(user: TodoList):
    todo_id = len(add) + 1

    new_user = {
        "todo_id": todo_id,
        "name": user.name,
        "roll": user.roll,
        "email": user.email
    }

    add.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }


# READ
@app.get("/user/{todo_id}")
def user_get(todo_id: int):
    for user in add:
        if user["todo_id"] == todo_id:
            return {
                "message": "User found",
                "user": user
            }

    return {
        "message": "User not found"
    }


# UPDATE
@app.put("/user/{todo_id}")
def user_update(todo_id: int, user: TodoList):
    for index, existing_user in enumerate(add):
        if existing_user["todo_id"] == todo_id:

            updated_user = {
                "todo_id": todo_id,
                "name": user.name,
                "roll": user.roll,
                "email": user.email
            }

            add[index] = updated_user

            return {
                "message": "User updated successfully",
                "user": updated_user
            }

    return {
        "message": "User not found"
    }


# DELETE
@app.delete("/user/{todo_id}")
def user_delete(todo_id: int):
    for index, user in enumerate(add):
        if user["todo_id"] == todo_id:
            deleted_user = add.pop(index)

            return {
                "message": "User deleted successfully",
                "user": deleted_user
            }

    return {
        "message": "User not found"
    }