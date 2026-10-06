from fastapi import FastAPI,Request
app=FastAPI()
@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("request received")
    response = await call_next(request)
    print("request servier send")
    return response
@app.get("/")
def home():
    return {
        "message": "you are hiring "
    }