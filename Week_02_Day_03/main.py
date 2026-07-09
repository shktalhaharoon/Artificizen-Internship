from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from database import engine, Base, get_db

import models
import schemas

app = FastAPI(title="Week 02 (Day 03)")

# Create database tables
Base.metadata.create_all(bind=engine)



# Task 1
@app.get("/")
def home():

    return {
        "message": "SQLite Database Connected Successfully"
    }


# Task 2
# POST /users
@app.post("/users", response_model=schemas.UserRead)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    new_user = models.User(name=user.name,email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



# Task 3
# GET /users/{user_id}


@app.get("/users/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user


# Task 4
# GET /users
@app.get("/users")
def get_all_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# Task 5
# DELETE /users/{user_id}


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    db.delete(user)
    db.commit()
    return Response(status_code=204)





# Task 6
# GET /users/{user_id}/posts

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user.posts