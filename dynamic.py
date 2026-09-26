from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
def get_user(name: str | None = None):
    return {
        "message": f"Hello {name}",
        "name": name
    }
    