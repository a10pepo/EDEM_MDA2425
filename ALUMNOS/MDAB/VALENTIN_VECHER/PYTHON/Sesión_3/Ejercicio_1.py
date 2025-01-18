def menu_inicial():
    print('''
Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
[1] Calcular una inversión
[X] Salir         
 ''')

def c_inversion():
    while True: 
        try:
            capital:float= float(input('''
Introduce el capital inicial (€):        
'''))   
            break
        except:
            print('''
Recuerda que solo se pueden poner números y la coma es este signo (.).
''')
    while True:
        try:
            interes:float= float(input('''
Introduce la tasa de interés anual (%): 
'''))   
            break
        except:
            print('''
Recuerda que solo se pueden poner números y la coma es este signo (.).
                  
''')
    while True:
        try:
            anios= int(input('''
Introduce el numero de años deseados:                
'''))
            break  
        except:
            print('''
Recuerda que solo se pueden poner números y la coma es este signo (.).                 
''')
        
    capital_final= capital*(1 + interes/100)**anios
    interes_obtenido=capital_final-capital

    print(f'''
En {anios} años habrás recibido {interes_obtenido:.2f}€ de interés.

con una cantidad final de:
 _____________________
|  _________________  |
| |                 | |
| |  {capital_final}               
| |_________________| |
|  ___ ___ ___   ___  
| | 7 | 8 | 9 | | + | 
| |___|___|___| |___| 
| | 4 | 5 | 6 | | - | 
| |___|___|___| |___| 
| | 1 | 2 | 3 | | x | 
| |___|___|___| |___| 
| | . | 0 | = | | ÷ | 
| |___|___|___| |___| 
|_____________________

''')
    while True: 
            print('''
¿Qué quieres hacer ahora?
[1] Una nueva elección
[X] Salir              
''')
            eleccion= input('elegir opción: ').strip().upper()

            if eleccion=='1':
                break
            elif eleccion=='X':
                print('''
¡Nos vemos!''')
                exit()
            else:
                print('''
Error, recuerda que solo puedes seleccionar 1 o X: 
''')
def main():
    while True:
        menu_inicial()
        eleccion= input('elige una opción: ').strip().upper()

        if eleccion=='1':
            c_inversion()
        elif eleccion=='X':
            print('''
¡Nos vemos!  
                  ''')
            exit()
        else: 
            print('''
Error, recuerda que solo puedes seleccionar 1 o X:              
''')
            
main()