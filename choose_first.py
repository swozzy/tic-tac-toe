# Imports
from Player import Player
from random import randint

# Sets either Player 1 or Player 2 be first
# The player not chosen first goes second
def choose_first(p1, p2):

    rand = randint(0, 1)

    if rand:
        p1.set_turn("first")
        p2.set_turn("second")
    else:
        p1.set_turn("second")
        p2.set_turn("first")

    print()

    # Prints who goes first for user clarification
    if p1.get_turn() == "first":
        print("** " + p1.get_name() + " will go first and " + p2.get_name() + " will go second **")
    if p2.get_turn() == "first":
        print("** " + p2.get_name() + " will go first and " + p1.get_name() + " will go second **")
