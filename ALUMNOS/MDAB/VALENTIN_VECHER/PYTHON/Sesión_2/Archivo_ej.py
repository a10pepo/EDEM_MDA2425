# Crea una aplicación de consola que calcule los resultados de una inversión. Debe pedir por consola:
    # Una cantidad (numérica) de Inversión
    # Pedir el % de interés anual
    # Pedir el número de años que se va a mantener la inversión
    # Finalmente, calcular la cantidad generada en los años especificados por el usuario

# # while True:
#     try:
#         cantidad: float= float(input(''' 
# Hola. Bienvenido al sistema de cálculo de inversiones.
# ¿Cuánto quiere invertir? '''))
#         try:
#             interes: float= float(input(''' 
# ¿Cuál es el interés anual (en %)? '''))
#             try:
#                 anio: float= float(input('''
# ¿Cuántos años va a mantener la inversión? '''))
#                 break
#             except ValueError:
#                 print("patataque solo se puden poner números y la coma es este signo(.)")
#         except ValueError:
#             print("Oopotatoado. Recuera que solo se puden poner números y la coma es este signo(.)")
#     except ValueError:
#         print("Oops!  No es un valor adecuado. Recuera que solo se puden poner números y la coma es este signo(.)")

# inversion: float=  cantidad + ((cantidad*(interes/100))*anio)

# print(f'''
# la inversion realizada le obtendrá al final de {anio} años la siguiente cantidad: {inversion}''')

print('''
  ____      _            _           _                  
 / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _  
| |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` | 
| |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | 
 \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_| 
 ____     
|  _ \  ___                                             
| | | |/ _ \                                            
| |_| |  __/                                            
|____/ \___|  
 ___                                              
|_ _|_ ____   _____ _ __ ___(_) ___  _ __   ___  ___    
 | || '_ \ \ / / _ \ '__/ __| |/ _ \| '_ \ / _ \/ __|   
 | || | | \ V /  __/ |  \__ \ | (_) | | | |  __/\__ \   
|___|_| |_|\_/ \___|_|  |___/_|\___/|_| |_|\___||___/   
      ''')

while True:
    try:
        cantidad = float(input(''' 
Hola. Bienvenido al sistema de cálculo de inversiones.
¿Cuánto quiere invertir? '''))
        break
    except ValueError:
        print("Recuerda que solo se pueden poner números y la coma es este signo (.).")

while True:
    try:
        interes = float(input(''' 
¿Cuál es el interés anual (en %)? '''))
        break
    except ValueError:
        print("Recuerda que solo se pueden poner números y la coma es este signo (.).")

while True:
    try:
        anio = float(input('''
¿Cuántos años va a mantener la inversión? '''))
        break
    except ValueError:
        print("Recuerda que solo se pueden poner números y la coma es este signo (.).")


inversion: float=  cantidad + ((cantidad*(interes/100))*anio)

print(f'''
la inversion realizada le obtendrá al final de {anio} años {inversion - cantidad}€ de intereses
''')

print(f'''
Obrendrá en total:
 _____________________
|  _________________  
| |     
| |   {inversion}               
| |_________________
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