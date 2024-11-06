
#Apartado 1
# def numeros_primos (inicio, fin):
#     print(f'Los numeros primos entre {inicio} y {fin} son:')
#     for num in range (inicio,fin+1): #Range=Rango
#         if num <= 1:
#             continue
#         for i in range(2, num):
#             if num % i ==0:
#                 break
#         else:
#             print(num)
    
# numeros_primos(1,100)




# #Apartado 2

# def es_primo(num):
#      for n in range (2, num):
#           if num % n ==0:
#                print(f'El numero {num} no es primo')
#                return False
#           else:
#                print(f'El numero {num} es primo')
#                return True
       
# es_primo(4)


#Apartado 3

def es_bisiestos(año):
    
    if( año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
        
    else:
        return False
       
print(es_bisiestos(2100))