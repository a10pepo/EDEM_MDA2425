print('Hola. Bienvenido al sistema de calculo de inversiones')
# Definiendo las variables #
monto_inversion= float(input('¿Cuanto quieres invertir? :' ))
interes= float(input('¿Que porcentaje quieres invertir? Debe estar comprendido entre 0 y 1:' ))
anios= int(input('¿Cuantos años lo quieres mantener?:' ))

# Cálculo para saber cuánto interes generamos en años #

interes_simple= monto_inversion*interes*anios
print('El interes en años es:', interes_simple)






