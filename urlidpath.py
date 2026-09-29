from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserUpi(BaseModel):
    name: str
    age: int


users = []


@app.post("/user/")
def create_user(user: UserUpi):
    new_user = {
        "username": user.name,
        "age": user.age,
        "message": "Successfully created the user"
    }

    users.append(new_user)

    return {
        "message": "Successfully",
        "data": users
    }

    @app.put("user/{user_id}")
    def update_users(user_id:int,user:UserUpi,notify:bool=false):
        for x in users:
            if(user[user_id]==user_id):
                x["username"]:user.name
                x["username"]:user.age
                return {
                    "message":"successfully your message",
                    "success":true
                }
        return {
            "message": "not found"
        }