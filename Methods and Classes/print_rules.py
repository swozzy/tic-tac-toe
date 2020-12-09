import time
from ask_yes_no import ask_yes_no

####################
# HELPER FUNCTIONS #
####################

# Prints empty game board
def print_emptygame():
    print("1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9")

# Prints tied game board
def print_tiedgame():
    print("O | O | X\n---------\nX | X | O\n---------\nO | O | X")

# Prints a won game
def print_wongame():
    print("1 | O | O\n---------\nX | X | X\n---------\n7 | 8 | 9")

# Prints a board that's mid-game
def print_midgame():
    print("O | 2 | O\n---------\nO | X | 6\n---------\nX | 8 | O")

#################
# MAIN FUNCTION #
#################

# Is the "introduction" to our game and prints out rules.
def print_rules():

# Asks user if they would like to skip the introduction

    flag = ask_yes_no("Would you like to hear the rules of the game? (Y/N): ")

    if (flag):

        print("Tic-Tac-Toe is a game in which two players take turns marking spaces in a 3x3 grid with Xs and Os.")
        print("\nBelow is an example of a board MID-GAME:\n")

        print_midgame()

        time.sleep(1.5)

        print("\nThe player who succeeds in placing three of their symbols in a horizontal, vertical, or diagonal row is the winner.")
        print("\nBelow is an example of a WON game:\n")

        print_wongame()

        time.sleep(2.5)

        print("\nA tie is formed when the board is filled and there are no horizontal, diagonal, or vertical rows whose symbols all match.")
        print("\nBelow is an example of a TIED game:\n")

        print_tiedgame()

        time.sleep(2.5)

        print("\nPlayers will take turns entering the number of the spot in which they would like to place their symbol.")
        print("An empty grid for reference is printed below:\n")

        print_emptygame()

        print("\nEach index corresponds to a space the user can select to place their symbol.")
        print("An occupied spot cannot be chosen again nor can it be replaced with another symbol.")

# Added functionality to skip intro
