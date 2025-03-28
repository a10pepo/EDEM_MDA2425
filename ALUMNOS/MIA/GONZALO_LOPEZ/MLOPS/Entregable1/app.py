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
import pickle
import numpy as np
import os
from typing import List


# 1. Create the data model
# The data model describes the format of the input and output data
# The model is a simple dictionary with 4 float fields: sepal_length, sepal_width, petal_length, petal_width

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    # TODO: WRITE YOUR CODE HERE
    
class PredictRequest(BaseModel):
    instances: List[IrisData]

    class PredictResponse(BaseModel):
        predictions: List[int]

    
# 2. Load the model
# The model is a serialized scikit-learn model
# TODO: WRITE YOUR CODE HERE
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ Modelo cargado correctamente.")
except Exception as e:
    print(f"❌ Error al cargar el modelo: {e}")


HEALTH_ROUTE = os.getenv("AIP_HEALTH_ROUTE", "/health")
PREDICT_ROUTE = os.getenv("AIP_PREDICT_ROUTE", "/predict")



app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 3. Create the health check endpoint
# The health check endpoint is used to check if the server is up and running
# If the model is loaded correctly, the endpoint should return {"status": "ok"}	


@app.get(HEALTH_ROUTE, status_code=200, summary="Health Check")
async def health():
        # TODO: WRITE YOUR CODE HERE
    if model:
        return {"status": "ok"}
    



    

@app.post(PREDICT_ROUTE,response_model=PredictResponse, summary="Make a Prediction")
async def predict(request: PredictRequest):
    inputs=np.asarray(request.instances)
    inputs=[[x.sepal_length, x.sepal_width, x.petal_length, x.petal_width] for x in inputs]
    y_pred=model.predict(inputs)
    outputs=[int(x) for x in y_pred]
    return PredictResponse(predictions=outputs)    
    

# 4. Create the prediction endpoint
# The prediction endpoint is used to get predictions from the model
# The endpoint should take the data model as input and return the prediction as output in json format
# HINT: fastapi expects to send a json object as output, so you need to convert the prediction to json format
# See https://fastapi.tiangolo.com/tutorial/response-model/

@app.post("/predict")
async def predict(data: IrisData):
    try:
        input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        prediction = model.predict(input_data).tolist()
        return {"prediction": prediction}
    except Exception as e:
        return {"error": f"Error al hacer la predicción: {str(e)}"}
    # TODO: WRITE YOUR CODE HERE


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# Example request:
# curl -X 'POST' \
#     'http://localhost:8000/predict' \
#     -H 'accept: application/json' \
#     -H 'Content-Type: application/json' \
#     -d "{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}"