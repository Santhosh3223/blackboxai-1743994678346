import copy
from game_logic import Board

class ChessAI:
    def __init__(self, depth=3):
        self.depth = depth  # Search depth for minimax

    def get_best_move(self, board):
        """Returns the best move for the current player using minimax with alpha-beta pruning"""
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')

        # Get all possible moves for current player
        moves = self.get_all_possible_moves(board)

        for move in moves:
            # Make a copy of the board to simulate the move
            new_board = copy.deepcopy(board)
            new_board.make_move(move[0], move[1])

            # Evaluate the move
            move_value = self.minimax(new_board, self.depth-1, alpha, beta, False)

            if move_value > best_value:
                best_value = move_value
                best_move = move

            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cutoff

        return best_move

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.game_over:
            return board.evaluate_board()

        if maximizing_player:
            max_eval = -float('inf')
            moves = self.get_all_possible_moves(board)
            for move in moves:
                new_board = copy.deepcopy(board)
                new_board.make_move(move[0], move[1])
                eval = self.minimax(new_board, depth-1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            moves = self.get_all_possible_moves(board)
            for move in moves:
                new_board = copy.deepcopy(board)
                new_board.make_move(move[0], move[1])
                eval = self.minimax(new_board, depth-1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_all_possible_moves(self, board):
        """Returns all possible moves for current player"""
        moves = []
        for x in range(7):
            for y in range(7):
                piece = board.grid[x][y]
                if piece and piece.color == board.current_player:
                    for (nx, ny) in piece.get_valid_moves(board.grid):
                        moves.append(((x, y), (nx, ny)))
        return moves