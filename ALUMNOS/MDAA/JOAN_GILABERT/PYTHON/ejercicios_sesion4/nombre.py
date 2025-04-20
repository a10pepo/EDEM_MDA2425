import requests

def nombre(url):
    try:
        api = requests.get(url)
        api.raise_for_status()  
        json=api.json()
        nombre=json['results'][0]['name']['first']
        apellido=json['results'][0]['name']['last']
        return f'El nombre completo es {nombre} {apellido}'
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return None