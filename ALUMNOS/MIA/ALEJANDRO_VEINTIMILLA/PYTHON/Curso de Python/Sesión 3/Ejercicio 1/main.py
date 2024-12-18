#3. Ejercicios Sesión 3
#   1.A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.


exit=False
x=False
print("Hola. Bienvenido al sistema de cálculo de inversiones.")
while exit==False:
    if x==True:
        print("¿Qué quieres hacer ahora?")
    else:
        print("¿Qué desea hacer?:")
    print("[1] Calcular una inversión")
    print("[X] Salir")
    respuesta=input()

    if respuesta=="1":
        x=True
        print("¿Cuanto dinero deseas invertir?")
        money = int(input())

        print("¿Cuál es el interés anual?")
        interest = float(input())

        print("¿Cuántos años vas a mantener la inversión?")
        year = int(input())
        profit= round((money*(1+interest)**year)-money, 2)
        print(f"En {year} años habrás recibido {profit}€ de interés")

    elif respuesta=="X" or respuesta=="x":
        print("¡Nos vemos!")
        break

