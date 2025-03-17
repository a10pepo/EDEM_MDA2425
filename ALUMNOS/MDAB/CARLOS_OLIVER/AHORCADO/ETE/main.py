abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("palabras.txt") as fichero:
    palabras = fichero.read().splitlines()

intentos = 0
aciertos = 0

for palabra in palabras:
    palabra = palabra.upper()
    letras_unicas = set(palabra)
    aciertos_por_palabra = 0
    
    for letra in abecedario:
        intentos += 1

        if letra in letras_unicas:
            print(f"{letra} está en {palabra}")
            aciertos_por_palabra += palabra.count(letra)
            
            if aciertos_por_palabra == len(palabra):
                print(f"Acerté la palabra: {palabra}")
                break
    
    aciertos += aciertos_por_palabra

print(f"Total de intentos: {intentos}")
print(f"Total de aciertos: {aciertos}")