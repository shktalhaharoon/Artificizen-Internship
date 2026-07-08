from fastapi import FastAPI
# to use build in email 
# from pydantic import BaseModel, EmailStr
from pydantic import BaseModel, Field
app = FastAPI(title="Week 02 (Day 02) -- Task 02")

class UserCreate(BaseModel):
    name: str
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
# from pydantic import BaseModel, EmailStr
# we can also use this beacuse Pydantic provides a built-in for email
    # email: EmailStr
    age: int = Field(ge=18,le=120)


@app.post("/users")
def create_user(user: UserCreate):
    return user