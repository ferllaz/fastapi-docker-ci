
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello"}


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}


@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}