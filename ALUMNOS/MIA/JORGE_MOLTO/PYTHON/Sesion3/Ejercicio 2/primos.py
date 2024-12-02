
def es_primo(numero):
    """Función para verificar si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):  # Solo verifica hasta la raíz cuadrada del número
        if numero % i == 0:
            return False
    return True

# Generar e imprimir los números primos del 1 al 100
print("Números primos del 1 al 100:")
for num in range(1, 101):
    if es_primo(num):
        print(num, end=" ")
