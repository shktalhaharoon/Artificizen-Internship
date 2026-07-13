from fastapi import FastAPI, HTTPException, Header
app = FastAPI(title="Week 02 Day 05")
emails = []


@app.post("/users")
def create_user(email: str):

    if email in emails:
        raise HTTPException(
            status_code=409,
            detail="Email already exists")
    emails.append(email)
    return {"message": "User Created"}


@app.get("/protected")
def protected_route(authorization: str = Header(default=None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized")
    return {"message": "Access Granted"}