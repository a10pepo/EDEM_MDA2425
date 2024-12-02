

def es_primo(numero):
    """Función para verificar si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):  # Solo verifica hasta la raíz cuadrada del número
        if numero % i == 0:
            return False
    return True

def primos_en_rango (inicio: int, fin: int):
    for num in range(inicio, fin):
        if es_primo(num):
            print(num, end=" ")

inicio = int(input('Introduce el principio del rango: '))
fin = int(input('Introduce el final del rango: '))

primos_en_rango(inicio, fin)

