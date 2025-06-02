import requests
r = requests.get("https://randomuser.me/api")
data = r.json()
resultados = data['results']
for i in resultados:
    ie = i
monsieur = ie["name"]["title"]
nombre = ie["name"]["first"]
apellido = ie["name"]["last"]
print(f"{monsieur} {nombre} {apellido}")