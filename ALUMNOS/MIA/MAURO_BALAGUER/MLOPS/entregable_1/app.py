import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 1. Create the data model
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 2. Load the model
load_model = joblib.load("/Users/mauro/Documents/MIA/EDEM_MDA2425/ALUMNOS/MIA/MAURO_BALAGUER/MLOPS/entregable_1/iris_model.pkl")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 3. Create the health check endpoint
@app.get("/health")
async def health():
    try:
        load_model
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 4. Create the prediction endpoint
@app.post("/predict")
async def predict(data: IrisData):
    predicciones = load_model.predict([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    return {'predicciones': predicciones.tolist()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
