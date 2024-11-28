with open('palabras.txt', 'r') as fichero:
    palabras = [linea.strip() for linea in fichero.readlines()]  

abecedario = 'eaosrnidlctumpbgvyqhfzjñxkw'

palabraclean = [palabra.lower() for palabra in palabras]

for palabra in palabraclean:
    palabra_descubierta = ['_'] * len(palabra)  
    contador = 0  

    for letraadivinada in abecedario:  
        contador += 1  
        
        if letraadivinada in palabra:  
            for i in range(len(palabra)):
                if palabra[i] == letraadivinada:  
                    palabra_descubierta[i] = letraadivinada
                    
        if '_' not in palabra_descubierta:  
            break 

    # Imprime el resultado
    print(f'Se hicieron {contador} intentos para descubrir la palabra {palabra}')