from models import *

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(7)] for _ in range(7)]
        self.current_player = 'white'
        self.game_over = False
        self.winner = None
        self.setup_board()

    def setup_board(self):
        # Setup pawns
        for x in range(7):
            self.grid[x][1] = Pawn('white', 'pawn', (x, 1))
            self.grid[x][5] = Pawn('black', 'pawn', (x, 5))

        # Setup back rows
        pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight']
        for x, piece in enumerate(pieces):
            self.grid[x][0] = eval(piece.capitalize())('white', piece, (x, 0))
            self.grid[x][6] = eval(piece.capitalize())('black', piece, (x, 6))

    def is_valid_move(self, start, end):
        piece = self.grid[start[0]][start[1]]
        if not piece or piece.color != self.current_player:
            return False
            
        return end in piece.get_valid_moves(self.grid)

    def make_move(self, start, end):
        if not self.is_valid_move(start, end):
            return False
            
        # Move the piece
        piece = self.grid[start[0]][start[1]]
        self.grid[end[0]][end[1]] = piece
        self.grid[start[0]][start[1]] = None
        piece.position = end
        piece.has_moved = True
        
        # Switch player
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        return True

    def evaluate_board(self):
        """Simple evaluation function for AI"""
        score = 0
        piece_values = {
            'pawn': 1, 'knight': 3, 'bishop': 3,
            'rook': 5, 'queen': 9, 'king': 100
        }
        
        for row in self.grid:
            for piece in row:
                if piece:
                    value = piece_values[piece.type]
                    score += value if piece.color == 'white' else -value
                    
        return score