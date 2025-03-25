class HexGame:
    def __init__(self, board_size=11):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]  # 0: vacío, 1: jugador, 2: bot