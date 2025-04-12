from colorama import Fore

def show_menu():
    print(Fore.CYAN + "\n=== HEX GAME ===")
    print(Fore.YELLOW + "1. Jugar contra el bot")
    print(Fore.YELLOW + "2. Jugar contra otro humano")
    print(Fore.YELLOW + "3. Configurar tamaño del tablero")
    print(Fore.RED + "4. Salir")
    
    while True:
        choice = input(Fore.WHITE + "Selecciona una opción: ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        print(Fore.RED + "Opción inválida. Intenta de nuevo.")