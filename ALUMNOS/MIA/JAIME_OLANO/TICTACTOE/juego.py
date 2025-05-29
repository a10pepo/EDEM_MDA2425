import random
import pg8000
from datetime import datetime
import functions
from termcolor import colored
import time
import sys

class TicTacToe:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.current_player = "X"
        self.moves_made = 0
        self.conn = self.connect_to_db()
        self.setup_database()

    def connect_to_db(self):
        """Establece conexión con PostgreSQL"""
        try:
            return pg8000.connect(
                user="postgres",
                password="Welcome01",
                host="postgres",  # Cambiar a "localhost" si no usas Docker
                port=5432,
                database="tictactoe"
            )
        except Exception as e:
            print(f"\n⚠️  Error de conexión a la base de datos: {e}\n")
            return None

    def setup_database(self):
        """Crea la tabla si no existe"""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id SERIAL PRIMARY KEY,
                    move TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )""")
                self.conn.commit()
            except Exception as e:
                print(f"❌ Error al crear tabla: {e}")

    def print_board(self):
        """Muestra el tablero con colores"""
        print("\n" + "-" * 13)
        for row in self.board:
            print(" | ", end="")
            for cell in row:
                if cell == "X":
                    print(colored('X', 'green', attrs=['bold']), end="")
                elif cell == "O":
                    print(colored('O', 'red', attrs=['bold']), end="")
                else:
                    print(cell, end="")
                print(" | ", end="")
            print("\n" + "-" * 13)

    def check_winner(self, player):
        """Verifica si hay ganador"""
        # Filas y columnas
        for i in range(3):
            if all([cell == player for cell in self.board[i]]) or \
               all([self.board[row][i] == player for row in range(3)]):
                return True
        # Diagonales
        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def get_user_move(self):
        """Obtiene movimiento válido del jugador"""
        while True:
            try:
                move = int(input("\nTu turno (X). Elige celda (1-9): "))
                if 1 <= move <= 9:
                    row, col = (move - 1) // 3, (move - 1) % 3
                    if self.board[row][col] not in ["X", "O"]:
                        return row, col, move
                    print(colored("\n❌ Casilla ocupada. Elige otra.", 'yellow'))
                else:
                    print(colored("\n❌ Número inválido. Elige del 1 al 9.", 'yellow'))
            except ValueError:
                print(colored("\n❌ Entrada no válida. Introduce un número.", 'yellow'))

    def get_computer_move(self):
        """Movimiento aleatorio de la computadora"""
        available = [(r, c, (r*3+c+1)) 
                    for r in range(3) 
                    for c in range(3) 
                    if self.board[r][c] not in ["X", "O"]]
        return random.choice(available)

    def log_move(self, move_text):
        """Registra movimiento en la base de datos"""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO games (move, timestamp) VALUES (%s, %s)",
                    (move_text, datetime.now())
                )
                self.conn.commit()
            except Exception as e:
                print(f"⚠️  Error al guardar movimiento: {e}")

    def play(self):
        """Lógica principal del juego"""
        functions.make_header('TIC TAC TOE', 'Moves are logged in the database')
        
        while True:
            self.print_board()
            
            if self.current_player == "X":
                row, col, move = self.get_user_move()
            else:
                time.sleep(1)  # Pausa dramática
                row, col, move = self.get_computer_move()
                print(f"\nComputadora (O) elige celda {move}")

            self.board[row][col] = self.current_player
            self.moves_made += 1
            move_text = f"Jugador {self.current_player} -> Celda {move}"
            self.log_move(move_text)

            if self.check_winner(self.current_player):
                self.print_board()
                winner_msg = f"\n¡{self.current_player} GANA!\n"
                color = 'green' if self.current_player == "X" else 'red'
                print(colored(winner_msg, color, attrs=['bold']))
                self.log_move(f"GANADOR: {self.current_player}")
                break

            if self.moves_made == 9:
                self.print_board()
                print(colored("\n¡EMPATE!\n", 'blue', attrs=['bold']))
                self.log_move("RESULTADO: Empate")
                break

            self.current_player = "O" if self.current_player == "X" else "X"

        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

