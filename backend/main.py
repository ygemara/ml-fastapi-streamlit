from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model/model.pkl")

class Input(BaseModel):
    number: float

@app.post("/predict")
def predict(data: Input):
    prediction = model.predict([[data.number]])
    return {"prediction": int(prediction[0])}
