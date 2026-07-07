from fastapi import FastAPI,status
app = FastAPI(title="Week 02 (Day 01)")
@app.post("/Ping", status_code= status.HTTP_201_CREATED)
def ping():

    return {"status": "created"}