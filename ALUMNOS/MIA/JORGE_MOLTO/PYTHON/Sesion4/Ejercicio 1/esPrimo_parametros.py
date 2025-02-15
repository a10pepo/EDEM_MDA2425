
def es_primo(numero):
    """Función para verificar si un número es primo."""
    if numero < 2:
        return print(f'{numero} no es primo.')
    for i in range(2, int(numero ** 0.5) + 1):  # Solo verifica hasta la raíz cuadrada del número
        if numero % i == 0:
            return print(f'{numero} no es primo.')
    return print(f'{numero} es primo.')


numero = int(input('Introduce un número para saber si es primo: '))

es_primo(numero)