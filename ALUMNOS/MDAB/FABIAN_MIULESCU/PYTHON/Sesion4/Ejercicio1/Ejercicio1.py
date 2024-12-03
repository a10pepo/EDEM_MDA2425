# Función que recibe un rango, verifica si un número es primo y muestra los primos en el rango
def mostrar_primos_rango(inicio, fin):
    print(f"Números primos entre {inicio} y {fin}:")
    for num in range(inicio, fin + 1):
        es_primo = True
        if num < 2:
            es_primo = False
        else:
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break
        
        if es_primo:
            print(num, end=" ")

#----------------------------------------------------------------------------------------

# Función para evaluar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

#----------------------------------------------------------------------------------------

# Función para evaluar si un año es bisiesto
def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False