# Este programa calcula la rentabiliadd de una inversión 
print('Hola. Bienvenido al sistema de cálculo de inversiones.')

while(True):
    try:
        dinero_invertido = float(input('¿Cuánto quieres invertir?: '))
        break
    except ValueError:
        print('No es un valor adecuado. Prueba de nuevo')

while(True):
    try:
        tipo_interes = float(input('¿Cuál es el interés anual?: ')) 
        break
    except ValueError:
        print('No es un valor adecuado. Prueba de nuevo')

while(True):
    try:
        anios = float(input('¿Cuántos años quieres mantener la inversión?: '))
        break
    except ValueError:
        print('No es un valor adecuado. Prueba de nuevo')

# Cálculo del monto total después de un año con interés compuesto
monto_final = dinero_invertido * ((1 + (tipo_interes / 100)) ** anios)

# Cálculo de los intereses obtenidos
intereses = monto_final - dinero_invertido

print(f'En {anios} año(s), obtendrás {intereses:.2f}€ en intereses.')
