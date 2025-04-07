
Built by https://www.blackbox.ai

---

```markdown
# Chess Game

## Project Overview
This project is an implementation of a chess game that allows two players to play against each other or against an AI. The game is structured to follow the standard rules of chess, with pieces having their respective movements and capture capabilities defined. The project utilizes Python along with Flask to create a web-based interface for users to interact with the game.

## Installation
To set up the project locally, please follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chess-game.git
   cd chess-game
   ```

2. Install dependencies:
   Make sure you have Python and pip installed. Then, run:
   ```bash
   pip install flask
   ```

3. Start the application:
   ```bash
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000/` to access the chess game.

## Usage
After starting the application, you can interact with the chess game through the web interface:

- Click on pieces to see possible moves.
- Click on a valid move location to move the piece.
- If playing against the AI, simply let the AI take its turn after yours.

## Features
- Web-based chess interface.
- Play against another player or AI.
- Valid moves and captures implemented for chess pieces.
- Session management to maintain game state across requests.
- Simple AI using minimax algorithm with alpha-beta pruning.

## Dependencies
The project requires the following Python packages:

- Flask: A micro web framework for Python.

## Project Structure
The project consists of several key files and directories:

```
/chess-game
│
├── app.py             # Flask application for handling game logic and routes
├── ai.py              # Contains the ChessAI class for AI movement
├── game_logic.py      # Contains the Board class and game logic methods
└── models.py          # Contains class definitions for the chess pieces
```

### File Descriptions
- **app.py**: This file initializes the Flask application and handles routes for rendering pages and managing game state via API requests.
- **ai.py**: Implements the `ChessAI` class, which determines the best moves for the AI player using the minimax algorithm.
- **game_logic.py**: Manages the board state, movement validation, and game rules.
- **models.py**: Defines the `Piece` class and its subclasses (e.g., `Pawn`, `Knight`) that govern the behavior and movement of the chess pieces.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

Happy playing!
```