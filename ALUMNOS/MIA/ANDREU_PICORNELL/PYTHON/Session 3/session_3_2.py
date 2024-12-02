
def es_primo(num):
    if num < 2:
        return False

    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True

print("Los números primos de 1 a 100 son:")
for num in range(1, 101):
    if es_primo(num):
        print(num)
