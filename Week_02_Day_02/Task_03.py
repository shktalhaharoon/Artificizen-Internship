from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="Week 02 (Day 02)")
# User nter This Data Name,email,Age 
class UserCreate(BaseModel):
    name: str
    email: str
    age: int
# ID is given by server
class UserRead(BaseModel):
    id: int
    name: str
    email: str
    age: int


@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate):
    user_data = {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
    return user_data