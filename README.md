# Tic-Tac-Toe Game

A simple command-line Tic-Tac-Toe game built using Python, where two players can play against each other.

## How the Game Works

- The game board is a 3x3 grid, represented as a list of 9 elements.
- Players take turns to place their mark (X or O) on the board.
- Player X always goes first.
- The game checks for a win after each move.
- If all spots on the board are filled and no player has won, the game results in a draw.

## Features

1. **Player Interaction**: 
   - Each player selects a position on the board by entering a number (1-9).
   - The board updates after each move and is displayed to the players.

2. **Win Condition**: 
   - The game checks for any winning combinations (rows, columns, or diagonals) after each move. 
   - If a player completes any of these combinations, they are declared the winner.

3. **Draw Condition**: 
   - If the board is completely filled without any winning combination, the game ends in a draw.

## How I Made This

1. **Board Representation**:
   - The board is stored as a list of 9 elements, initially filled with spaces (' '). Players can place their mark (X or O) by selecting the corresponding position.

2. **Game Logic**:
   - A set of functions handle the core logic:
     - `print_board`: Displays the current state of the game board.
     - `check_win`: Checks for any winning combinations based on the current player’s mark.
     - `check_draw`: Determines if the board is full and there’s no winner, resulting in a draw.
   
3. **Player Input and Validation**:
   - Players enter their desired move (1-9). The game ensures the input is valid (number between 1-9, and the position is not already taken).
   
4. **Game Loop**:
   - The game continuously prompts players for moves, checks for win/draw conditions after each move, and switches players until the game is over.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `tic_tac_toe.py` file.
3. Open a terminal and navigate to the directory containing the file.
4. Run the game with the following command:
   ```bash
   python tic_tac_toe.py
