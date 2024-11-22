#Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code

import requests
import pandas as pd

def archivo8():
    print("¡Hola desde el proyecto plantilla de Python!")
    
    response = requests.get("https://api.github.com")
    print(f"Estado de la API de GitHub: {response.status_code}")
    
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("\nDataFrame de ejemplo:")
    print(df)

if __name__ == "__main__":
    archivo8()