# A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def es_primo(numero):
    """Función auxiliar que verifica si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Solo hasta la raíz cuadrada de 'numero'
        if numero % i == 0:
            return False
    return True

def mostrar_primos(inicio, fin):
    """
    Muestra por consola los números primos dentro de un rango.
    :param inicio: El inicio del rango.
    :param fin: El final del rango (incluido).
    """
    print(f"Números primos entre {inicio} y {fin}:")
    for num in range(inicio, fin + 1):
        if es_primo(num):
            print(num)

# Ejemplo de uso
mostrar_primos(10, 50)

# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def es_primo(numero):
    """
    Evalúa si un número es primo o no.
    :param numero: Número entero a evaluar.
    :return: True si el número es primo, False en caso contrario.
    """
    if numero < 2:
        return False  # Los números menores que 2 no son primos.
    
    # Verificamos si tiene divisores entre 2 y la raíz cuadrada del número.
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible, no es primo.
    
    return True  # Si no se encontraron divisores, es primo.

# Ejemplo de uso
numero = 29
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

# Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code
'''
En requeriments.txt 
'''

# Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests

def get_name_from_api():
    # URL de la API
    url = "https://randomuser.me/api"
    
    try:
        # Petición GET a la API
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta
        
        # Extraer los datos en formato JSON
        data = response.json()
        user = data["results"][0]  # Extraer el primer resultado
        
        # Obtener nombre y apellidos
        first_name = user['name']['first']
        last_name = user['name']['last']
        
        # Imprimir el nombre y apellidos
        print(f"Nombre completo: {first_name} {last_name}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except KeyError as e:
        print(f"Error al extraer los datos: {e}")

if __name__ == "__main__":
    get_name_from_api()