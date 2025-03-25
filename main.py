from game_logic.hex_game import HexGame
from interface.cli_interface import display_board

def main():
    print("¡Bienvenido al juego Hex!")
    game = HexGame(board_size=11)
    display_board(game.board)

if __name__ == "__main__":
    main()