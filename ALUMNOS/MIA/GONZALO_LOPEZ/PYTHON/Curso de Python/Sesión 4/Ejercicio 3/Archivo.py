# Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests  #importa la libreria para hacer peticion https

response = requests.get('https://randomuser.me/api') #1.Hacer la peticion http a la API de randomuser

#Comprobar que la respuesta sea exitosa
if response.status_code==200:
    data = response.json() # Convertir la respuesta a JSON

    nombre = data['results'][0]['name']['first'] # extraer el nombre del json
    apellido = data['results'][0]['name']['last'] # extraer el apellido del json

    print(f'Nombre:{nombre},apellido : {apellido}')
else:
    print('Error en la peticion',response.status_code)    