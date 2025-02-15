# lista_numeros: list= range(0,101)
# for numero in lista_numeros:
#     print(numero)

# def es_primo(n):
#     if n < 1:
#         return False
#     for n in lista_numeros:
#         for x in n:
#             if x%n==0:
#                 print('el numero no es primo')
#                 return False
#             else:
#                 print('el numero es primo')
#                 return True
        
# print(es_primo())



numero = range(0,101)
numeros_primos= []

for numerin in numero:
    es_primo = True
    if numerin <2:
        es_primo=False 
    else:
        for i in range(2,numerin):
            if numerin%i==0:
                es_primo=False
                break
    if es_primo:
        numeros_primos.append(numerin)

print(f' los numeros siguientes son primos: {numeros_primos}')