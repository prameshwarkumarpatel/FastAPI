from fastapi import FastAPI

app = FastAPI()

users = []


# GET - Get all users
@app.get("/user")
def get_users():
    return {
        "message": "Users fetched successfully",
        "data": users
    }


# GET - Get one user
@app.get("/user/{user_id}")
def get_user(user_id: int):

    if user_id <= len(users):
        return {
            "message": "User found",
            "data": users[user_id - 1]
        }

    return {
        "message": "User not found"
    }


# POST - Create user
@app.post("/user")
def create_user(username: str, age: int):

    new_user = {
        "name": username,
        "age": age
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "data": new_user
    }


# PUT - Update user
@app.put("/user/{user_id}")
def update_user(user_id: int, username: str, age: int):

    if user_id <= len(users):
        users[user_id - 1]["name"] = username
        users[user_id - 1]["age"] = age

        return {
            "message": "User updated successfully",
            "data": users[user_id - 1]
        }

    return {
        "message": "User not found"
    }


# DELETE - Delete user
@app.delete("/user/{user_id}")
def delete_user(user_id: int):

    if user_id <= len(users):
        deleted_user = users.pop(user_id - 1)

        return {
            "message": "User deleted successfully",
            "data": deleted_user
        }

    return {
        "message": "User not found"
    }