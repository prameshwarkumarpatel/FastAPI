# home, profile, dashboard, file

from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()


# -------------------------
# Custom Exception
# -------------------------
class UserFound(Exception):
    def __init__(self, name: str):
        self.name = name


# -------------------------
# Exception Handler
# -------------------------
@app.exception_handler(UserFound)
def user_found_exception_handler(request: Request, exc: UserFound):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "status": 409,
            "message": "User already exists",
            "name": exc.name,
            "url": str(request.url)
        }
    )


# -------------------------
# Dependencies
# -------------------------
def home():
    return {
        "message": "this is home page",
        "page": "home_title"
    }


def profile():
    return {
        "message": "my profile file and page",
        "page": "profile page and directly access"
    }


def dashboard():
    return {
        "message": "this is dashboard page",
        "page": "dashboard page"
    }


def file():
    return {
        "message": "this is file page",
        "page": "file title"
    }


# -------------------------
# POST User
# -------------------------
@app.post("/user/{user_id}")
def create_post(user_id: int):

    if user_id == 1:
        raise UserFound("Prameshwar")

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "status": 201,
            "message": "User created successfully",
            "user_id": user_id
        }
    )


# -------------------------
# Home
# -------------------------
@app.get("/home")
def home_page(data=Depends(home), request: Request = None):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "home page",
            "status_code": 200,
            "url": str(request.url),
            "data": data
        }
    )


# -------------------------
# Profile
# -------------------------
@app.get("/profile")
def profile_page(data=Depends(profile), request: Request = None):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "profile page",
            "status_code": 200,
            "url": str(request.url),
            "data": data
        }
    )


# -------------------------
# Dashboard
# -------------------------
@app.get("/dashboard")
def dashboard_page(data=Depends(dashboard), request: Request = None):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "dashboard page",
            "status_code": 200,
            "url": str(request.url),
            "data": data
        }
    )


# -------------------------
# File
# -------------------------
@app.get("/file")
def file_page(data=Depends(file), request: Request = None):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "file page",
            "status_code": 200,
            "url": str(request.url),
            "data": data
        }
    )