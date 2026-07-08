from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="Week 02 (Day 02) -- Task 04")


class Address(BaseModel):
    city: str
    country: str

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    address: Address

@app.post("/users")
def create_user(user: UserCreate):
    return user