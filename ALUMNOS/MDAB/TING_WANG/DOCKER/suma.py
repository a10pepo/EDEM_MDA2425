import sys

if len(sys.argv) != 3:
    print("Error, no han introducido valores correctos") 

else:
    numero1 = float(sys.argv[1])
    numero2 = float(sys.argv[2])
    print(f'La suma de {numero1} y {numero2} es {numero1 + numero2}')

