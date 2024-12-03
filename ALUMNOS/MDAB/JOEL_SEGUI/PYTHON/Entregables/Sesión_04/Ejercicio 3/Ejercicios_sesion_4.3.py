import requests
r = requests.get('https://randomuser.me/api')

datos = r.json()

nombre = datos["results"][0]["name"]
nombre_completo = f"{nombre['title']} {nombre['first']} {nombre['last']}"
print(f'El nombre aleatorio obtenido es: {nombre_completo}')
