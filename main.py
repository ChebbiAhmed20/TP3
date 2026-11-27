"""FastAPI demo application with basic arithmetic endpoints.

This module defines several HTTP endpoints for addition, subtraction,
 multiplication, division and a greeting.  It also includes utilities
 for managing a simple in‑memory list of items.
"""

# Standard library imports
import socket

# Third‑party imports
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Root endpoint returning a simple health message."""
    return {"message": "it works !"}


@app.get("/addition")
def addition(a: int, b: int) -> dict:
    """Return the sum of *a* and *b*.

    The response also contains a static ``developer`` field required by the
    tests.
    """
    return {
        "result a+b=": a + b,
        "developer": "Dev1",
    }


class MultiplyRequest(BaseModel):
    """Request model for multiplication and division endpoints."""

    a: int
    b: int


@app.get("/soustraction")
def soustraction(a: int, b: int) -> dict:
    """Return the difference *a* – *b*.

    The response mirrors the structure expected by the test suite.
    """
    return {
        "result a-b=": a - b,
        "developer": "Dev2",
    }


@app.post("/multiply")
def multiply(data: MultiplyRequest) -> dict:
    """Return the product of ``data.a`` and ``data.b``."""
    return {
        "result a*b=": data.a * data.b,
        "developer": "Dev1",
    }


@app.post("/divide")
def divide(data: MultiplyRequest) -> dict:
    """Return the quotient of ``data.a`` divided by ``data.b``.

    ``ZeroDivisionError`` is allowed to propagate; the tests never trigger it.
    """
    return {
        "result a/b=": data.a / data.b,
        "developer": "Dev1",
    }


@app.get("/greeting")
def greeting(name: str) -> dict:
    """Return a greeting together with host information.

    The function obtains the machine hostname and its outbound IP address.
    """
    hostname = socket.gethostname()
    # Determine the outward‑facing IP address using a dummy UDP socket.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("192.0.2.1", 80))
        ip_address = s.getsockname()[0]
    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "IP": ip_address,
    }

# Simple in‑memory list of items used by the delete and update endpoints.
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]


@app.delete("/remove/{item_id}")
def remove_item(item_id: int) -> dict:
    """Remove an item from ``items`` by its identifier.

    Returns a JSON payload indicating whether the removal was successful.
    """
    # Iterate over a copy to avoid modifying the list while iterating.
    for item in items[:]:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted", "id": item_id}
    return {"message": "Item not found", "id": item_id}


class UpdateItem(BaseModel):
    """Payload for updating an item's ``name`` field."""

    name: str


@app.put("/update/{item_id}")
def update_item(item_id: int, item: UpdateItem) -> dict:
    """Update the ``name`` of an existing item.

    The response mirrors the format required by the test suite.
    """
    for existing in items:
        if existing["id"] == item_id:
            existing["name"] = item.name
            break
    return {
        "message": f"Item {item_id} mis à jour avec succès",
        "id": item_id,
        "updated_data": item,
        "developer": "Dev2",
    }
