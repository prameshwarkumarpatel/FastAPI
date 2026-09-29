from fastapi import FastAPI, status

app = FastAPI()


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "user_created"
    }