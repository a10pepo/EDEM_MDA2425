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

# 1. Create the data model
# The data model describes the format of the input and output data
# The model is a simple dictionary with 4 float fields: sepal_length, sepal_width, petal_length, petal_width

class IrisData(BaseModel):
    # TODO: WRITE YOUR CODE HERE
    pass

    
# 2. Load the model
# The model is a serialized scikit-learn model

# TODO: WRITE YOUR CODE HERE


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 3. Create the health check endpoint
# The health check endpoint is used to check if the server is up and running
# If the model is loaded correctly, the endpoint should return {"status": "ok"}	

@app.get("/health")
async def health():
    # TODO: WRITE YOUR CODE HERE
    pass

# 4. Create the prediction endpoint
# The prediction endpoint is used to get predictions from the model
# The endpoint should take the data model as input and return the prediction as output in json format
# HINT: fastapi expects to send a json object as output, so you need to convert the prediction to json format
# See https://fastapi.tiangolo.com/tutorial/response-model/

@app.post("/predict")
async def predict(data: IrisData):
    # TODO: WRITE YOUR CODE HERE

    return None
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# Example request:
# curl -X 'POST' \
#     'http://localhost:8000/predict' \
#     -H 'accept: application/json' \
#     -H 'Content-Type: application/json' \
#     -d "{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}"