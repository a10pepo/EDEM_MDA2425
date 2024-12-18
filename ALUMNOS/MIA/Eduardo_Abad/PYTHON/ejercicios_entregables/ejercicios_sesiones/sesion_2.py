print('Hola. Bienvenido al sistema de cálculo de inversiones.')

cantidad_inicial=float(input('¿Cuánto dinero quieres invertir? '))
interés_anual=int(input('¿Cuál es el interés anual? '))/100
años=int(input('¿Cuántos años vas a mantener la inversión? '))
dinero_acumulado=cantidad_inicial*(1+interés_anual)

for i in range(años):
    dinero_acumulado=dinero_acumulado*(1+interés_anual)
    
print(f'En {años} años habrás recibido {dinero_acumulado:.2f}€ de interés')
