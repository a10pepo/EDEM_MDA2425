
# 3.- Crea un programa en Python que sea capaz de identificar 
# a partir de una lista de años si un año es bisiesto o no.

def esBisiesto(año:int):   
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            print(f"El año {año}, es bisiesto") 
        else:   
            print(f"El año {año}, no es bisiesto")

lista_años = list(range(2020,2031))            
    

for año in lista_años:
    esBisiesto(año)