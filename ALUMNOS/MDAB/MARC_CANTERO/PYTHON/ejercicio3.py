# 3. Ejercicios Sesión 3
# A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

decision=input("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?\n > [1] Calcular una inversión\n > [X] Salir\n >")
if decision == "1":
   inversion = float(input("Hola. Bienvenido al sistema de cálculo de inversiones. \n¿Cuánto quieres invertir? (€) ->"))
   interes = float(input("¿Cuál es el interés anual? (%) ->"))
   anyos = int(input("¿Cuántos años vas a mantener la inversión? ->"))
   ganancia = float(((inversion*(interes / 100))*anyos))

   print (f"En {anyos} años habrás recibido {ganancia}€ de interés") 

elif decision == "X":
   print("¡Hasta pronto!")
else:
   print("Valor incorrecto")


# Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1-100

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_hasta_100():
    print("Números primos del 1 al 100:")
    for numero in range(1, 101):
        if es_primo(numero):
            print(numero, end=" ")

if __name__ == "__main__":
    primos_hasta_100()

