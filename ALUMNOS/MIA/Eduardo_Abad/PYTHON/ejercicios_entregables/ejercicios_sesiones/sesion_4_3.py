import requests

respuesta = requests.get('https://randomuser.me/api')

# Extraemos los datos en formato JSON

datos = respuesta.json()
print(datos) # Simplemente para comprobar el formato y como están los datos en el archivo JSON

nombre= datos['results'][0]['name']['first']
apellido= datos['results'][0]['name']['last']
print(f'El nombre y apellido del usuario es: {nombre} {apellido}')