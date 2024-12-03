def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos(inf, sup):
    for numero in range(inf,sup+1):
        if es_primo(numero):
            print(f"El número {numero} es primo")


if __name__=="__main__":
    mostrar_primos(1,100)