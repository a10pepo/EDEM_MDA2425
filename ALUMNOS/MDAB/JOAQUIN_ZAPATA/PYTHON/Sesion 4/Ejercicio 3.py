import requests # type: ignore
url = 'https://randomuser.me/api/?results=5'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for user in data['results']:
        first_name = user['name']['first']
        last_name = user['name']['last']
        print(f'El nombre y apellido es: {first_name} {last_name}')
else:
    print("Error al obtener los datos.")
