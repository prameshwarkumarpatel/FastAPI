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
                update_user={
                    "usernaem":x.user,
                    "age":x.user
                }
                return user.append(update_user)
        return users