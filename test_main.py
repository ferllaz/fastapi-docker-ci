
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_add():
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_multiply():
    response = client.get("/multiply/4/5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}