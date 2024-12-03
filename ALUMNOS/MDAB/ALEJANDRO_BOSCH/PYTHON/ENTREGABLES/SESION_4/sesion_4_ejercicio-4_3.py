# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def esBisiesto(año:int):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False

lista_años = list(range(2020,2031))

for año in lista_años:
    resultado = esBisiesto(año)
    print(f"El año {año} es bisiesto?: {resultado}")

