from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "status": 404,
            "message": f"User {exc.name} not found"
        }
    )


@app.get("/user/name/{name}")
def user_getapi(name: str):
    if name != "monmohan":
        raise UserNotFoundException(name)

    return {
        "username": name
    }


@app.get("/user/id/{user_id}")
def user_get(user_id: int):

    users = [
        {"user_id": 1, "name": "pawan kumar patel"},
        {"user_id": 2, "name": "nitesh kumar patel"},
        {"user_id": 3, "name": "prameshwar kumar patel"}
    ]

    for user in users:
        if user["user_id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="user not found"
    )