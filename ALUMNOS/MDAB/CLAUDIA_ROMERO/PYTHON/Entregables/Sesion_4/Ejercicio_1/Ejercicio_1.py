# A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def numero_primo(n):
    if n < 2:
        return False
    
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def rango_números(x, y):
    for n in range(x, y + 1):
        if numero_primo(n):
            print(n)

rango_números(1, 100)


# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def numero_primo(n):
    if n < 2:
        return False
    
    for x in range(2, n):  
        if n % x == 0: 
            return False
    
    return True

print(numero_primo(5)) #Comprobación

# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def año_bisiesto(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    else:
        return False

print(año_bisiesto(2004)) #Comprobación
