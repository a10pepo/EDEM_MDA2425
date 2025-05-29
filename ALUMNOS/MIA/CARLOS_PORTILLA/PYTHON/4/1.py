# PARTE 1
def lista_primos():
    numeros = input("Dame una lista de números separados por comas: ").replace(" ", "").split(",")
    lista = []
    for num in numeros:
        lista.append(int(num))

    numeros_primos = []
    for num in lista:
        es_primo = True
        if num < 2:
            es_primo = False
        else:
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break
        if es_primo:
            numeros_primos.append(num)
    print(sorted(numeros_primos))

lista_primos()

# PARTE 2
def es_primo(num:int):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numero = int(input("Dame un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")

# PARTE 3
def year():
    anyo = int(input("Dime un año: "))
    if anyo % 4 == 0:
        return True
    else:
        return False

resultado = year()
print(resultado)
