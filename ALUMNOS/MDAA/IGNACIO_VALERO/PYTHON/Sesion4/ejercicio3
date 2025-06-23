import requests

# Realizar la petición HTTPS
url = "https://randomuser.me/api"
response = requests.get(url)

# Comprobar que la petición fue exitosa
if response.status_code == 200:
    # Parsear la respuesta JSON
    data = response.json()
    
    # Extraer el nombre y apellidos
    nombre = data['results'][0]['name']['first']
    apellido = data['results'][0]['name']['last']
    
    # Mostrar los datos en la consola
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
else:
    print(f"Error en la petición: {response.status_code}")