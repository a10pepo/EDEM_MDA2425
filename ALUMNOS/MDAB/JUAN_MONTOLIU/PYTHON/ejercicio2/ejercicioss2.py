print("BIENVENIDO AL SISTEMA PARA CALCULAR TU INVERSION")

def intereses(inversion0, interes, periodo):
    cuota = (inversion0 * (interes/100) * periodo)
    return cuota


inversion0 = int(input(f"Introduzca la cantidad que desee invertir inicialmente: "))
while True:
    interes = float(input(f"Que tipo de interes desearía: "))
    if 0<= interes <=100:
        break
    else:
        print(f"Error el interes debe estar comprendido entre 0 y 1. Vuelva a intentarlo")
periodo = int(input(f"Cuantos años desearía invertir en el producto: "))

cuotapers = (intereses(inversion0, interes, periodo))

print(f"En {periodo} años habrás obtenido {cuotapers}€ en intereses")

