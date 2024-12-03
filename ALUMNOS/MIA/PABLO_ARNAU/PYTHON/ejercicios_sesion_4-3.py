import requests

respuesta = requests.get("https://randomuser.me/api")
randomuser = respuesta.json()

nombre = randomuser['results'][0]['name']['first']
apellido = randomuser['results'][0]['name']['last']

print (f'El nombre es {nombre} y el apellido {apellido}')

