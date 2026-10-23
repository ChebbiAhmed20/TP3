from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it works !"}

@app.get("/addition")
def addition(a: int, b: int):
    return {
        "result a+b=": a + b,
        "developer": "Dev1"
    }


class MultiplyRequest(BaseModel):
    a: int
    b: int

@app.post("/multiply")
def multiply(data: MultiplyRequest):
    return {
        "result a*b=": data.a * data.b,
        "developer": "Dev1"
    }