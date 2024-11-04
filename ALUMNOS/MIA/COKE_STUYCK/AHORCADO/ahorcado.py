def read_words():
    """
    Reads words from the file 'palabras.txt' and returns them as a list.

    Each word should be on a separate line in the file. If the file is not found,
    prints an error message and returns None.
    """
    try:
        with open('palabras.txt', 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File 'palabras.txt' not found.")
        return None


def guess_word(word):
    """
    Tries to guess the letters of a given word by iterating through the alphabet.

    Args:
        word (str): The word to guess the letters for.

    Returns:
        int: The number of attempts needed to guess all the letters in the word.
    """
    guessed_letters = set()
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    attempts = 0
    
    for letter in alphabet:
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter)
        
        if all(letter.lower() in guessed_letters for letter in word):
            return attempts
    
    return attempts


def main():
    """
    Main function of the program.

    Reads the words from the file 'palabras.txt' using the function read_words()
    and then tries to guess the letters of each word using the function guess_word().

    Prints the number of attempts needed to guess each word and the total number of attempts.

    Returns:
        int: The total number of attempts needed to guess all the words.
    """
    words = read_words()
    total_attempts = 0
    
    print('')

    for word in words:
        attempts = guess_word(word)
        print(f"Word: {word} - Attempts needed: {attempts}")
        total_attempts += attempts

    print(f"\nTotal attempts needed: {total_attempts}\n")
    return total_attempts


if __name__ == "__main__":
    main()