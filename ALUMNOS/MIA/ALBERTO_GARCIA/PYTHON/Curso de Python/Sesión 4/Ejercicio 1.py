
#PARTE 1
def primos(ini:int,fin:int):
    lista_primos=[]
    for a in range(ini,fin):
        b=True
        for n in range(2,a):
            if a % n ==0:
                b=False
        if(b==True):
            lista_primos.append(a)
    print(lista_primos)

primos(1,100)

# PARTE 2
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

# PARTE 3

def esBisiesto(anyo: int):
    if(anyo % 4 == 0 and anyo%100!=0 or anyo%400==0):
        return True
    else:
        return False