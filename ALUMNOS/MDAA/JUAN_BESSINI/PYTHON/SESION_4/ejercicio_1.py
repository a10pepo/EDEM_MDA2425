# by Juan Bessini

def es_primo(numero):
    """Evalúa si un número es primo o no."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_en_rango(inicio, fin):
    """Muestra por consola los números primos dentro de un rango especificado."""
    print(f"Números primos entre {inicio} y {fin}:")
    primos = [num for num in range(inicio, fin + 1) if es_primo(num)]
    print(primos)

# Ejemplo de uso
primos_en_rango(1, 100)

#########################################

def es_bisiesto(ano):
    """Evalúa si un año es bisiesto o no."""
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Prueba de la función bisiesta
años_prueba = [1900, 2000, 2024, 2025, 2100, 2400]
for año in años_prueba:
    print(f"El año {año} {'es' if es_bisiesto(año) else 'no es'} bisiesto.")
