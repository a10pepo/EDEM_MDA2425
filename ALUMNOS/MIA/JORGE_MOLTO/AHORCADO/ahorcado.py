
# Obtener la lista de palabras del fichero
import sys

name_fichero = sys.argv[1] if len(sys.argv) > 1 else 'palabras.txt'
fichero = open(name_fichero, 'r')  # Abrir en modo lectura
palabras = []
abcdario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n' , 'ñ' ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
    
for line in fichero:
    line = line.replace("\n", "")
    palabras.append(line) 

# Procesar el fichero...
fichero.close()  # Cerrar el fichero

n_intentos = 0
aciertos = 0

for palabra in palabras: 
    for letra in abcdario:
        n_intentos += 1
        if letra in palabra:
            print(f'La {letra} esta en {palabra}')
            aciertos = aciertos + palabra.count(letra)
            print(f'llevas {aciertos} aciertos y hay {len(palabra)} letras')
            if (aciertos == len(palabra)):
                print(f'{palabra} ACERTADA.')
                aciertos = 0
                break
        
print(f'Intentos: {n_intentos}')



'''
for palabra in palabras: 

    print(f'La palabra a acertar es: {palabra}')

    letras = []
    n_letras = len(palabra)
    intentando = True
    acierto = 0

    for letra in palabra: 
        letras.append(letra)
    
    while(intentando):
        if(intentando == False): break
        for letra_abc in abcdario: 
            n_intentos += 1
            if(intentando == False): break
            for letra_palabra in letras:
                if(letra_palabra == letra_abc):
                    acierto += 1
                if (acierto == n_letras):
                    intentando = False
                    print(f'Has necesitado {n_intentos} para solucionar {palabra}')
                    break
print(f'Has necesitado {n_intentos}')'''