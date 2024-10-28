#3. Ejercicios Sesión 3
#   2.Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100


primo=[2,3,5]
rango=range(6,100)

for i in rango:
    for x in primo:
        if i % x == 0:
            break
        elif x==primo[-1]:
            primo.append(i)
print("La siguiente lista contiene todos los números primos del 1 al 100")
print(primo)
 