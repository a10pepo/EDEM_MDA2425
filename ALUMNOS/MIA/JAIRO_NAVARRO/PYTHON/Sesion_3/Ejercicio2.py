import math

#primo con contador


def primo(n:int):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
        
numero = 0       
while numero <= 99:
    numero += 1
    if primo(numero):
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo') 

