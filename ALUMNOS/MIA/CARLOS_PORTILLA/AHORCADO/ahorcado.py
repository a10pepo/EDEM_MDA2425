import os

# Obtener el directorio del archivo actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa a palabras.txt
ruta_archivo = os.path.join(directorio_actual, "palabras.txt")

# Abrir el archivo usando la ruta completa
lista = []
with open(ruta_archivo, "r") as palabras:
    for _ in palabras.readlines():
        lista.append(_) 
# Hecho con chatgpt hasta aquí porque no cargaba el archivo de texto

lista_palabras = []
for palabra in lista:
    lista_palabras.append(palabra.strip().lower())

letrita = ['e', 'a', 'o', 's', 'n', 'r', 'i', 'd', 'l', 't','c', 'u', 'p', 'm', 'b', 'g', 'v', 'h', 'y', 'q','f', 'z', 'j', 'x', 'k', 'w']

total_intentos = 0

for adivina in lista_palabras:
    intentos = 0
    estado_actual = ["_"] * len(adivina)
    for letra in letrita:
        intentos += 1
        total_intentos += 1 
        if letra in adivina:
            for i in range(len(adivina)):
                if adivina[i] == letra:
                    estado_actual[i] = letra
        print(f"Intento {intentos}: Letra '{letra}' - Estado: {''.join(estado_actual)}")
        if estado_actual == list(adivina):
            print(f"¡Palabra adivinada '{adivina}' en {intentos} intentos!")
            break
    else:
        print(f"No se adivinó la palabra '{adivina}'. Estado final: {''.join(estado_actual)}")

print(f"Número total de intentos realizados: {total_intentos}")
