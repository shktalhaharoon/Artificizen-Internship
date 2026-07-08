from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="Week 02 (Day 02) -- Task 06")

class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

class ItemRead(BaseModel):
    name: str
    price: float
    in_stock: bool
    created_at: str

@app.post("/items", response_model=ItemRead)
def create_item(item: ItemCreate):
    item_data = {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
        "created_at": "2025-07-09 10:30 AM"
    }
    
    return item_data