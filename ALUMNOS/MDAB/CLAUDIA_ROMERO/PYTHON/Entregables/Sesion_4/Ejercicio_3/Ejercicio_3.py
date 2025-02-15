#Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos 
# retornados por la API

import requests

respuesta = requests.get('https://randomuser.me/api')
datos = respuesta.json()
nombre = datos['results'][0]['name']['first']
apellido = datos['results'][0]['name']['last']

print(nombre, apellido)



