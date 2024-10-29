import sys

def adivinar_palabras(archivo):
    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_intentos = 0
    
    with open(archivo, 'r') as f:
        for palabra in f:
            palabra = palabra.strip().upper()
            palabra_actual = ['_'] * len(palabra)
            letras_bien = ""
            letras_mal = ""
            intentos = 0

            for letra in abecedario:
                if '_' not in palabra_actual:
                    break
                fallo = True
                for i, caracter in enumerate(palabra):
                    if caracter == letra:
                        palabra_actual[i] = letra
                        fallo = False
                if fallo:
                    letras_mal += letra
                else:
                    letras_bien += letra
                intentos += 1

            total_intentos += intentos    
            print(f"\nPalabra '{palabra}' adivinada en {intentos} intentos.")
            print(f"Letras bien {letras_bien}")
            print(f"Letras bien {letras_mal}")
    print(f"\nTotal de intentos utilizados en todas las palabras: {total_intentos}")
    
file = sys.argv[1]
adivinar_palabras(file)