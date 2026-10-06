from fastapi import FastAPI, Depends

app = FastAPI()


def common_logic():
    return {
        "message": "common logic executed successfully",
        "status_code": 200
    }


def get_user():
    return {
        "name": "prameshwar",
        "id": 1,
        "pay": "ph111",
        "street": "sakhuwa"
    }


def dashboard():
    return {
        "message": "dashboard page",
        "status_code": 200
    }


@app.get("/home")
def home(data=Depends(common_logic)):
    return {
        "message": "home page",
        "status_code": 200,
        "data": data
    }


@app.get("/profile")
def profile_user(user=Depends(get_user)):
    return {
        "message": "profile page",
        "street": user["street"]
    }


@app.get("/dashboard")
def dashboard_user(user=Depends(dashboard)):
    return {
        "message": "dashboard page",
        "status_code": 200
    }