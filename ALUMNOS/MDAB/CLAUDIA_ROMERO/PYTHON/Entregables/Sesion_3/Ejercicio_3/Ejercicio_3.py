#Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

años = list(range(2000, 2024))

def año_bisiesto(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    else:
        return False
    
for n in años:
    if año_bisiesto(n):
        print(n)