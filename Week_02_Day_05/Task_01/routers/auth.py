from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():

    return {
        "message": "Login Successful"
    }


@router.post("/logout")
def logout():

    return {
        "message": "Logout Successful"
    }