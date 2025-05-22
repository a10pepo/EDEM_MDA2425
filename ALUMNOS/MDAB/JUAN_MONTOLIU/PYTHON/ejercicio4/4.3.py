import requests

respuesta = requests.get('https://randomuser.me/api')

datos = respuesta.json()

usuario = datos['results'][0]

nombre = usuario['name']['first']
apellido = usuario['name']['last']

print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")