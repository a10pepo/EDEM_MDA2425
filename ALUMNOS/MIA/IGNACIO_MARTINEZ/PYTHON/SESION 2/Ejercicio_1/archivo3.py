#Pedir por consola una cantidad (numérica) de Inversión

print("Hola. Bienvenido al sistema de cálculo de inversiones.")
inversion= float(input('Cuanto quieres invertir?\n'))

#Pedir el % de interés anual

interes= float(input('Cual es la tasa de interes anual?\n'))

#Pedir el número de años que se va a mantener la inversión

anios= float(input('Cuantos años vas a invertir?\n'))

#Finalmente, calcular la cantidad generada en los años especificados por el usuario

Ingresos_netos= inversion * (1 + interes/100) ** anios-inversion
print(f'Los ingresos netos son: {Ingresos_netos}')





