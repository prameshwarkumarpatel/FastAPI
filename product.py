from fastapi import FastAPI

app = FastAPI()


# Path Parameter
@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    return {
        "message": f"Hello user {user_id}",
        "user_id": user_id
    }


# Query Parameter
@app.get("/user")
def get_user(name: str | None = None):
    return {
        "message": f"Hello {name}",
        "name": name
    }


# Multiple Query Parameters
@app.get("/items")
def get_items(limit: int = 10, offset: int = 0):
    return {
        "message": f"Items with limit {limit} and offset {offset}",
        "limit": limit,
        "offset": offset
    }


# Multiple Query Parameters
@app.get("/products")
def get_products(name: str | None = None, price: int = 0):
    return {
        "message": f"Hello {name}",
        "name": name,
        "price": price
    }