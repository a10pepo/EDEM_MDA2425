
# 1. A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
 
  # 1.1 Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos.

def mostrar_primos(rango_inicio, rango_fin):
    
    for num in range(rango_inicio, rango_fin + 1):
        
        if es_primo(num):
            
            print(num)

  # 1.2 Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no.

def es_primo (num):

  if num < 2: # Si el número es menor que 2, no es primo.

    return False
    
    for num in range (2, num): # Itera desde 2 hasta el número -1.

        if num % i == 0: # Si el número es divisible por 'i', no es primo.

            return False
        
    return True   # Si no encuentra divisores, es primo.

  # 1.3 Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def es_bisiesto(año):
    
  return (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))



# 2. Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code.

# 3. Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests

response = requests.get("https://randomuser.me/api")

data = response.json()

nombre = data ['results'][0]['name']

print (nombre ['first'], nombre ['last'])






