import time
import sys

import pg8000.native


con = pg8000.native.Connection("postgres", password = "Welcome01", host = "postgres")

try:
    aux = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    contador = 0
    with open(sys.argv[1],"r") as archivo:
        inicio = time.time()
        for linea in archivo:
            lista_de_letras = ''
            contador_linea = 0 
            Ultima_pos_letra = 0
            for j in aux:
                contador_linea += 1
                if j in linea and j not in lista_de_letras:
                    Ultima_pos_letra = contador_linea
                    lista_de_letras += j
            contador += Ultima_pos_letra
            con.run("INSERT INTO ahorcado (palabras, letras_acertadas, letras_fallidas, intentos) VALUES (:palabras, :letras_acertadas, :letras_falladas, :intentos)",
                    palabras=linea, letras_acertadas=lista_de_letras, letras_falladas='', intentos= contador_linea)
        fin = time.time()
        tiempo = fin - inicio
        print('Contador total =' + str(contador) + ', tiempo =' + str(tiempo))
        inicio2 = time.time()
        for linea in archivo:
            max = 0
            for i in linea:
                num = aux.index(i)
                if max < num:
                    max = num
            contador += max
        fin2 = time.time()
        tiempo = fin2 - inicio2        
        print('Contador total =' + str(contador) + ', tiempo =' + str(tiempo))
except FileNotFoundError:
    print("El archivo no existe.")