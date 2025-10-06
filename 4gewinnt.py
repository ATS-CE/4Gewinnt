import random
import time

print("4 Gewinnt")
print("Die Leisten sind von 0-6 durchnummeriert.\nWenn du dran bist gib eine Zahl an, dort wird dann dein O sein.")
print("Viel Glück\n"+20*"-")
time.sleep(3)
compPlayer = input("Willst du gegen einen Computer Spielen?\n> ").lower()

playeroptions = ["X", "O"]
player = random.choice(playeroptions)

ROWS = 6
COLS = 7

board = [[" "for _ in range(COLS)] for _ in range(ROWS)]

def printBoard():
    for row in board:
        print("|"+"|".join(row)+"|")
    print(" "+ " ".join(str(i) for i in range(COLS)))
  
def dropPiece(col, piece):
    for row in reversed(board):
        if row[col] ==" ":
            row[col] = piece
            return True
    return False

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

def boardFull():
    return all(board[0][c]!= " " for c in range (COLS))


while True:
    if compPlayer != "ja":
        printBoard()
        col = int(input(f"Spieler {player} wähle eine Spalte (0-{COLS-1})\n> "))
        
        if col < 0 or col >= COLS or not dropPiece(col, player):
            print("Ungültige Eingabe, erneut")
            continue
    
    elif player == "O":
        col = random.randint(0,6)
        if col < 0 or col >= COLS or not dropPiece(col, player):
            continue
    
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