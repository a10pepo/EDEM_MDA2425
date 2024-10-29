import psycopg2

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("palabras.txt") as fichero:
    list_words=fichero.read().splitlines()

conexion = psycopg2.connect(host="localhost", database="Ahorcado", user="postgres", password="Welcome01", port=5432)
print(conexion)
cur = conexion.cursor()

num_iterations = 0
for word in list_words:
    num_successes = 0
    succesful_letters = ''
    error_letters = ''
    for letter in alphabet:
        num_iterations = num_iterations + 1
        if letter in word:
            num_successes = num_successes + word.count(letter)
            succesful_letters = succesful_letters + letter
            if num_successes == len(word):
                print ("Acerté la palabra!")
                break
        else:
            error_letters = error_letters + letter
            
        query = f"INSERT INTO ahorcado (palabra, letras_acertadas, letras_falladas, intentos, tiempo) VALUES ('{word}', '{succesful_letters}', '{error_letters}', {num_iterations}, NOW());"
        cur.execute( query )

print (f"Hemos descifrado todas la palabra en {num_iterations} intentos")

