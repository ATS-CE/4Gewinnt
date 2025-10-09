# 4 Gewinnt Docker App

## Overview
This project is a dockerized version of the classic game "4 Gewinnt" (Connect Four). It allows users to play the game against a computer opponent through a web-based console.

## Project Structure
```
4gewinnt
├── app.py                # Web server for the game interface
├── vier_gewinnt.py       # Main game logic
├── templates
│   └── index.html        # HTML template for the game
├── requirements.txt      # Python dependencies
├── Dockerfile            # Instructions to build the Docker image
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd 4gewinnt
   ```

2. **Build the Docker Image**
   ```bash
   docker build -t 4gewinnt-app .
   ```

3. **Run the Docker Container**
   ```bash
   docker run -p 5000:5000 4gewinnt-app
   ```

4. **Access the Game**
   Open your web browser and navigate to `http://localhost:5000` to start playing the game.

## How to Play
- The game is played against an AI opponent.
- You can change the AI strength (depth from 1 to 10) before each move.
- Click on a column to make your move.
- The game will indicate when a player has won or if the board is full.

## Dependencies
This project requires the following Python packages:
- Flask: A web framework for Python to create the web interface.
- NumPy: For efficient array operations for the game board.
- Gunicorn: A production-ready web server (for Unix-like systems).
- Waitress: A production-ready web server (for Windows).

Make sure to install the dependencies listed in `requirements.txt` if running outside of Docker.