numero = range(1, 101)
numeros_primos = []

for numerin in numero:
    es_primo = True
    if numerin < 2:
        es_primo = False
    else:
        for i in range(2, numerin):
            if numerin % i == 0:
                es_primo = False
                break

    if es_primo:
        numeros_primos.append(numerin)

print(numeros_primos)