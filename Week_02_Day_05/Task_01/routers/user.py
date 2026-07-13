from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():

    return {
        "message": "All Users"
    }


@router.post("/")
def create_user():

    return {
        "message": "User Created Successfully"
    }