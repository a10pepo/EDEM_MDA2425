import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

# Definir la estructura de los datos de entrada
class IrisInput(BaseModel):
    sl: float  # Sepal Length
    sw: float  # Sepal Width
    pl: float  # Petal Length
    pw: float  # Petal Width

# Obtener el path del modelo de manera relativa
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
modelo = joblib.load(MODEL_PATH)

# Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de predicción del dataset Iris"}

# Endpoint de verificación del estado del servicio
@app.get("/status")
def check_status():
    return {"service": "running", "model_loaded": modelo is not None}

# Endpoint de predicción
@app.post("/predict")
def get_prediction(entrada: IrisInput):
    features = [[entrada.sl, entrada.sw, entrada.pl, entrada.pw]]
    resultado = modelo.predict(features)
    return {"prediccion": resultado[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
