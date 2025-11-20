import pickle
from fastapi import FastAPI

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Model API is running"}

@app.post("/predict")
def predict(feature1: float, feature2: float):
    prediction = model.predict([[feature1, feature2]])[0]
    return {
        "feature1": feature1,
        "feature2": feature2,
        "prediction": prediction
    }
