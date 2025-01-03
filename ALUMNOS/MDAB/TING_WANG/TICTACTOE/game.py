import random
import pg8000
from datetime import datetime

# Crea una board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# imprimir board "vacío"
# board = [["1","2","3"], ["4", "5", "6"], ["7", "8","9"]]
# print_board(board)

# Verifica si el jugador ha ganado
def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]): # si todas las celdas de una fila son iguales
            return True
    for col in range(3): # columna 0, 1, 2
        if all([board[row][col] == player for row in range(3)]): # si todas las celdas de cada columna son iguales
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]): # diagonales
        # board[i][i] = [fila][columna] = diagonal // bucle = recorre todas las combinaciones
        return True
    return False

# movimientos del jugador 
def get_user_move(board):
    while True:
        try:
            move = int(input("Enter the number of the cell (1-9): "))
            if move in range(1, 10):
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] not in ["X", "O"]: # verifica que la celda está vacía
                    return row, col, move
                else:
                    print("Cell already taken. Choose another cell.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# get_user_move(board)

# "rival" automático (computer)
def get_computer_move(board):
    available_moves = [(r, c, (r * 3 + c + 1)) for r in range(3) for c in range(3) if board[r][c] not in ["X", "O"]]
    # movimiento aleatorio
    return random.choice(available_moves)

# BBDD
def setup_database(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        move TEXT
    )
    """)
    conn.commit()

def insert_move_to_db(conn, move_text):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO games (timestamp, move) VALUES (%s)", (datetime.now(), move_text))
        conn.commit()
    except Exception as e:
        print("Error: La base de datos no está lista, si estás en Fase 1 no es un problema")


def main():
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = pg8000.connect(user="postgres", password="pass01", host="postgres", port=5432, database="tictactoe")
        print("Conexión exitosa")
        # Setup the database
        setup_database(conn)
    except pg8000.exceptions.InterfaceError as e:
        print(f"Error al conectar a la base de datos: {e}")
        conn = None
        
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"
    moves_made = 0

    while True:
        print_board(board)
        if current_player == "X":
            row, col, move = get_user_move(board)
        else:
            row, col, move = get_computer_move(board)
            print(f"Computer chose cell {move}")

        board[row][col] = current_player
        moves_made += 1

        move_text = f"Player {current_player} moved to cell {move}"
        insert_move_to_db(conn, move_text)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            insert_move_to_db(conn, f"Player {current_player} wins!")
            break

        if moves_made == 9:
            print_board(board)
            print("It's a draw!")
            insert_move_to_db(conn, "It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
    if conn:
        conn.close()

if __name__ == "__main__":
    main()
