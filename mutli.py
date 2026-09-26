from fastapi import FastAPI

app = FastAPI()

# Multi method

@app.get("/")
def home():
    return {"message": "GET method is present"}


@app.post("/data")
def post_data():
    return {"message": "POST method is present"}


@app.put("/data")
def put_data():
    return {"message": "PUT method is present"}


@app.delete("/data")
def delete_data():
    return {"message": "DELETE method is present"}