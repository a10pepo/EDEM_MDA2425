#Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests
import json

url = "https://randomuser.me/api"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = json.loads(respuesta.text)
    
    nombre = datos['results'][0]['name']['first']
    apellidos = datos['results'][0]['name']['last']
    
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
else:
    print("Error al realizar la petición:", respuesta.status_code)