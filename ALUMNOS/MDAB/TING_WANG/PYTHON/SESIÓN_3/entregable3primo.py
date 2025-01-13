## 2
def esPrimo(numero:int) -> None:
    if numero <= 1:
        print(f'{numero} no es primo')
    else:
        for i in range(2, int(numero ** 0.5) +1):
            if numero % i == 0:
             print(f'{numero} no es primo')
             return
    print(f' - {numero} es primo')


if __name__== "entregable3primo.py":
    x = range(1,101)
    for numero in x:
        esPrimo(numero)
    