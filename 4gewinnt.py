import random
import time

startingPlayer = random.randint(1,2)
print("4 Gewinnt")
print("Die Leisten sind von 0-6 durchnummeriert.\nWenn du dran bist gib eine Zahl an, dort wird dann dein O sein.")
print("Viel Glück\n"+20*"-")

ROWS = 6
COLS = 7

board = [[" "for _ in range(COLS)] for _ in range(ROWS)]

def printBoard():
    for row in board:
        print("|"+"|".join(row)+"|")
    print(" "+ " ".join(str(i) for i in range(COLS)))
  
def dropPiece(col, piece):
    for row in reversed(board):
        if row(col) ==" ":
            row(col) = piece
            return True
    return False

def checkWinner:
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    return False

def boardFull:
    return all(board[0][c]!= " " for c in range (COLS))

player = "X"
while True:
    




