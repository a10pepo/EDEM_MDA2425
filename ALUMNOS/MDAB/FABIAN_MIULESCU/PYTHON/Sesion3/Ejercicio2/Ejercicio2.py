print("Números primos entre 1 y 100:")

for num in range(1, 101):
    es_primo = True
    if num < 2:
        es_primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
    
    if es_primo:
        print(num, end=" ")
