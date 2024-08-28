from utils import validate_choice_menu


class Menu:
    def display_main_menu(self) -> int:
        print("Welcome to my X-O game!\n1. Start Game\n2. Quit Game\nEnter your choice (1 or 2):")
        return validate_choice_menu("main_menu")

    def display_endgame_menu(self) -> int:
        print("1. Restart Game\n2. Quit Game\nEnter your choice (1 or 2):")
        return validate_choice_menu("endgame_menu")
