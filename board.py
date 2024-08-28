class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self, win_pattern=None):
        for i in range(0, 9, 3):
            if i != 0 and i % 3 == 0:
                print("-" * 5)
            row = self.board[i:i + 3]
            if win_pattern:
                row = [self.board[index] if index in win_pattern else ' ' for index in range(i, i + 3)]
            print("|".join(row))

    def update_board(self, index, symbol) -> bool:
        if self._is_valid_move(index):
            self.board[index - 1] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

    def _is_valid_move(self, index):
        return self.board[index - 1].isdigit()
