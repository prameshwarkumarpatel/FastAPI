from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class UserExceptionHandler(Exception):
    def __init__(
        self,
        name: str,
        age: int,
        username: str,
        email: str,
        password: str
    ):
        self.name = name
        self.age = age
        self.username = username
        self.email = email
        self.password = password


@app.exception_handler(UserExceptionHandler)
async def user_exception_not_found(
    request: Request,
    exc: UserExceptionHandler
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "message": "User not found",
            "status_code": status.HTTP_404_NOT_FOUND,
            "data": {
                "name": exc.name,
                "age": exc.age,
                "username": exc.username,
                "email": exc.email,
                "password": exc.password
            },
            "url": str(request.url)
        }
    )


@app.get("/user/{name}")
def get_user(name: str, request: Request):

    if name != "prameshwar":
        raise UserExceptionHandler(
            name=name,
            age=20,
            username="pawan",
            email="pawan@gmail.com",
            password="pk@123"
        )

    return {
        "message": "user found successfully",
        "status_code": status.HTTP_200_OK,
        "data": {
            "name": "pawan",
            "age": 22,
            "username": "pawakmr",
            "email": "pk@gmail.com",
            "password": "k@128"
        },
        "url": str(request.url)
    }