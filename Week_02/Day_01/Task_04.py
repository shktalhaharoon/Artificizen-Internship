from fastapi import FastAPI, HTTPException
app = FastAPI(title="Week 02 (Day 01)")

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id > 100:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return {"User ID": user_id}