def es_primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
    
lista_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []

for numero in lista_nums:
    if es_primo(numero):
        primos.append(numero)

print("Los números primos del 1 al 100 son: ")
print(primos)
