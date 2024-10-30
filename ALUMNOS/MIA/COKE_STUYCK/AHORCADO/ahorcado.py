import sys

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

def guess_word_spanish(word):
    """
    Guesses a word in Spanish by brute force iterating through an optimized
    alphabet for this Spanish words.

    The optimized alphabet is based on the frequency of letters in the Spanish
    language.

    Args:
        word: The word to guess.

    Returns:
        int: The number of attempts needed to guess the word.
    """
    guessed_letters = set()
    spanish_optimized_alphabet = "aeirocmdnptlvugzsjbyqhfñxkw"
    attempts = 0

    for letter in spanish_optimized_alphabet:
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter)
        
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
    total_attempts_optimized = 0
    
    print("\nWith the optimized spanish alphabet:\n")
    
    for word in words:
        attempts_optimized = guess_word_spanish(word)
        print(f"Word: {word} - Attempts needed: {attempts_optimized}")
        total_attempts_optimized += attempts_optimized

    print(f"\nTotal attempts needed: {total_attempts_optimized}\n")
    return total_attempts_optimized
    
if __name__ == "__main__":
    main()
