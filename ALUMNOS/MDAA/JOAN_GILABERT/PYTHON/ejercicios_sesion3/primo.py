'''
Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100
'''

for num in range(2,101):
    es_primo=True
    for div in range(2, num):
        resto=num%div
        if resto==0:
            es_primo=False
            break
    if es_primo:
            print(f'{num} es primo')

   

        
