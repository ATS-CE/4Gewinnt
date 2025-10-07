import random
import time
import copy

print("4 Gewinnt")
print("Die Leisten sind von 0-6 durchnummeriert.\nWenn du dran bist gib eine Zahl an, dort wird dann dein O sein.")
print("Viel Glück\n"+20*"-")
time.sleep(3)
compPlayer = input("Willst du gegen einen Computer Spielen?\n> ").lower()
print(20*"-")

difficulty = 0
if compPlayer == "ja":
    while difficulty == 0:
        difficulty = int(input("nenne die Schwierigkeit von 1-7\nJe höher die Schwierigkeit desto länger braucht aber auch der Computer\n> "))
        if difficulty <= 0 or difficulty >= 8:
            print("Ungültige Eingabe")
        else:
            print(20*"-")

playeroptions = ["X", "O"]
player = random.choice(playeroptions)

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
def checkWinner(piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
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
    score += center_column.count(piece) * 1.5

    def count_windows(line):
        nonlocal score
        for i in range(len(line) - 3):
            window = line[i:i+4]
        if window.count(piece) == 4:
            score += 1000
        elif window.count(piece) == 3 and window.count(" ") == 1:
            score += 50
        elif window.count(piece) == 2 and window.count(" ") == 2:
            score += 5

        if window.count(opponent) == 4:
            score -= 2000
        elif window.count(opponent) == 3 and window.count(" ") == 1:
            score -= 200
        elif window.count(opponent) == 2 and window.count(" ") == 2:
            score -= 10

    for r in range(ROWS):
        count_windows(board[r])

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


# Computer logic 
def minimax(board, depth, maximizing, piece, alpha, beta):
    valid_moves = get_valid_moves(board)
    is_terminal = checkWinner("X") or checkWinner("O") or boardFull()

    if depth == 0 or is_terminal:
        if is_terminal:
            if checkWinner(piece):
                return (None, 1000000)
            elif checkWinner("O" if piece == "X" else "X"):
                return (None, -1000000)
            else:  # Unentschieden
                return (None, 0)
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
        col, _ = minimax(board, 5, True, "O", -float('inf'), float('inf'))
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
        
    if checkWinner(player):
        printBoard()
        print(f"Spieler {player} hat gewonnen!")
        break
    player = "O" if player == "X" else "X"