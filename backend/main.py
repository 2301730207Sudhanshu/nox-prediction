from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load model
model = joblib.load("model/RESEARCH_model.pkl")

# ✅ Input schema
class InputData(BaseModel):
    no2: float
    traffic: float
    no: float
    wind_speed: float
    airflow: float
    co: float
    temperature: float
    o3: float
    pm10: float
    relativehumidity: float
    depth: float

@app.get("/")
def home():
    return {"message": "NOx Prediction API is running"}

@app.post("/predict")
def predict(data: InputData):
    try:
        input_array = np.array(list(data.dict().values())).reshape(1, -1)
        prediction = model.predict(input_array)
        return {"predicted_NOx": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}