
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("palabras.txt") as fichero:
    list_words=fichero.read().splitlines()

num_iterations = 0
for word in list_words:
    num_successes = 0
    for letter in alphabet:
        num_iterations = num_iterations + 1
        if letter in word:
            num_successes = num_successes + word.count(letter)
            if num_successes == len(word):
                print ("Acerté la palabra!")
                break
         
print (f"Hemos descifrado todas la palabra en {num_iterations} intentos")