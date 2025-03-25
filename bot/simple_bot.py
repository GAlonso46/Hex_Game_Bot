import random

class RandomBot:
    def __init__(self, board):
        self.board = board

    def make_move(self):
        empty_cells = [
            (i, j) 
            for i in range(len(self.board)) 
            for j in range(len(self.board[i])) 
            if self.board[i][j] == 0
        ]
        return random.choice(empty_cells)