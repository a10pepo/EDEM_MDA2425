
def calcular_inversion(inversion, interes, años):
    inversion_final = inversion * (1 + interes/100) ** años
    return inversion_final


def main():
    try:
        inversion = float(input("¿Cuánto quieres invertir?: "))
        interes = float(input("¿Cuál es el interés anual?: "))
        años = int(input("¿Cuántos años vas a mantener la inversión?: "))
        inversion_generada = calcular_inversion(inversion, interes, años)
        interes_generado = inversion_generada - inversion
        print(f"En {años} años habrás recibido {interes_generado:.2f}€ de interés")

    except ValueError:
        print("Error: Introduce un número válido")  

if __name__ == "__main__":
    main()   
