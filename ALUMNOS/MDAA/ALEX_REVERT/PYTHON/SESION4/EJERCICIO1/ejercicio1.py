def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_primos(inicio, fin):
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero)

mostrar_primos(10, 50)