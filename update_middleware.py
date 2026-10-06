from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware("http")
async def middleware_user(request: Request, call_next):

    print("First received the request")

    first_time = time.time()

    print(f"\nThe value of time: {first_time}")

    response = await call_next(request)

    processing_response = time.time() - first_time

    print(
        f"\nThe value of processing time: {processing_response} "
        f"and path: {request.url.path}"
    )

    return response