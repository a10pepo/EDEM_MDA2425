import sys
import string
import pg8000
from datetime import datetime
import time
import os

def read_words(file):
    try:
        with open(file, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        sys.exit(1)

def connect_db(max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            print(f"Attempting to connect to database (attempt {retries + 1}/{max_retries})...")
            conn = pg8000.connect(
                user=os.getenv('DB_USER', 'hangman'),
                password=os.getenv('DB_PASSWORD', 'hangman'),
                database=os.getenv('DB_NAME', 'hangman'),
                host=os.getenv('DB_HOST', 'db'),
                port=int(os.getenv('DB_PORT', 5432))
            )
            print("Successfully connected to database!")
            return conn
        except Exception as e:
            print(f"Database connection error: {str(e)}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Could not connect to database.")
                raise

def execute_with_retry(cursor, query, params=None, max_retries=3):
    """Execute a query with retry logic"""
    for attempt in range(max_retries):
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return True
        except Exception as e:
            print(f"Query execution failed (attempt {attempt + 1}/{max_retries}): {str(e)}")
            if attempt == max_retries - 1:
                raise
            time.sleep(1)

def create_table():
    conn = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        print("Creating attempts table if it doesn't exist...")
        
        # Drop existing table
        execute_with_retry(cursor, "DROP TABLE IF EXISTS attempts CASCADE")
        
        # Create new table
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
        execute_with_retry(cursor, create_table_query)
        
        # Commit the transaction
        conn.commit()
        print("Table creation successful!")
        
        # Verify table exists and is empty
        execute_with_retry(cursor, "SELECT COUNT(*) FROM attempts")
        count = cursor.fetchone()[0]
        print(f"Verified: Table exists and contains {count} rows")
            
    except Exception as e:
        print(f"Error in create_table: {str(e)}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

def log_attempt(word, correct_letters, incorrect_letters, attempts):
    conn = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Begin transaction explicitly
        cursor.execute("BEGIN")
        
        insert_query = """
        INSERT INTO attempts (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
        VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
        RETURNING id
        """
        
        # Execute insert with retry logic
        execute_with_retry(cursor, insert_query, 
                         (word, correct_letters, incorrect_letters, attempts))
        
        # Fetch the returned ID
        result = cursor.fetchone()
        if not result:
            raise Exception("Insert did not return an ID")
        
        inserted_id = result[0]
        
        # Verify the insert within the same transaction
        verify_query = "SELECT id FROM attempts WHERE id = %s"
        execute_with_retry(cursor, verify_query, (inserted_id,))
        
        if not cursor.fetchone():
            raise Exception("Verification failed - inserted row not found")
        
        # If we get here, everything worked, so commit the transaction
        conn.commit()
        print(f"Successfully inserted and verified row with ID {inserted_id}")
        
        return True
            
    except Exception as e:
        print(f"Error in log_attempt: {str(e)}")
        if conn:
            try:
                conn.rollback()
                print("Transaction rolled back")
            except Exception as rollback_error:
                print(f"Error during rollback: {str(rollback_error)}")
        return False
    finally:
        if conn:
            try:
                conn.close()
                print("Connection closed")
            except Exception as close_error:
                print(f"Error closing connection: {str(close_error)}")

def guess_word_spanish(word):
    guessed_letters = set()
    attempts = 0
    spanish_optimized_alphabet = "aeirocmdnptlvugzsjbyqhfñxkw"
    correct_letters = ""
    incorrect_letters = ""
    
    for letter in spanish_optimized_alphabet:
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter)
            correct_letters += letter
        else:
            incorrect_letters += letter
        
        if not log_attempt(word, correct_letters, incorrect_letters, attempts):
            print(f"Failed to log attempt for word {word}, letter {letter}")
        else:
            print(f"Successfully logged attempt for word {word}, letter {letter}")
        
        if all(letter.lower() in guessed_letters for letter in word):
            return attempts
    
    return attempts

def verify_data_in_database():
    """Verify data exists in the database"""
    conn = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Check row count
        cursor.execute("SELECT COUNT(*) FROM attempts")
        count = cursor.fetchone()[0]
        print(f"\nTotal records in database: {count}")
        
        if count > 0:
            # Show some sample data
            cursor.execute("SELECT * FROM attempts ORDER BY id LIMIT 5")
            rows = cursor.fetchall()
            print("\nSample records:")
            for row in rows:
                print(row)
        
        return count > 0
            
    except Exception as e:
        print(f"Error verifying database: {str(e)}")
        return False
    finally:
        if conn:
            conn.close()

def main():
    print("Starting Hangman game with database logging...")
    
    try:
        create_table()
    except Exception as e:
        print(f"Failed to create table: {str(e)}")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python3 ahorcado.py palabras.txt")
        sys.exit(1)
    
    words_file = sys.argv[1]
    words = read_words(words_file)
    print(f"\nRead {len(words)} words from file")
    
    for word in words:
        print(f"\nProcessing word: {word}")
        try:
            attempts_optimized = guess_word_spanish(word)
            print(f"Word: {word} - Attempts needed: {attempts_optimized}")
        except Exception as e:
            print(f"Error processing word {word}: {str(e)}")
    
    # Verify final database state
    print("\nVerifying final database state...")
    if verify_data_in_database():
        print("Data successfully stored in database")
    else:
        print("No data found in database after processing")
    
    print("\nGame completed!")

if __name__ == "__main__":
    main()