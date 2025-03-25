from game_logic.hex_game import HexGame
from interface.cli_interface import display_board
from bot.simple_bot import RandomBot
from colorama import Fore

def main():
    board_size = 5  # Para pruebas, luego puedes cambiarlo a 11
    game = HexGame(board_size)
    bot = RandomBot(game.board)

    while True:
        display_board(game.board)
        
        # Turno del jugador
        if game.current_player == 1:
            print(Fore.BLUE + "\nTu turno (Jugador Azul)")
            try:
                move = input("Ingresa tu movimiento (ej. 'a1'): ")
                col = ord(move[0].lower()) - ord('a')
                row = int(move[1:]) - 1
                if not game.make_move(row, col):
                    print(Fore.RED + "¡Movimiento inválido!")
                    continue
            except (ValueError, IndexError):
                print(Fore.RED + "Formato incorrecto. Usa letra + número (ej. 'a1').")
                continue
        
        # Turno del bot
        else:
            print(Fore.RED + "\nTurno del Bot (Rojo)")
            row, col = bot.make_move()
            game.make_move(row, col)
            print(f"Bot juega: {chr(97 + col)}{row + 1}")

        # Verificar ganador
        winner = game.check_winner()
        if winner == 1:
            display_board(game.board)
            print(Fore.BLUE + "¡Ganaste!")
            break
        elif winner == 2:
            display_board(game.board)
            print(Fore.RED + "¡El bot ganó!")
            break

if __name__ == "__main__":
    main()