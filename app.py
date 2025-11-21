import pickle
from fastapi import FastAPI
from pydantic import BaseModel


class Features(BaseModel):
    feature1: float
    feature2: float


app = FastAPI()


# Load model at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
def home():
    return {"message": "Model API is running"}


@app.post("/predict")
def predict(feats: Features):
    X = [[feats.feature1, feats.feature2]]
    pred = model.predict(X)[0]
    return {"prediction": float(pred)}