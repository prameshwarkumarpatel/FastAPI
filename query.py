from fastapi import FastAPI, HTTPException, status, Request
from pydantic import BaseModel

app = FastAPI()


class Users(BaseModel):
    name: str
    age: int
    roll: int
    notify: bool


total_user = []


@app.post("/user/{user_id}")
def create_user(user: Users, user_id: int, request: Request):

    if user.age < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user age must be greater than 18"
        )

    total_user.append(user)

    return {
        "status": status.HTTP_200_OK,
        "message": "user created successfully",
        "data": user,
        "notify": user.notify,
        "url": str(request.url)
    }


@app.put("/user/{user_id}")
def update_user(
    user_id: int,
    user: Users,
    request: Request,
    notify: bool = False
):

    if user_id < 0 or user_id >= len(total_user):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )

    total_user[user_id] = user

    return {
        "status": status.HTTP_200_OK,
        "message": "user updated successfully",
        "data": user,
        "notify": notify,
        "url": str(request.url)
    }


@app.get("/user/{user_id}")
def get_user(user_id: int, request: Request):

    if user_id < 0 or user_id >= len(total_user):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )

    return {
        "status": status.HTTP_200_OK,
        "message": "user fetched successfully",
        "data": total_user[user_id],
        "url": str(request.url)
    }