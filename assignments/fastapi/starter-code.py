from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items: List[Item] = [
    Item(id=1, name="Notebook", description="A simple ruled notebook", price=4.99),
    Item(id=2, name="Pencil", description="HB pencil for writing", price=0.99),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API"}

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item
