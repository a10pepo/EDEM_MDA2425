import requests

llamada = requests.get("http://server:8000")

print(llamada.text)