#by Juan Bessini
import requests

# Hacer la solicitud a la API
respuesta = requests.get("https://randomuser.me/api")

# Si la respuesta es correcta, obtener los datos
if respuesta.ok:
    usuario = respuesta.json()['results'][0]['name']
    print(f"Nombre: {usuario['first']} {usuario['last']}")
else:
    print("Error al obtener datos")