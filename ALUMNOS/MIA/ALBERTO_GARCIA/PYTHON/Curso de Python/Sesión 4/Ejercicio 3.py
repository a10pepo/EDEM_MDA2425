import requests
r=requests.get('https://randomuser.me/api')
datos=r.json()
nombre:str =datos['results'][0]['name']['first']
apellido:str =datos['results'][0]['name']['last']
print(f'El nombre completo es: {nombre} {apellido}')