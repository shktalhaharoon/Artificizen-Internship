from fastapi import FastAPI, Request
app = FastAPI(title="Week 02 Day 05")


# Middleware to log request details
@app.middleware("http")
async def log_requests(request: Request, call_next):

    # Print request 
    print("Request Method :", request.method)

    # Print request path
    print("Request Path   :", request.url.path)

    # Continue to the requested endpoint
    response = await call_next(request)

    # Print response status code
    print("Response Status:", response.status_code)
    return response


# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# Sample GET Route
@app.get("/users")
def get_users():
    return {"message": "List of Users"}


# Sample POST Route
@app.post("/users")
def create_user():
    return {"message": "User Created Successfully"}