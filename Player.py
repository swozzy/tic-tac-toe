# 'Player' class
class Player():

    # Initialization. Holds their name, data if they go first, and what symbol they chose
    def __init__(self, name = "temp", turn = "temp", symbol = "temp"):

        self.name = name
        self.turn = turn
        self.symbol = symbol

    # Return name
    def get_name(self):
        return self.name

    # Return turn
    def get_turn(self):
        return self.turn

    # Return symbol
    def get_symbol(self):
        return self.symbol

    # Sets name
    def set_name(self, new_name):
        self.name = new_name

    # Sets turn
    def set_turn(self, new_turn):
        self.turn = new_turn

    # Sets symbol
    def set_symbol(self, new_symb):
        self.symbol = new_symb
