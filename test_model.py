import joblib

model = joblib.load("backend/model/RESEARCH_model.pkl")

print("Model loaded successfully")
print(type(model))