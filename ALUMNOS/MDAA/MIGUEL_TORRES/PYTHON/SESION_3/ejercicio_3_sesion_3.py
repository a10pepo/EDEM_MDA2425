def es_bisiesto(año):
    """Determina si un año es bisiesto."""
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def identificar_años_bisiestos(lista_años):
    """Identifica y muestra los años bisiestos de una lista."""
    for año in lista_años:
        if es_bisiesto(año):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")

# Lista de años a analizar
años = [1900, 2000, 2004, 2023, 2024, 2100]

# Ejecutar la función
identificar_años_bisiestos(años)