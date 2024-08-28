from player import Player
from menu import Menu
from board import Board
from utils import clear_screen


class Game:
    def __init__(self):
        self.board = Board()
        self.menu = Menu()
        self.players = [Player(), Player()]
        self.current_player = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            clear_screen()
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()

    def setup_player(self):
        symbols = set()  # To keep track of used symbols
        for index, player in enumerate(self.players):
            print(f"For player {index + 1}, enter your details:")
            player.choose_name()

            while True:
                clear_screen()
                player.choose_symbol()
                if player.symbol in symbols:
                    print(f"Symbol '{player.symbol}' is already taken. Please choose a different symbol.")
                else:
                    symbols.add(player.symbol)
                    break
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            is_win, win_pattern = self.check_win()
            if is_win:
                self.switch_player()
                clear_screen()
                self.board.display_board(win_pattern)
                print(f"Congratulations {self.players[self.current_player].name.capitalize()}! You won!")
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            elif self.check_draw():
                clear_screen()
                self.board.display_board()
                print("It's a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        clear_screen()
        player = self.players[self.current_player]
        self.board.display_board()
        print(f"{player.name.capitalize()}'s turn ({player.symbol})")
        while True:
            try:
                choice = int(input("Choose a cell (1 to 9): "))
                if 0 < choice <= 9 and self.board.update_board(choice, player.symbol):
                    self.switch_player()
                    break
                else:
                    raise Exception
            except ValueError:
                clear_screen()
                print(f"Invalid cell! {player.name.capitalize()}, try again.")
                self.board.display_board()
                continue
            except Exception:
                clear_screen()
                if choice < 1 or choice > 9:
                    print(f"Invalid Cell! {player.name.capitalize()}, Try again.")
                    self.board.display_board()
                else:
                    print(f"Cell {choice} is taken already {player.name.capitalize()}, Choose another cell.")
                    self.board.display_board()
                continue

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_win(self):
        winning_combinations = [
            # Rows
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            # Columns
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            # Diagonals
            [0, 4, 8],
            [2, 4, 6]
        ]
        for combo in winning_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]] and
                    not self.board.board[combo[0]].isdigit()):  # Ensure that the cells are not digits
                return True, combo
        return False, None

    def check_draw(self) -> bool:
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        clear_screen()
        self.board.reset_board()
        self.current_player = 0
        self.play_game()

    def quit_game(self):
        clear_screen()
        print("Thank you for playing")
