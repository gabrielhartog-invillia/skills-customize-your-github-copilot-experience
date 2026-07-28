"""
Building REST APIs with FastAPI - Starter Code

Instructions:
1. Install the required packages:
       pip install fastapi uvicorn

2. Run the application:
       uvicorn starter-code:app --reload

3. Open your browser at http://127.0.0.1:8000
   Interactive API docs are available at http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

app = FastAPI(title="Items API")

# --- In-memory data store ---
items = [
    {"id": 1, "name": "Hammer", "price": 12.99},
    {"id": 2, "name": "Screwdriver", "price": 7.49},
    {"id": 3, "name": "Wrench", "price": 15.00},
]


# --- Task 3: Define your Pydantic model here ---
# class Item(BaseModel):
#     name: str
#     price: float
#
#     @field_validator("price")
#     @classmethod
#     def price_must_be_positive(cls, v):
#         # TODO: raise ValueError if price <= 0
#         pass


# --- Task 1: Root endpoint ---
@app.get("/")
def read_root():
    # TODO: return a welcome message
    pass


# --- Task 1: List all items ---
@app.get("/items")
def list_items(name: str = None, limit: int = 10):
    # TODO: return items list
    # Task 2: filter by `name` (case-insensitive) if provided
    # Task 2: apply the `limit` parameter
    pass


# --- Task 2: Get item by ID ---
@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: find and return the item with the given item_id
    # Raise HTTP 404 if not found
    pass


# --- Task 3: Create a new item ---
# @app.post("/items", status_code=201)
# def create_item(item: Item):
#     # TODO: assign a new unique id and append to items list
#     pass


# --- Task 3: Update an existing item ---
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     # TODO: find the item, update name and price, return updated item
#     # Raise HTTP 404 if not found
#     pass
