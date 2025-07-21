import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np

# 1. Create the data model
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 2. Load the model
model = joblib.load("iris_model.pkl")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 3. Create the health check endpoint
@app.get("/health")
async def health():
    if model:
        return {"status": "ok"}
    else:
        return {"status": "error", "detail": "Model not loaded"}

# 4. Create the prediction endpoint
@app.post("/predict")
async def predict(data: IrisData):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)
    return {"prediction": prediction[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Example request:
# curl -X 'POST' \
#     'http://localhost:8000/predict' \
#     -H 'accept: application/json' \
#     -H 'Content-Type: application/json' \
#     -d "{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}"