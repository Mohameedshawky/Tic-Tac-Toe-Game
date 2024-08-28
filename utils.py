def clear_screen():
    print("\n" * 25)


def validate_choice_menu(option):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2]:
                raise ValueError
        except ValueError:
            if option == "main_menu":
                print("Choose from these choices only\n1. Start Game\n2. Quit Game")
            else:  # option == "endgame_menu"
                print("Choose from these choices only\n1. Restart Game\n2. Quit Game")
            continue
        else:
            return choice
