import math
from sympy import isprime


#primo con rango y biblioteca isprime

for n in range(1,100):
   if isprime(n):
        print(f'{n} es primo')
   else:
        print(f'{n} no es primo')

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

numero = int()
if primo(numero):
    print(f'{numero} es primo')
else:
    print(f'{numero} no es primo')

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

#Primo con rango

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

numero = int()
for numero in range(1,101):
    if primo(numero):
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')