#from ...Sesión_3.Ejercicio2.Ejercicio2 import Num_primo
#No entiendo el porque no me lee la función. Me pone ModuleNotFoundError: No module named 'Sesión_3'
def Num_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):  
        if numero % i == 0:
            return False
    return True

inicio = int(input("¿Desde que número quiere usted comprobar si es primo?"))
final = int(input("¿Hasta que número quiere comprobar si es primo?"))

print("Números primos del {inicio} al {final}:")
for num in range(inicio, final):
    if Num_primo(num):
        print(num, end=" ")
