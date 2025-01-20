def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Solo comprobamos hasta la raíz cuadrada
        if numero % i == 0:
            return False
    return True

def primos_hasta_100():
    primos = [num for num in range(1, 101) if es_primo(num)]  # Generamos la lista de números primos
    print("Números primos entre 1 y 100:")
    print(primos)

# Ejecutar la función
primos_hasta_100()