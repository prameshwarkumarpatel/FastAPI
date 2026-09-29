from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


useradd = []


@app.post("/user")
def create_user(user: User):
    new_user = {
        "name": user.name,
        "age": user.age
    }

    useradd.append(new_user)

    return {
        "message": "Successfully",
        "data": useradd
    }


@app.put("/user/{user_id}")
def user_update(user_id: int, user: User, notify: bool = False):

    if user_id <= len(useradd):
        x = useradd[user_id - 1]

        x["name"] = user.name
        x["age"] = user.age

        return {
            "message": "Your message is successfully",
            "notify": notify,
            "data": x
        }

    return {
        "message": "User not found"
    }