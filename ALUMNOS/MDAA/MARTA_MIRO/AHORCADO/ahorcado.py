import sys

# Crear el diccionario con las letras del abecedario
diccionario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Ruta del archivo de texto
ruta_archivo = 'C:/Users/marta/Desktop/palabras.txt'

# Leer el archivo y guardar las palabras en una variable
try:
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    palabras = [linea.strip().upper() for linea in lineas]
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {ruta_archivo}.")
    exit()

# Variable para acumular el total de intentos
total_intentos = 0

# Procesar cada palabra
for palabra in palabras:
    intentos = 0
    descubierta = set()  # Conjunto para almacenar letras adivinadas
    palabra_original = palabra  # Guardamos la palabra original para no cambiarla
    print(f"\nProcesando palabra: {palabra}")
    
    # Contar cuántas veces aparece cada letra en la palabra
    contador_letras = {letra: palabra.count(letra) for letra in set(palabra)}
    
    # Longitud total de la palabra (número de letras que faltan por adivinar)
    longitud = len(palabra)
    
    # Probar todas las letras del diccionario (26 intentos por palabra)
    for letra in diccionario:
        if letra in palabra and letra not in descubierta:  # Si la letra está en la palabra y no se ha adivinado
            intentos += 1
            # Restamos la cantidad de veces que aparece la letra de la longitud total
            cantidad_acertada = contador_letras[letra]
            longitud -= cantidad_acertada
            print(f"Letra '{letra}': Acierto")
            
            # Añadir la letra al conjunto de letras adivinadas
            descubierta.add(letra)
        elif letra not in palabra:
            intentos += 1
            print(f"Letra '{letra}': Fallo")
        
        # Si ya se han adivinado todas las letras, se puede salir del bucle
        if longitud == 0:
            break  # Salir del bucle porque la palabra ha sido adivinada
    
    print(f"Palabra '{palabra}' adivinada en {intentos} intentos.")
    
    # Acumular los intentos totales
    total_intentos += intentos

# Imprimir el total de intentos
print(f"\nTotal de intentos para adivinar todas las palabras: {total_intentos}")

letras_falladas = []  # Lista para almacenar letras falladas
letras_falladas.append(letra)  # Añadir la letra fallida a la lista
letras_falladas="".join(letras_falladas),  # Convertir lista de letras fallidas en una cadena

from datetime import datetime
tiempo = datetime.now()  # Capturar la hora actual
tiempo=tiempo,  # Tiempo actual como parte de los valores a insertar


import pg8000.native
con = pg8000.native.Connection("postgres", password="Welcome01")


con.run("""
    INSERT INTO intentos_adivinacion (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
    VALUES (:palabra, :letras_acertadas, :letras_falladas, :intentos, :tiempo)
""", 
palabra=palabra, 
letras_acertadas=cantidad_acertada, 
letras_falladas=letras_falladas, 
intentos=intentos, 
tiempo=tiempo)
 
 