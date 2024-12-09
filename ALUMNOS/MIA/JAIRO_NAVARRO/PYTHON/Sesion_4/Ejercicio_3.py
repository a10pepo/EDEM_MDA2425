import requests

url = requests.get('https://randomuser.me/api')

datos = url.json()

nombre = datos['results'][0]['name']['first']
apellido = datos['results'][0]['name']['last']

print(nombre, apellido)