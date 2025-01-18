
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


with open ('palabras.txt','r') as fichero:
    list_words=fichero.read().splitlines()

numero_intentos=0

for word in list_words: # 2. ITERAR PALABRAS E IMPRIMIR UNA
    aciertos=0
    for letter in alfabeto :
        numero_intentos=numero_intentos +1  #quiero contar como intento tanto si la letra esta en la palabra como si no
        if letter in word:
            print(f'La letra {letter} esta en la palabra {word}')
            aciertos = aciertos + word.count(letter)

            if aciertos == len(word):
                print(f'Acerté la palabra')
                break

print(numero_intentos)
print(aciertos)

import psycopg2
host = "localhost5050"
database="ahorcado"
user="postgres"
password="Welcome01"

try:
    connection = psycopg2.connect(
        host='localhost',
        database='ahorcado',
        user='postgres',
        password='Welcome01',
        port='5050'

    ) # Crear un cursor para ejecutar comandos SQL
    cursor = connection.cursor()

    # Ejecutar una consulta para verificar la conexión
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Conectado a PostgreSQL, versión:", version)


except exception as e :
    print('Ocurro un error al conectar la base de datos:',e)

    
finally:
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()






