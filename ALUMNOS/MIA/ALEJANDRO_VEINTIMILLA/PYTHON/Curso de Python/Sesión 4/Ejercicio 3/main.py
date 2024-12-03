#4. Ejercicios Sesión 4
#   3.Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre 
#       y los apellidos retornados por la API

import requests

respuesta = requests.get("https://randomuser.me/api")

#print(respuesta.status_code)- Para comprobar que la respuesta llega correctamente durnate testing

datos = respuesta.json() 
name:str=datos["results"][0]["name"]["title"]+"."+datos["results"][0]["name"]["last"]+" "+datos["results"][0]["name"]["first"]

print(name)
