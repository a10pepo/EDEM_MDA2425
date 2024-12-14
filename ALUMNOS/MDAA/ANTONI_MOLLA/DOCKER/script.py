import sys

print('Bienvenido al programa de sumas')

def sumatorio (a,b):
    Suma= a+b
    print(f'La suma de estos números es {Suma}')

if len(sys.argv) != 3:

    print("Introduza solo dos números")


else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    sumatorio(num1, num2)
