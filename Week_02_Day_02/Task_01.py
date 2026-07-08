from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="Week 02 (Day 02) -- Task 01")

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):

    return user