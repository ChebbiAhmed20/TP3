from fastapi import FastAPI
import socket

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

@app.get("/greeting")
def greeting(name: str):
    hostname = socket.gethostname()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("192.0.2.1", 80))
        ip_address = s.getsockname()[0]

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "IP": ip_address
    }