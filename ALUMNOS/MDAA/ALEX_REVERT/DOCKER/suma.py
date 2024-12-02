import sys

def sumar_dos_numeros (num1, num2):
    
 try:
        num1 = float(num1)
        num2 = float(num2)
        resultado = num1 + num2
        print(f'La suma de {num1} y {num2} es : {resultado}')
 except ValueError:  
        print('Por favor, introduzca valores numéricos válidos.') 


if len(sys.argv) != 3:
    print('Por favor, introduzca dos números.')
else:
    sumar_dos_numeros(sys.argv[1], sys.argv[2])    

     


 
