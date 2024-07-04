from fastapi import FastAPI, Request, Depends
from middleware import RequestInitTimeMiddleware

import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Add the middleware to the FastAPI app
app.add_middleware(RequestInitTimeMiddleware)

# Define a dependency to get request start time
async def get_request_start_time(request: Request):
    return request.state['request_start_time']

# Define your FastAPI routes below
@app.get("/")
async def read_root(start_time: float = Depends(get_request_start_time)):
    # start_time will contain the request initiation time
    return {"message": "Hello World", "request_initiation_time": start_time}
