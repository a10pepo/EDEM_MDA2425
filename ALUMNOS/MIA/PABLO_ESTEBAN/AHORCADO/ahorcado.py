class Ahorcado:

    def __init__(self, palabra):
        self.word = palabra.upper()
        self.board = ["_" for _ in range(len(palabra))]
        self.tried_letters = []
        self.tries = 0

    def __str__(self) -> str:
        return f"""
        {' '.join(self.board)}

        Tries: {self.tries}
        {self.tried_letters}
        """
    
    def try_letter(self, letter: str):
        letter = letter.upper()
        
        if len (letter) > 1:
            raise ValueError("Introduce una sola letra")
        
        self.tries += 1
        
        if letter in self.word and letter not in self.tried_letters:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.board[i] = letter
            self.tried_letters.append(letter)
            return True
        
        else:
            self.tried_letters.append(letter)
            return False

    def won(self):
        if "_" not in self.board:
            return True
        else:
            return False


if __name__ == "__main__":
    ahoracado = Ahorcado("murcielago")
    print(ahoracado)
    ahoracado.try_letter("a")
    print(ahoracado)
    print(ahoracado.won())