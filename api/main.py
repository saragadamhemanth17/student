
import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student Placement Prediction API")

# Load trained model
model = joblib.load("models/model.pkl")

class Student(BaseModel):
    CGPA: float
    Programming_Score: float
    Communication_Score: float
    Aptitude_Score: float
    Internship: int
    Projects: int
    Technical_Score: float

@app.get("/")
def home():
    return {"message": "Student Placement API is running"}

@app.post("/predict")
def predict(student: Student):

    input_data = pd.DataFrame([student.model_dump()])

    prediction = model.predict(input_data)[0]

    result = "Placed" if int(prediction) == 1 else "Not Placed"

    return {
        "placement_prediction": result,
        "prediction_value": int(prediction)
    }
