import os
import time
import string

def leer_palabras():
    """Lee las palabras desde el archivo palabras.txt"""
    archivo = "palabras.txt"
    if not os.path.exists(archivo):
        print(f"Error: No se encontró el archivo {archivo}")
        return []
    with open(archivo, "r", encoding="utf-8") as f:
        return [line.strip().upper() for line in f.readlines()]

def jugar_ahorcado(palabra):
    """Simula el juego del ahorcado probando cada letra del abecedario"""
    letras_acertadas = ""
    letras_falladas = ""
    intentos = 0
    abecedario = string.ascii_uppercase  # A-Z en mayúsculas
    
    for letra in abecedario:
        intentos += 1
        if letra in palabra:
            letras_acertadas += letra
        else:
            letras_falladas += letra
        
        # Si hemos adivinado la palabra, terminamos
        if set(letras_acertadas) == set(palabra):
            break
    
    return palabra, letras_acertadas, letras_falladas, intentos, time.strftime("%Y-%m-%d %H:%M:%S")

def main():
    palabras = leer_palabras()
    if not palabras:
        return
    
    print("Iniciando el juego del ahorcado...")
    
    resultados = []
    for palabra in palabras:
        resultado = jugar_ahorcado(palabra)
        resultados.append(resultado)
        print(f"Palabra: {resultado[0]}, Intentos: {resultado[3]}, Acertadas: {resultado[1]}, Falladas: {resultado[2]}")
    
    print("\nResumen de resultados:")
    for res in resultados:
        print(f"{res[0]} - Intentos: {res[3]}, Acertadas: {res[1]}, Falladas: {res[2]}, Fecha: {res[4]}")

if __name__ == "__main__":
    main()

