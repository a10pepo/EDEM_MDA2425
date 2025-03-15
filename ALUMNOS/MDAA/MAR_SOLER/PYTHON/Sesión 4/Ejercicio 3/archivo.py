# Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests

api = requests.get("https://randomuser.me/api")
data= api.json()

nombre = data['results'][0]['name']['first']
apellido = data['results'][0]['name']['last']
    
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")