import requests

# URL de la API
URL = 'https://randomuser.me/api'

# Realizar la solicitud GET
r = requests.get(url=URL)

# Convertir la respuesta a JSON
datos = r.json()

# Extraer el nombre del primer resultado
nombre = datos['results'][0]['name']

# Formatear el nombre completo
nombre_completo = f"{nombre['title']} {nombre['first']} {nombre['last']}"

# Imprimir el nombre completo
print(nombre_completo)
