from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import RootModel
import pandas as pd
import joblib

class EmployeeData(RootModel[dict]):
    pass

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("EmployeeAttritionDataset.pkl")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as f:
        return f.read()

@app.post("/predict")
def predict(data: EmployeeData):
    input_df = pd.DataFrame([data.root])
    pred = model.predict(input_df)[0]
    result = "Leave" if pred == 1 else "Stay"
    return JSONResponse({"prediction": result})
