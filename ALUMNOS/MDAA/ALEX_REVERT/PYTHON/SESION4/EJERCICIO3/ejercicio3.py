import requests

def obtener_usuario_aleatorio():
    url = "https://randomuser.me/api"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        usuario = data['results'][0]
        nombre = usuario['name']['first']
        apellidos = usuario['name']['last']
        print(f"Nombre: {nombre}, Apellidos: {apellidos}")
    else:
        print("Error al realizar la petición")

if __name__ == "__main__":
    obtener_usuario_aleatorio()