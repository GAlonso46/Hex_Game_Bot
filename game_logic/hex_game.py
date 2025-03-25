class HexGame:
    def __init__(self, board_size=11):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 1  # 1: Jugador (azul), 2: Bot (rojo)

    def make_move(self, row, col):
        """Realiza un movimiento en el tablero."""
        if self.board[row][col] != 0:
            return False  # Casilla ocupada
        self.board[row][col] = self.current_player
        self.current_player = 3 - self.current_player  # Alterna entre 1 y 2
        return True

    def check_winner(self):
        """Verifica si hay un ganador usando BFS."""
        for player in [1, 2]:
            visited = set()
            queue = []
            # Configuración inicial según el jugador
            if player == 1:
                cells = [(i, 0) for i in range(self.board_size) if self.board[i][0] == player]
            else:
                cells = [(0, j) for j in range(self.board_size) if self.board[0][j] == player]

            for cell in cells:
                queue.append(cell)
                visited.add(cell)

            while queue:
                i, j = queue.pop(0)
                # Condición de victoria: llegar al lado opuesto
                if (player == 1 and j == self.board_size - 1) or (player == 2 and i == self.board_size - 1):
                    return player

                # Explorar vecinos (6 direcciones en Hex)
                for di, dj in [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.board_size and 0 <= nj < self.board_size:
                        if self.board[ni][nj] == player and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            queue.append((ni, nj))
        return 0  # No hay ganador aún