from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test 1
def test_create_user():

    response = client.post(

        "/users",

        params={

            "email": "ali@gmail.com"

        }

    )

    assert response.status_code == 200


# Test 2
def test_duplicate_email():

    client.post(

        "/users",

        params={

            "email": "abc@gmail.com"

        }

    )

    response = client.post(

        "/users",

        params={

            "email": "abc@gmail.com"

        }

    )

    assert response.status_code == 409


# Test 3
def test_protected_route():

    response = client.get("/protected")

    assert response.status_code == 401