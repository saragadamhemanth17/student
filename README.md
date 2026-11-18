
# Student Placement Prediction using MLOps

## Problem Statement
Predict student placement status using academic and technical skills.

## Technologies
- Python
- Pandas and NumPy
- Scikit-learn
- MLflow
- FastAPI
- GitHub Actions

## MLOps Workflow

1. Synthetic Dataset Generation
2. Dataset Version Management
3. Data Preprocessing
4. Feature Engineering and Feature Store
5. Model Training
6. Model Evaluation
7. MLflow Experiment Tracking
8. Model Registry
9. GitHub Actions CI/CD
10. FastAPI Model Deployment

## Models
- Logistic Regression
- Random Forest Classifier

## API Endpoint

POST /predict

## Execution

pip install -r requirements.txt

pytest -v

uvicorn api.main:app --reload

## Dataset
Dataset V1 and V2 are stored in the data folder.

## Conclusion
The project implements an end-to-end MLOps workflow
for predicting student placement status.
