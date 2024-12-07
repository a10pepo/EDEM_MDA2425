# 3
import requests

respuesta = requests.get('https://randomuser.me/api')
print(respuesta.status_code)

datos_user = respuesta.json() 

user_nombre:str = datos_user['results'][0]['name']['first']
user_apellido:str = datos_user['results'][0]['name']['last']


print(f'El nombre es {user_nombre} y el apellido {user_apellido}') 
