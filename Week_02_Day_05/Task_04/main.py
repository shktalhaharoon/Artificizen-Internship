# {
#     "error": true,
#     "detail": "...",
#     "status": 404
# }


from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


app = FastAPI(title="Week 02 Day 05")

# Global Exception Handler
@app.exception_handler(HTTPException)
async def custom_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "detail": exc.detail,
            "status": exc.status_code
        })


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id > 100:
        raise HTTPException(
            status_code=404,
            detail="User not found")
    return {"user_id": user_id}