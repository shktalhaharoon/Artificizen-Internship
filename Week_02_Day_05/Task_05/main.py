from fastapi import FastAPI, BackgroundTasks
app = FastAPI(title="Week 02 Day 05")


# Background Function
def send_welcome_email(name: str):
    print(f"Welcome Email Sent to {name}")


@app.post("/users")
def create_user(
    name: str,
    background_tasks: BackgroundTasks
):

    # Run in background
    background_tasks.add_task(
        send_welcome_email,
        name)
    return {"message": "User Created Successfully"}