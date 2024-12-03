def es_primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
    
primos = []

for numero in range(1,101):
    if es_primo(numero):
        primos.append(numero)

print("Los números primos del 1 al 100 son: ")
print(primos)

