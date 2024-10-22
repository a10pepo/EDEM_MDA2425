import requests

response = requests.get('https://randomuser.me/api')

if response.status_code == 200:
    data = response.json()
    
    usuario = data['results'][0]
    
    nombre = usuario['name']['first']
    apellido = usuario['name']['last']
    
    print(f"Nombre: {nombre} {apellido}")
else:
    print(f"Error en la petición. Código de estado: {response.status_code}")
