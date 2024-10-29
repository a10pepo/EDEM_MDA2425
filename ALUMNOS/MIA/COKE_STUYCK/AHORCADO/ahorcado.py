import string

def read_words():
    # Reads words from the given file and returns them as a list.
    # Each word should be on a separate line in the file.

    try:
        with open('palabras.txt', 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File 'palabras.txt' not found.")
        return

def guess_word(word):
    # Guesses the word by brute-forcing through all the letters of the alphabet.
    # Returns the number of attempts needed to guess the word.

    guessed_letters = set()  # Tracks the letters that have been correctly guessed
    attempts = 0

    alphabet = string.ascii_lowercase
    
    for letter in alphabet:  # Iterates through the alphabet in order
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter)
        
        # Checks if all letters in the word have been guessed
        if all(letter.lower() in guessed_letters for letter in word):
            return attempts
    
    return attempts  # Ensures the function always returns attempts


def main():
    
    words = read_words()
    print('')

    total_attempts = 0
    for word in words:
        attempts = guess_word(word)
        print(f"Word: {word} - Attempts needed: {attempts}")
        total_attempts += attempts

    print(f"\nTotal attempts needed: {total_attempts}\n")
    

if __name__ == "__main__":
    main()
