# Tic-Tac-Toe Game

## Overview
This is a simple command-line Tic-Tac-Toe game implemented in Python. The game allows two players to play against each other by taking turns to place their symbols (X or O) on a 3x3 grid. The first player to align three of their symbols horizontally, vertically, or diagonally wins the game.

## Features
- Two-player mode
- Input validation for player names and symbols
- Clear screen functionality for better user experience
- Detection of win and draw conditions
- Option to restart or quit the game after it ends

## Requirements
- Python 3.11.9
- 

## Usage
1. Run the game:
    ```sh
    python main.py
    ```
2. Follow the on-screen instructions to enter player names and symbols.
3. Players take turns to choose a cell (1 to 9) to place their symbol.
4. The game will announce the winner or if it's a draw.
5. Choose to restart or quit the game after it ends.

## Code Structure
- `main.py`: The entry point of the application.
- `player.py`: Contains the `Player` class.
- `menu.py`: Contains the `Menu` class.
- `board.py`: Contains the `Board` class.
- `game.py`: Contains the `Game` class and game logic.
- `utils.py`: Contains utility functions like `clear_screen`,`validate_choice_menu`.

## Classes
- **Player**: Handles player details and input validation.
- **Menu**: Manages the display and validation of menu choices.
- **Board**: Manages the game board and its display.
- **Game**: Handles the game logic, including turns, win/draw detection, and game flow.

## Class Diagram
![classDigram](https://github.com/user-attachments/assets/d1ed8526-9bc7-479b-a45d-df9034fb4ab6)
