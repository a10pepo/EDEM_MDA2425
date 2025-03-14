import random
import pg8000
from datetime import datetime
import functions
from termcolor import colored
import time

# def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)
        
def print_board(board):
    print(" ", "\n", "-" * 13)
    for row in board:
        print(" | ", end="")
        for cell in row:
            if cell == "X":
                colored_x = colored('X', 'green', attrs=['bold'])
                print(colored_x, end="")
            elif cell == "O":
                colored_o = colored('O', 'red', attrs=['bold'])
                print(colored_o, end="")
            else:
                print(cell, end="")
            print(" | ", end="")
        print(" ", "\n", "-" * 13)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_user_move(board):
    while True:
        try:
            move = int(input("\nEnter the number of the cell (1-9): "))
            if move in range(1, 10):
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] not in ["X", "O"]:
                    return row, col, move
                else:
                    print("\nCell already taken. Choose another cell.")
            else:
                print("\nInvalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 9.")

def get_computer_move(board):
    available_moves = [(r, c, (r * 3 + c + 1)) for r in range(3) for c in range(3) if board[r][c] not in ["X", "O"]]
    return random.choice(available_moves)

def insert_move_to_db(conn, move_text):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO games (
        timestamp,
        move
    )
    VALUES (%s, %s)
    """, (datetime.now(), move_text))
    conn.commit()

def setup_database(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id SERIAL PRIMARY KEY,
        move TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()

def main():
    # Connect to the PostgreSQL database
    conn = pg8000.connect(
        user="postgres",
        password="Welcome01",
        host="postgres",
        port=5432,
        database="tictactoe"
    )
    # Setup the database
    setup_database(conn)

    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"
    moves_made = 0
    
    functions.make_header('TIC TAC TOE', 'Moves are logged in the database')

    while True:
        print_board(board)
        if current_player == "X":
            row, col, move = get_user_move(board)
        else:
            time.sleep(1)
            row, col, move = get_computer_move(board)
            print(f"\nComputer chose cell {move}")

        board[row][col] = current_player
        moves_made += 1

        move_text = f"Player {current_player} moved to cell {move}"
        insert_move_to_db(conn, move_text)

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                colored_x_winner = colored('\nPlayer X wins!\n\n', 'green', attrs=['bold'])
                print(colored_x_winner, end="")
            else:
                colored_o_winner = colored('\nPlayer O wins!\n\n', 'red', attrs=['bold'])
                print(colored_o_winner, end="")
            insert_move_to_db(conn, f"\nPlayer {current_player} wins!")
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