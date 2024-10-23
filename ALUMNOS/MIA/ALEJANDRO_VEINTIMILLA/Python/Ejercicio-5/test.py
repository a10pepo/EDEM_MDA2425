
import requests

respuesta = requests.get("http://api.chucknorris.io/jokes/random")
print(respuesta.status_code)

datos = respuesta.json()

frase_Norris:str=datos["value"]

print(frase_Norris)
