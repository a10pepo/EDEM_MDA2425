
# Inicializar una lista
lista_palabras = []

# Abrir el archivo y leerlo
with open('palabras.txt', 'r') as archivo:
    for palabra in archivo:
        # Agregar la línea a la lista, eliminando el salto de línea
        lista_palabras.append(palabra.strip())

alfabeto ='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

contador_intentos = 0
acierto = 0

for palabra in lista_palabras:
    for letra_intento in alfabeto:
        contador_intentos += 1
        if letra_intento in palabra:
            acierto = acierto + palabra.count(letra_intento)
            if acierto == len(palabra):
                acierto = 0
                break

print(f'El numero de intentos es {contador_intentos}')
