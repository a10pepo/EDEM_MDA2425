def es_primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False 
    else:
        return True  
    
numero = 2024

if es_primo(numero):
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')

