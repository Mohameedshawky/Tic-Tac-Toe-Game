class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only):")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name! Please enter your name (letters only):")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, Choose your symbol (a single letter):")
            if len(symbol) == 1 and symbol.isalpha():
                self.symbol = symbol.upper()
                break
            print("Invalid symbol! Enter a single letter only:")