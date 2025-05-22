# FastAPI model server for Iris dataset
# Path: model-servers/fast-api-server/app/app.py
# Run with: uvicorn app:app --reload

# 1. Create the data model
# 2. Load the model
# 3. Create the health check endpoint
# 4. Create the prediction endpoint

import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List
import numpy as np

# 1. Create the data model
# The data model describes the format of the input and output data
# The model is a simple dictionary with 4 float fields: sepal_length, sepal_width, petal_length, petal_width

class IrisData(BaseModel):
    # TODO: WRITE YOUR CODE HERE
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

    
# 2. Load the model
# The model is a serialized scikit-learn model
model_path = 'model.pkl'

# Load the model
model = joblib.load(model_path)


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "API Iris Dataset"}

# 3. Create the health check endpoint
# The health check endpoint is used to check if the server is up and running
# If the model is loaded correctly, the endpoint should return {"status": "ok"}	
try:
    model = joblib.load(model_path)
    model_loaded = True
except Exception as e:
    model_loaded = False
    print(f"Error loading model: {e}")

@app.get("/health")
async def health():
        return {"status": "ok"}

# 4. Create the prediction endpoint
# The prediction endpoint is used to get predictions from the model
# The endpoint should take the data model as input and return the prediction as output in json format
# HINT: fastapi expects to send a json object as output, so you need to convert the prediction to json format
# See https://fastapi.tiangolo.com/tutorial/response-model/

class PredictionInput(BaseModel):
    features: List[float]

@app.post("/predict")
async def predict(input_data: PredictionInput):

    features = np.array(input_data.features).reshape(1, -1)  

    prediction = model.predict(features)

    return {"prediction": prediction.tolist()}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# Example request:
# curl -X 'POST' \
#     'http://localhost:8000/predict' \
#     -H 'accept: application/json' \
#     -H 'Content-Type: application/json' \
#     -d "{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}"