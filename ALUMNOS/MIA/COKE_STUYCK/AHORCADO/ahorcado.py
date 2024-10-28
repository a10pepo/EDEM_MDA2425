import sys
import string

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

def guess_word(word):
    # Guesses the word by brute-forcing through all the letters of the alphabet.
    # Returns the number of attempts needed to guess the word.

    guessed_letters = set()  # Tracks the letters that have been correctly guessed
    attempts = 0
    
    for letter in string.ascii_lowercase:  # Iterates through the alphabet in order
        attempts += 1
        if letter in word.lower():
            guessed_letters.add(letter.upper())
        
        # Checks if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word):
            return attempts

def main():
    # Checks if the file has been provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 ahorcado.py words.txt")
        sys.exit(1)
    
    words_file = sys.argv[1]
    words = read_words(words_file)
    
    for word in words:
        attempts = guess_word(word)
        print(f"Word: {word} - Attempts needed: {attempts}")

if __name__ == "__main__":
    main()
