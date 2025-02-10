"""
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
- Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
- Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
- Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
"""

# Función para recibir un rango de números como parámetros y que muestre los primos
def primos(numbers):
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, num):
                if num % i == 0:
                    break
        else:
            print(num)

# Función para saber si un número es primo o no
def primo(number):
    if number < 2:
        return  
    for i in range(2, number):
        if number % i == 0:
            return
    print(number)


# Función para saber si un año es bisiesto
def bisiesto(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'El año {year} es bisiesto')
    else:
        print(f'El año {year} no es bisiesto')
