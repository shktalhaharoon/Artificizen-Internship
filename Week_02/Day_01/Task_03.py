from fastapi import FastAPI
app = FastAPI(title="Week 02 (Day 01)")
items = [
    "Bike",
    "Cycle",
    "Laptop",
    "Phone",
    "Keyboard",
    "Mouse",
    "KeyChain",
    "Water Bottle",
    "Notebook",
    "Tablet",
    "LCD",
    "Charger"
]


@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]