import requests


def peticion(): 
    response = requests.get("https://randomuser.me/api")
    if response.status_code == 200:
        data = response.json()
        nombre = data['results'][0]['name']['first']
        apellidos = data['results'][0]['name']['last']
        print(f"Nombre: {nombre}, Apellidos: {apellidos}")
    else:
        print("Error al obtener el usuario.")


peticion()