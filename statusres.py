from fastapi import FastAPI, status,HTTPException

app =  FastAPI()
@app.post("/user", status_code= status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "user created successfully"

    }
@app.get("/user", status_code = status.HTTP_200_OK)
def get_user():
    return {
        "message": " your message is successsfully",
        "data": {
            "name": "prameshwar",
            "roll": 1,
            "street": "kakinada",
            "power": "java"
        }
    }
@app.get("/user/{user_id}")
def get_userss(user_id: int):
    if user_id!=1:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with this {user_id} is not available"
        )
    return {
        message:"succssfully",
        status_code: status.HTTP_200_OK,
        "datat":{
            "name": "pk",
            "rooll":1,
            "maya":"pk"
        }
    }