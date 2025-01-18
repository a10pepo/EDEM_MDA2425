import requests

response = requests.get("https://randomuser.me/api")

if response.status_code == 200:

    data = response.json()

    user = data['results'][0]
    nombre = user['name']['first']
    apellidos = user['name']['last']

    print(f"Nombre: {nombre}, Apellidos: {apellidos}")
else:
    print("Error en la petición:", response.status_code)
