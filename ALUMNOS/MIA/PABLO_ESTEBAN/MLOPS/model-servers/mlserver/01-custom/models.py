
from mlserver import MLModel
from mlserver.codecs import decode_args
from mlserver.utils import get_model_uri
from mlserver.errors import InferenceError
from mlserver.types import InferenceRequest, InferenceResponse
from mlserver import types
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib


class customModel(MLModel):
    async def load(self) -> bool:
        
        model_uri = await get_model_uri(self._settings) #"../../model.pkl" #
        
        with open(model_uri, 'rb') as f:
            self._model = joblib.load(f)
            
        self.ready = True
        return self.ready
    
    @decode_args
    async def predict(self, data: np.ndarray) -> np.ndarray:
        data = data.reshape(1, -1)
        data = data.astype(np.float32)
        
        predictions = self._model.predict(data)
        return np.asarray(predictions)
