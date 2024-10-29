#Ahorcado

palabras= ['MURCIELAGO', 'VIAJE', 'EVADIR', 'ZAPATO', 'CIELO', 'RECREO', 'PIZARRA', 'MATEMATICAS', 'PROGRAMACION', 'ORDENADOR']

abecedario_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Fase 1: Codificación: objetivo de esta fase es conseguir un algoritmo que por fuerza bruta (es decir, probando todas las letras, en el orden del abecedario) adivine las palabra

intentos_totales=0
for palabra in palabras:
    palabra_sinresolver = ['_'] * len(palabra)
    intentos = 0
   
    
    for letraadivinada in abecedario_mayusculas:
        if letraadivinada in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letraadivinada:
                    palabra_sinresolver[i] = letraadivinada
        intentos += 1
        
        if '_' not in palabra_sinresolver:
            break

    intentos_totales+=intentos

    
    palabra_adivinada = ''.join(palabra_sinresolver)
    print(f"Palabra objetivo: {palabra}")
    print(f"Palabra adivinada: {palabra_adivinada}")
    print(f"Número de intentos: {intentos}")
    print("-" * 30)

print(intentos_totales)
    






