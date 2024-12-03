print(" Hola. Bienvenido al sistema de cálculo de inversiones (Por el método del interés compuesto).")


while(True):
    try:
       cantidad = int(input("¿Cuánto quieres invertir? "))
       break
    except ValueError:
        print('''
            Disculpe, ha habido algún problema
            Vuelve a introducir la cantidad a invertir deseada... 
              ''')
        

while(True):
    try:
       interes = float(input("¿Cuál es el interés anual? [En términos porcentuales]: "))
       interes = interes/100
       break
    except ValueError:
        print('''
            Disculpe, ha habido algún problema
            Vuelve a introducir el interes anual a utilizar... 
              ''')

while(True):
    try:
        años = int(input("¿Cuántos años vas a mantener la inversión? "))
        break
    except ValueError:
        print('''
            Disculpe, ha habido algún problema
            Vuelve a introducir la cantidad de años que vas a mantener la inversión... 
              ''')

#Fórmula del interés compuesto     
operacion = cantidad *((1 + interes) ** años) - cantidad
        
print(f'En {años} años habrás recibido {operacion}€ de interés')