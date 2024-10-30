import sys
import pg8000
import time
import os

def read_words(file):
    """
    Reads a list of words from a file and returns them in a list.

    Each word should be in a separate line in the file.

    If the file does not exist, prints an error and exits the program.

    Args:
        file: The file to read from.

    Returns:
        list: A list of words.
    """
    try:
        with open(file, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None

def connect_db():
    """
    Connects to the database using the environment variables
    DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, and DB_PORT.

    If the connection fails, it will retry up to 5 times with
    a 5 second delay in between.

    If all retries fail, it will raise the last exception.

    Returns:
        connection: A connection to the database.
    """
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            return pg8000.connect(
                user=os.getenv('DB_USER', 'hangman'),
                password=os.getenv('DB_PASSWORD', 'hangman'),
                database=os.getenv('DB_NAME', 'hangman'),
                host=os.getenv('DB_HOST', 'db'),
                port=int(os.getenv('DB_PORT', 5432))
            )
        except Exception:
            retries += 1
            if retries < max_retries:
                time.sleep(5)
            else:
                raise

def execute_query(conn, query, params=None, max_retries=3):
    """
    Executes a SQL query using the given database connection.
    
    Args:
        conn: The database connection object.
        query: The SQL query to be executed.
        params: Optional parameters to pass with the SQL query.
        max_retries: The maximum number of retry attempts for query execution.
    
    Returns:
        bool: True if the query is executed successfully, otherwise raises an exception.
    
    Raises:
        Exception: If the query execution fails after the maximum number of retries.
    """
    cursor = conn.cursor()
    for _ in range(max_retries):
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return True
        except Exception:
            continue
    raise Exception("Query execution failed")

def create_table(conn):
    """
    Drops the existing 'attempts' table if it exists and creates a new 'attempts' table.

    Args:
        conn: The database connection object.

    The 'attempts' table includes the following columns:
        - id: A unique identifier for each record (auto-incremented).
        - palabra: The word being guessed.
        - letras_acertadas: The letters correctly guessed.
        - letras_falladas: The letters guessed incorrectly.
        - intentos: The number of attempts made.
        - tiempo: The timestamp of when the record was created (defaults to current timestamp).
    
    This function commits the transaction after successfully creating the table.
    """
    execute_query(conn, "DROP TABLE IF EXISTS attempts CASCADE")
    create_table_query = """
    CREATE TABLE attempts (
        id SERIAL PRIMARY KEY,
        palabra VARCHAR(255) NOT NULL,
        letras_acertadas VARCHAR(255) NOT NULL,
        letras_falladas VARCHAR(255) NOT NULL,
        intentos INTEGER NOT NULL,
        tiempo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """
    execute_query(conn, create_table_query)
    conn.commit()

def log_attempt(conn, word, correct_letters, incorrect_letters, attempts):
    """
    Logs a guess attempt in the 'attempts' table.

    Args:
        conn: The database connection object.
        word: The word being guessed.
        correct_letters: The letters correctly guessed.
        incorrect_letters: The letters guessed incorrectly.
        attempts: The number of attempts made.

    Logs the attempt in the 'attempts' table with the given arguments and commits the transaction.
    """
    insert_query = """
    INSERT INTO attempts (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
    VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
    """
    execute_query(conn, insert_query, params=(word, correct_letters, incorrect_letters, attempts))
    conn.commit()

def guess_word_spanish(conn, word):
    """
    Guesses a word in Spanish by iterating through an optimized alphabet and logs each attempt.

    This function uses a predetermined alphabet optimized for Spanish language and this list
    in particular to guess the letters of the given word. It logs each guess attempt to a database
    and returns the total number of attempts required to guess the entire word.

    Args:
        conn: The database connection object used to log each attempt.
        word: The word to be guessed.

    Returns:
        int: The total number of attempts needed to guess the word.
    """
    guessed_letters = set()
    attempts = 0
    alphabet = "aeirocmdnptlvugzsjbyqhfñxkw"
    correct_letters = ""
    incorrect_letters = ""
    
    for letter in alphabet:
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter)
            correct_letters += letter
        else:
            incorrect_letters += letter
        log_attempt(conn, word, correct_letters, incorrect_letters, attempts)
        if all(letter.lower() in guessed_letters for letter in word):
            return attempts
    
    return attempts

def main():
    """
    Main function.

    This function reads the words from the file passed as an argument, and
    prints the number of attempts needed to guess each word using the
    optimized spanish alphabet.

    Args:
        None

    Returns:
        int: The total number of attempts needed to guess all the words.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 ahorcado.py palabras.txt")
        return None
    
    words_file = sys.argv[1]
    words = read_words(words_file)
    total_attempts = 0
    
    conn = connect_db()
    create_table(conn)
    
    for word in words:
        attempts = guess_word_spanish(conn, word)
        total_attempts += attempts
        print(f"Word: {word} - Attempts needed: {attempts}")
    
    print(f"\nTotal attempts needed: {total_attempts}")
    conn.close()

if __name__ == "__main__":
    main()