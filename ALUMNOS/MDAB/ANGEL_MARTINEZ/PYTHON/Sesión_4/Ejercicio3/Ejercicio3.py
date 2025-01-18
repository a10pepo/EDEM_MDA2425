import requests
random = requests.get("https://randomuser.me/api")
name = random.json()

#print(name)

nombre = name["results"][0]["name"]["title"]
primer_apellido = name["results"][0]["name"]["first"]
segundo_apellido = name["results"][0]["name"]["last"]

print(f"El nombre es {nombre} {primer_apellido} {segundo_apellido}")