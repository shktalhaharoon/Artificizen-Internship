from fastapi import FastAPI
from pydantic import BaseModel, field_validator
app = FastAPI(title="Week 02 (Day 02) -- Task 05")


class UserCreate(BaseModel):

    name: str
    email: str
    age: int

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        for character in value:

            if character.isdigit():

                raise ValueError("Name cannot contain numbers.")

        return value


@app.post("/users")
def create_user(user: UserCreate):

    return user