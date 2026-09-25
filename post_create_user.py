from fastapi import FastAPI

app = FastAPI()


@app.post("/user/{user_id}")
def create_user(user_id: int, user: dict):
    return {
        "user_id": user_id,
        "user": user
    }