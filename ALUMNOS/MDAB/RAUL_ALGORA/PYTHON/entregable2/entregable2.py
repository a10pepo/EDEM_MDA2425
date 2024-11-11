x= int(input('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir?'))
y= float(input('¿cual es el interes anual?'))
z= int(input('¿cuantos años vas a mantener la inversión'))

def interes(x, y, z):
    interes_generado= x * (1+y) ** z
    print(f'En {z} años habras generado {interes_generado} euros')

interes(x, y, z)
