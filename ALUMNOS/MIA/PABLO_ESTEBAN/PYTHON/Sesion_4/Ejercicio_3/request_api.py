import requests

response = requests.get("https://randomuser.me/api")
data = response.json()

nombre = data["results"][0]["name"]["first"]
last = data["results"][0]["name"]["last"]
print(f"{nombre} {last}")