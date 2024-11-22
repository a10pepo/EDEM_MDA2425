#AHORCADO GAME made by JBESSINI

import sys
import pg8000.native
con = pg8000.native.Connection("postgres", password="Welcome01")

# Crear una tabla temporal
con.run("CREATE TEMPORARY TABLE Tabla_ahorcado (palabra VARCHAR, letras_acertadas VARCHAR, letras_falladas VARCHAR, intentos VARCHAR, tiempo DATE)")

# Abecedario como lista de letras
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
               "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

abecedario_opt = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", 
                         "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", 
                         "J", "Ñ", "X", "K", "W"]

# Código para leer un archivo y generar una lista con las líneas
# filename = "C:\\Users\\jbessini\\Documents\\GitHub\\EDEM_MDA2425\\ALUMNOS\\MDAA\\JUAN_BESSINI\\AHORCADO\\palabras.txt"
filename = sys.argv[1]

# Leer el archivo y crear la lista
with open(filename, "r") as file:
    palabras = [line.strip() for line in file]

# Imprimir la lista resultante
# print(palabras)

# Empieza el juego
intentos = 0
aciertos = 0
fallos = 0
for palabra in palabras:
    for letra in abecedario:
        intentos +=1 
        if letra in palabra:
            aciertos +=1
        else:
            fallos +=1
# print(intentos)
# print(aciertos)
# print(fallos)

# Empieza el juego
intentos = 0
aciertos = 0
fallos = 0

for palabra in palabras:
    letras_encontradas = set()  # Rastrear letras acertadas
    letras_unicas = set(palabra)  # Letras únicas de la palabra
    
    for letra in abecedario_opt:
        intentos += 1
        
        if letra in palabra:
            aciertos += 1
            letras_encontradas.add(letra)  # Marcar letra como encontrada
            
            # Verificar si todas las letras de la palabra se han encontrado
            if letras_encontradas == letras_unicas:
                break  # Terminar el bucle si la palabra está completa
        else:
            fallos += 1

print(intentos)
# print(letras_encontradas)
# print(letras_unicas)

# Rellenar la tabla
for palabra in ("Ender's Game", "The Magus"):
    con.run("INSERT INTO Tabla_ahorcado (palabra) VALUES (:palabra)", title=title)

# Imprime los valores
for row in con.run("SELECT * FROM book"):
     print(row)
[1, "Ender's Game"]
[2, 'The Magus']

con.close()