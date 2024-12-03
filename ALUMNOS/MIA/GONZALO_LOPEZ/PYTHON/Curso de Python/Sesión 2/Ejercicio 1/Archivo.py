#INTERES SIMPLE 

inversion = int(input('Introduce tu inversion :'))
porcentaje_interes_anual =int(input('Introduce el porcentaje de interes anual :'))
años = int(input('Introduce el numero de años que va durar la inversion :'))

interes_anual = inversion * (porcentaje_interes_anual/100)
total_generado = interes_anual * años

print (f'La cantidad generada en un año seria: {interes_anual} € de interes ')
print(f'La cantidad total generada en {años} años seria: {total_generado} € de interes')

#INTERES COMPUESTO
inversion = int(input('Introduce tu inversion :'))
porcentaje_interes_anual =int(input('Introduce el porcentaje de interes anual :'))
años = int(input('Introduce el numero de años que va durar la inversion :'))

cantidad_final = inversion * (1 + porcentaje_interes_anual/100) ** años
beneficio = cantidad_final - inversion

print(f'El beneficio obtenido despues del interes compuesto durante {años} años es de {beneficio} €')
