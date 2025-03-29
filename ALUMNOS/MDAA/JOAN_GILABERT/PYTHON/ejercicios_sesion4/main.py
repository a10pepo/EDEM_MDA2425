'''
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code
Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API
'''
import bisiesto 
import num_primo
import rango_primo
import nombre


print(bisiesto.bisiesto(1950))

print(num_primo.es_primo(5))

print(rango_primo.primo(2, 9))

print(nombre.nombre("https://randomuser.me/api"))

