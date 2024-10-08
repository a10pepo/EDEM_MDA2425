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
    print("Dime un intervalo de valores.")

    num1: int = int(input("Num 1: "))
    num2: int = int(input("Num 2: "))

    if(num1>num2):
        sup: int = num1
        inf: int = num2
    else:
        sup: int = num2
        inf: int = num1
    
    mostrar_primos(inf,sup)