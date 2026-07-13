from fastapi import FastAPI
from Week_02.Week_02_Day_05.Task_01.routers.user import router as user_router
from Week_02.Week_02_Day_05.Task_01.routers.auth import router as auth_router

app = FastAPI(title="Week 02 Day 05")
app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)


app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}