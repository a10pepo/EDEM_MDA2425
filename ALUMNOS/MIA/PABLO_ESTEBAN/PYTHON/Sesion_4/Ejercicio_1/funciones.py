
# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
def es_primo(numero: int) -> bool:
   if numero < 2:
      return False
   else:
    for i in range(2, int(numero ** 0.5 + 1)):
        if numero % i == 0:
            return False
    return True


# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
def get_primos(numeros: list) -> list:
   return [numero for numero in numeros if es_primo(numero)]


# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
def es_bisiesto(anyo: int) -> bool:
   return (anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0))

print(f"Numeros primos entre 1 y 100: {get_primos(range(1, 101))}")
print(f"Año bisiesto (2020): {es_bisiesto(2020)}")