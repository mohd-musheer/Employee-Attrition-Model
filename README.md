🤖 AI Employee Attrition Predictor

Machine Learning · FastAPI · Docker · Modern UI


live on : https://employee-attrition-model-x0ek.onrender.com


Docker : https://hub.docker.com/repository/docker/mohdmusheer/employee-attrition-predictor


📌 Overview

AI Employee Attrition Predictor is an end-to-end Machine Learning application that predicts whether an employee is likely to leave or stay in an organization.

The project demonstrates the complete ML lifecycle — from data cleaning and model training to production deployment using FastAPI and Docker, along with a modern AI-styled web interface.

🎯 Problem Statement

Employee attrition leads to:

High hiring costs

Loss of skilled talent

Reduced productivity

This system helps organizations identify employees at risk of leaving, enabling proactive retention strategies.

✨ Key Features

🔮 Real-time employee attrition prediction

🤖 Random Forest ML model (scikit-learn)

🚀 FastAPI backend with REST API

🎨 Modern purple-blue AI-themed UI

📊 Progress bar & demo data loader

🐳 Fully Dockerized application

📦 Model serialization using joblib

🧠 Machine Learning Details

Algorithm: Random Forest Classifier

Target Variable: Attrition (0 = Stay, 1 = Leave)

Data Preparation:

Removed non-informative columns

Encoded categorical features

Scaled numerical features

Addressed class imbalance

Evaluation:

Cross-validated accuracy ~84%

Confusion matrix, Recall, F1-score

Accuracy alone is misleading for attrition problems, so recall and F1-score were emphasized.

🏗️ System Architecture
User (UI)
   ↓
FastAPI Backend
   ↓
Preprocessing Pipeline
   ↓
Random Forest Model
   ↓
Prediction (Stay / Leave)

🌐 API Endpoints
🔹 Home
GET /


Returns the web UI.

🔹 Predict Attrition
POST /predict

Sample Request
{
  "Age": 41,
  "DailyRate": 1102,
  "Department": "Sales",
  "DistanceFromHome": 1,
  "Education": 2,
  "EnvironmentSatisfaction": 2,
  "Gender": "Female",
  "HourlyRate": 94,
  "JobInvolvement": 3,
  "JobLevel": 2,
  "JobRole": "Sales Executive",
  "JobSatisfaction": 4,
  "MaritalStatus": "Single",
  "MonthlyIncome": 5993,
  "MonthlyRate": 19479,
  "NumCompaniesWorked": 8,
  "OverTime": "Yes",
  "PercentSalaryHike": 11,
  "PerformanceRating": 3,
  "RelationshipSatisfaction": 1,
  "StockOptionLevel": 0,
  "TotalWorkingYears": 8,
  "TrainingTimesLastYear": 0,
  "WorkLifeBalance": 1,
  "YearsAtCompany": 6,
  "YearsInCurrentRole": 4,
  "YearsSinceLastPromotion": 0,
  "YearsWithCurrManager": 5
}

Sample Response
{
  "prediction": "Stay"
}

🐳 Run with Docker (Recommended)
1️⃣ Pull the image
docker pull <your-docker-username>/ai-employee-attrition-predictor

2️⃣ Run the container
docker run -p 8000:8000 <your-docker-username>/ai-employee-attrition-predictor

3️⃣ Open in browser
http://localhost:8000

🧪 Run Locally (Without Docker)
git clone https://github.com/<your-username>/ai-employee-attrition-predictor.git
cd ai-employee-attrition-predictor

pip install -r requirements.txt
uvicorn Employee:app --reload

🎨 UI Highlights

AI-themed purple & blue design

Human-friendly input labels

Large call-to-action button

Progress bar during prediction

Demo data loader for quick testing