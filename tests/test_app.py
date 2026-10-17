import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to the College ERP System"

def test_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json["students"]) == 2

def test_courses(client):
    response = client.get("/courses")
    assert response.status_code == 200
    assert len(response.json["courses"]) == 2
