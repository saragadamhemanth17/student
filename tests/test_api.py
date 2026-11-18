
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_prediction():
    student = {
        "CGPA": 8.5,
        "Programming_Score": 85,
        "Communication_Score": 80,
        "Aptitude_Score": 82,
        "Internship": 1,
        "Projects": 3,
        "Technical_Score": 84.1
    }

    response = client.post("/predict", json=student)

    assert response.status_code == 200
    assert response.json()["placement_prediction"] in [
        "Placed", "Not Placed"
    ]

print("API tests created successfully")
