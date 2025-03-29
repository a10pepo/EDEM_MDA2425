#by Juan Bessini
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("Números primos del 1 al 100:")
primos = [num for num in range(1, 101) if es_primo(num)]
print(primos)
