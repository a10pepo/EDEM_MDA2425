import random
import pg8000.native
import datetime

def print_board(board): #función para imprimir la pizarra
    for row in board: #para cada argumento en la lista row haz:
        print(" | ".join(row))  #imprime | despues del argumento
        print("-" * 5)  #Imprime - 5 veces

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:   #por cada columna en la lista board haz:
        if all([cell == player for cell in row]):   #si todos las celdas de la columna son iguales a lo que ha introducido el jugador, para comprobar si has ganado
            return True 
    for col in range(3):    
        if all([board[row][col] == player for row in range(3)]):    #comprueba si las filas son iguales al último movimiento del jugador 
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):    #si todas las celdas de la diagonal de der a izq de la pizarra o todas las celdas de la diagonal de der a izq son iguales a player
        return True
    return False

def get_user_move(board):
    while True: 
        try:
            move = int(input("Enter the number of the cell (1-9): "))   #Entra un número del 1 al 9 y se almacena en move, este será el número de la celda
            if move in range(1, 10):    #si move esta en el rango de 10 a 1
                row, col = (move - 1) // 3, (move - 1) % 3  #para saber la celda que quiere dentro de la pizarra
                if board[row][col] not in ["X", "O"]:   #se comprueba que la celda no está cogida
                    return row, col, move   
                else:
                    print("Cell already taken. Choose another cell.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def get_computer_move(board):
    available_moves = [(r, c, (r * 3 + c + 1)) for r in range(3) for c in range(3) if board[r][c] not in ["X", "O"]]    #primero el ordenador comprueba las celdas disponibles
    return random.choice(available_moves)   #elegir una celda aleatoria 

def insert_move_to_db(conn, move_text):
    try:
        tiempo_real=datetime.datetime.now()
        conn.run("INSERT INTO games (timestamp, move) VALUES (:tiempo, :move)", tiempo=tiempo_real, move=move_text)
        
        
    except Exception as e:
        print(f"Error: La base de datos no está lista, si estás en Fase 1 no es un problema {e}")

def setup_database(conn):
    conn.run("""
    CREATE TABLE IF NOT EXISTS games (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP WITH TIME ZONE,
        move TEXT
    );
    """)
    

def main():
    try:
        # Connect to the PostgreSQL database
        conn = pg8000.native.Connection("postgres", password="pass01", host="postgres_container")

        # Setup the database
        setup_database(conn)
    except pg8000.exceptions.InterfaceError:
        print("Error: La base de datos no está lista, si estás en Fase 1 no es un problema")
        conn = None
        

    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"
    moves_made = 0

    while True: #estaba false
        print_board(board)  #acciona la función de imprimir la pizarra
        if current_player == "X":   #Current_player = X cuando juega el usuario
            row, col, move = get_user_move(board)   #activa la función del movimiento, extrae la celda que quiere jugar el usuario
        else:
            row, col, move = get_computer_move(board)   #Current player = O si juega el ordenador
            print(f"Computer chose cell {move}")

        board[row][col] = current_player    #actualiza la pizarra
        moves_made += 1 #+1 movimientos realizzados

        move_text = f"Player {current_player} moved to cell {move}" 
        insert_move_to_db(conn, move_text)  #inserta movimiento realizado en bas de datos

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

        current_player = "O" if current_player == "X" else "X" #cambia el jugador para el siguiente turno
    if conn:
        conn.close()

if __name__ == "__main__":
    main()