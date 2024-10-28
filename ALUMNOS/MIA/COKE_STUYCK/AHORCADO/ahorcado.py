import sys
import string
import pg8000
from datetime import datetime

def read_words(file):
    # Reads words from the given file and returns them as a list.
    # Each word should be on a separate line in the file.
    try:
        with open(file, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        sys.exit(1)

def connect_db():
    # Connects to the PostgreSQL database using hardcoded values.
    conn = pg8000.connect(
        user='hangman',
        password='hangman',
        database='hangman',
        host='db',
        port=5432                 # Default PostgreSQL port
    )
    return conn

def create_table():
    # Creates the attempts table in the database if it doesn't exist.
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id SERIAL PRIMARY KEY,
            palabra VARCHAR(255),
            letras_acertadas VARCHAR(255),
            letras_falladas VARCHAR(255),
            intentos INTEGER,
            tiempo TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def log_attempt(word, correct_letters, incorrect_letters, attempts):
    # Logs the guessing attempts in the database
    conn = connect_db()
    cursor = conn.cursor()

    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert the log into the database
    cursor.execute(
        "INSERT INTO attempts (palabra, letras_acertadas, letras_falladas, intentos, tiempo) VALUES (%s, %s, %s, %s, %s)",
        (word, correct_letters, incorrect_letters, attempts, current_time)
    )
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

def guess_word_spanish(word):
    # Guesses the word by brute-forcing through an optimized Spanish alphabet.
    guessed_letters = set()  # Tracks the letters that have been correctly guessed
    attempts = 0

    spanish_optimized_alphabet = "aeirocmdnptlvugzsjbyqhfñxkw"
    
    correct_letters = ""
    incorrect_letters = ""

    for letter in spanish_optimized_alphabet:  # Iterates through the alphabet in order
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter)
            correct_letters += letter
        else:
            incorrect_letters += letter
        
        # Log the attempt
        log_attempt(word, correct_letters, incorrect_letters, attempts)

        # Checks if all letters in the word have been guessed
        if all(letter.lower() in guessed_letters for letter in word):
            return attempts

    return attempts  # Ensures the function always returns attempts

def main():
    # Connect to the database and create the attempts table
    create_table()

    # Checks if the file has been provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 ahorcado.py palabras.txt")
        sys.exit(1)
    
    words_file = sys.argv[1]
    words = read_words(words_file)
    print("\nWith the optimized Spanish alphabet:\n")
    for word in words:
        attempts_optimized = guess_word_spanish(word)
        print(f"Word: {word} - Attempts needed: {attempts_optimized}")
    print("")

if __name__ == "__main__":
    main()
