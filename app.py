from flask import Flask, render_template, request, jsonify
import random
import copy
from vier_gewinnt import dropPiece, checkWinner, get_immediate_win_or_block, minimax, boardFull

app = Flask(__name__)

ROWS = 6
COLS = 7
board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
current_player = "X"

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player)

@app.route('/move', methods=['POST'])
def make_move():
    global current_player
    col = request.json['column']
    depth = int(request.json.get('depth', 3)) # Default depth is 3
    if dropPiece(board, col, current_player):
        if checkWinner(current_player, board):
            return jsonify({'status': 'win', 'player': current_player, 'board': board})
        if boardFull(board):
            return jsonify({'status': 'draw', 'board': board})

        current_player = "O"

        col = get_immediate_win_or_block(board, "O")
        if col is None:
            col, _ = minimax(board, depth, True, "O", -float('inf'), float('inf'))

        if col is not None:
            dropPiece(board, col, "O")
            if checkWinner("O", board):
                return jsonify({'status': 'win', 'player': 'O', 'board': board})
            if boardFull(board):
                return jsonify({'status': 'draw', 'board': board})

        current_player = "X"

    return jsonify({'status': 'continue', 'board': board})

@app.route('/reset', methods=['POST'])
def reset_game():
    global board, current_player
    board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    current_player = "X"
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)