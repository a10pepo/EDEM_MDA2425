#Pedimos todos los datos necesarios a traves de consola con un try except para capturar errores

try:
    print('Hola. Bienvenido al sistema de cálculo de inversiones')
    Cantidad = int(input(f'¿Cuanto quieres invertir?'))
    Porcentaje= float(input(f'¿Cual es el interes anual?(En decimal)')) 
    Años= int(input(f'¿Cuantos años va a mantener la inversión?'))

#Capturamos el error ValueError si el usuario pone valores distintos a los indicados
except ValueError:
    print('Debes introducir un numero')

#Calculamos el interes compuesto
Total_compuesto = Cantidad * ((1 + Porcentaje / 100) ** Años)

print(f'En {Años} años deberias recibir en intereses {Total_compuesto:.2f} €' )
