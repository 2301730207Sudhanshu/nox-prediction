from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model/RESEARCH_model.pkl")

@app.get("/")
def home():
    return {"message": "NOx Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    try:
        input_data = [
            data["no2"],
            data["traffic"],
            data["no"],
            data["wind_speed"],
            data["airflow"],
            data["co"],
            data["temperature"],
            data["o3"],
            data["pm10"],
            data["relativehumidity"],
            data["depth"]
        ]

        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)

        return {"predicted_NOx": float(prediction[0])}

    except Exception as e:
        return {"error": str(e)}