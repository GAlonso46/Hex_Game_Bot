from colorama import Fore, Back, Style, init
init(autoreset=True)  # Inicializa colorama

def display_board(board):
    """Muestra el tablero con colores y coordenadas."""
    size = len(board)
    # Encabezado de columnas (letras)
    print("   " + " ".join([Fore.RED + f"{chr(97 + i)}" for i in range(size)]))

    for i in range(size):
        # Número de fila (derecha e izquierda)
        row_num = Fore.BLUE + f"{i + 1:2d}"
        print(row_num + " ", end="")
        
        # Espacios para el efecto hexagonal
        print(" " * i, end="")
        
        for j in range(size):
            cell = board[i][j]
            if cell == 1:  # Jugador (azul)
                print(Fore.BLUE + "● ", end="")
            elif cell == 2:  # Bot (rojo)
                print(Fore.RED + "● ", end="")
            else:  # Vacío (gris)
                print(Fore.WHITE + "○ ", end="")
        print(row_num)  # Número de fila al final

    # Pie de columnas (letras)
    print("   " + " " * size + " ".join([Fore.RED + f"{chr(97 + i)}" for i in range(size)]))