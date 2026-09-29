from fastapi import FastAPI, status,HTTPException

app = FastAPI()


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "user_created"
    }

@app.get("/user")
def user_get():
    return{
        "message":"successfully the code and exiting ",
        "status":"sucess",
        "data":{
            "name":"maya.tech"
        }

    }
@app.get("/user/{user_id}")
def user_get(user_id:int):
    if user_id!=1:
        raise HTTPException{
         status_code:404,
         default_user:"user not found"
        }
    return{
        "id":1,
        "name":"prameshwar kumar patel"
    }
