#Realiza una petición HTTPs a la ruta https://randomuser.me/api y 
# muestra por consola el nombre y los apellidos retornados por la API

import requests
respuesta = requests.get('https://randomuser.me/api')
respuesta = respuesta.json()
nombre = respuesta["results"][0]["name"]["first"]
apellido = respuesta["results"][0]["name"]["last"]
print(f"El nombre de esta persona es, {nombre} {apellido}")

#En este codigo se importa la libreria rquest, se obtiene una respuesta en formato json, la cual con .json() 
#se pasa a formato diccionario, de aqui simplemente consiste en moverse por el diciconario
#Finalmente se hace un print del nombre y apellido