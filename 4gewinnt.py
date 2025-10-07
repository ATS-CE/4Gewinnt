import random
import time
import copy

print("4 Gewinnt")
print("Die Leisten sind von 0-6 durchnummeriert.\nWenn du dran bist gib eine Zahl an, dort wird dann dein O sein.")
print("Viel Glück\n"+20*"-")
time.sleep(3)
compPlayer = input("Willst du gegen einen Computer Spielen?\n> ").lower()
print(20*"-")

playeroptions = ["X", "O"]
player = random.choice(playeroptions)

difficulty = 0
if compPlayer == "ja":
    while difficulty == 0:
        difficulty = int(input("nenne die Schwierigkeit von 1-5\nJe höher die Schwierigkeit desto länger braucht aber auch der Computer\n> "))
<<<<<<< HEAD
        if difficulty <= 0 or difficulty >= 8:
=======
        if difficulty <= 0 or difficulty >= 6:
>>>>>>> cfeb695 (Reworked immediate decisionmaking when threat shows up)
            print("Ungültige Eingabe")
        else:
            print(20*"-")

ROWS = 6
COLS = 7

board = [[" "for _ in range(COLS)] for _ in range(ROWS)]

# Printing the board
def printBoard():
    for row in board:
        print("|"+"|".join(row)+"|")
    print(" "+ " ".join(str(i) for i in range(COLS)))

# Putting a piece into place
def dropPiece(col, piece):
    for row in reversed(board):
        if row[col] ==" ":
            row[col] = piece
            return True
    return False

# Copying board for Computer
def simulate_move(board, col, piece):
    new_board = copy.deepcopy(board)
    for row in reversed(new_board):
        if row[col] == " ":
            row[col] = piece
            break
    return new_board

# Checking who won
def checkWinner(piece, board_to_check):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board_to_check[r][c+i] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board_to_check[r+i][c] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board_to_check[r+i][c+i] == piece for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board_to_check[r-i][c+i] == piece for i in range(4)):
                return True    
    return False

# checking if board is full then game concluded
def boardFull():
    return all(board[0][c]!= " " for c in range (COLS))

# Valid moves for Computer
def get_valid_moves(board):
    return [c for c in range(COLS) if board[0][c] == " "]

# Prefers the center column if no threat is close and if threat is there blocks
def evaluate_board(board, piece):
    opponent = "O" if piece == "X" else "X"
    score = 0

    center_column = [board[r][COLS // 2] for r in range(ROWS)]
    score += center_column.count(piece)
    
    def count_windows(line):
        nonlocal score
        for i in range(len(line)-3):
            window = line[i:i+4]
        if window.count(piece) == 4 and window.count(" ") == 0:
            score += 100
        elif window.count(piece) == 3 and window.count(" ") == 1:
            score += 50
        elif window.count(piece) == 2 and window.count(" ") == 2:
            score += 5
        if window.count(opponent) == 4 and window.count(" ") == 0:
            score -= 10000
        elif window.count(opponent) == 3 and window.count(" ") == 1:
            score -= 100
        elif window.count(opponent) == 2 and window.count(" ") == 2:
            score -= 40

    for r in range(ROWS):
        row = [board[r][c] for c in range(COLS)]
        count_windows(row)
    for c in range(COLS):
        col = [board[r][c] for r in range(ROWS)]
        count_windows(col)

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            diag1 = [board[r+i][c+i] for i in range(4)]
            diag2 = [board[r+3-i][c+i] for i in range(4)]
            count_windows(diag1)
            count_windows(diag2)

    return score

# looking for an immediate threat or win
def get_immediate_win_or_block(board, piece):
    valid_moves = get_valid_moves(board)
    opponent = "O" if piece == "X" else "X"
<<<<<<< HEAD
    
# Winning move
    for col in valid_moves:
        temp_board = simulate_move(board, col, piece)
        if checkWinner(piece):
            return col
# Blocking move
    for col in valid_moves:
        temp_board = simulate_move(board, col, opponent)
        if checkWinner(opponent):
            return col
    
    return None
=======
    for col in valid_moves:
        temp_board = simulate_move(board, col, piece)
        if checkWinner(piece, temp_board):
            return col
    for col in valid_moves:
        temp_board = simulate_move(board, col, opponent)
        if checkWinner(opponent, temp_board):
            return col
>>>>>>> cfeb695 (Reworked immediate decisionmaking when threat shows up)


# Computer logic 
def minimax(board, depth, maximizing, piece, alpha, beta):
    valid_moves = get_valid_moves(board)
    valid_moves = sorted(valid_moves, key=lambda c: abs(COLS//2 - c))
    is_terminal = checkWinner("X", board) or checkWinner("O", board) or boardFull()

    if depth == 0 or is_terminal:
        if is_terminal:
            if checkWinner(piece, board):
                return (None, 1000000)
            elif checkWinner("O" if piece == "X" else "X", board):
                return (None, -2000000)
            else:
                return (None, -1)
        else:
            return (None, evaluate_board(board, piece))

    if maximizing:
        value = -float('inf')
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            new_board = simulate_move(board, col, piece)
            _, new_score = minimax(new_board, depth - 1, False, piece, alpha, beta)
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = float('inf')
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            new_board = simulate_move(board, col, "O" if piece == "X" else "X")
            _, new_score = minimax(new_board, depth - 1, True, piece, alpha, beta)
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value


# Gameloop
while True:
    if compPlayer != "ja":
        printBoard()
        col = int(input(f"Spieler {player} wähle eine Spalte (0-{COLS-1})\n> "))
        if col < 0 or col >= COLS or not dropPiece(col, player):
            print("Ungültige Eingabe, erneut")
            continue
    
    elif player == "O":
        print("Computer denkt nach...")
        col = get_immediate_win_or_block(board, "O")
        if col is None:
            col, _ = minimax(board, difficulty, True, "O", -float('inf'), float('inf'))
        if col is not None:
            dropPiece(col, "O")
        else:
            print("Kein gültiger Zug gefunden!")
            break
    
    elif player == "X":
        printBoard()
        col = int(input(f"Spieler {player} wähle eine Spalte (0-{COLS-1})\n> "))
        if col < 0 or col >= COLS or not dropPiece(col, player):
            print("Ungültige Eingabe, erneut")
            continue
        
    if checkWinner(player, board):
        printBoard()
        print(f"Spieler {player} hat gewonnen!")
        break
    player = "O" if player == "X" else "X"