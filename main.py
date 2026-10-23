from fastapi import FastAPI
from pydantic import BaseModel
import socket

from pydantic import BaseModel

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

class MultiplyRequest(BaseModel):
    a: int
    b: int

@app.post("/multiply")
def multiply(data: MultiplyRequest):
    return {
        "result a*b=": data.a * data.b,
        "developer": "Dev1"
    }
@app.post("/divide")
def divide(data: MultiplyRequest):
    return {
        "result a/b=": data.a / data.b,
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

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.delete("/remove/{id}")
def remove_item(id: int):
    for item in items:
        if item["id"] == id:
            items.remove(item)
            return {"message": "Item deleted", "id": id}

    return {"message": "Item not found", "id": id}

    
class UpdateItem(BaseModel):
    name: str
@app.put("/update/{id}")
def update_item(id: int, item: UpdateItem):
    return {
        "message": f"Item {id} mis à jour avec succès",
        "id": id,
        "updated_data": item,
        "developer": "Dev2"
    }
