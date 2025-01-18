def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos_en_rango(inicio, fin):
    print(f"Números primos entre {inicio} y {fin}:")
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero, end=" ")
    print()

def es_bisiesto(anyo):
    return anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)

mostrar_primos_en_rango(1900, 2025)
print(es_primo(29))  
print(es_bisiesto(2022))