# IMPORTS
from print_rules import print_the_rules
from create_players import create_players
from Player import Player
from choose_first import choose_first
from choose_symbols import choose_symbols
from play_tic_tac_toe import play_tic_tac_toe
from play_again import play_again

def initialization():

    # PRINT RULES / INTRODUCTION
    print_the_rules()

    # CREATES AND RETURNS TWO PLAYER OBJECTS
    p1, p2 = create_players()

    # DECIDES WHO GOES FIRST
    choose_first(p1, p2)

    # DECIDE SYMBOLS
    choose_symbols(p1, p2)

    # BOTH PLAYERS COMPLETELY INITIALIZED
    # GAME READY TO BE STARTED

    print("\n** GAME START!! **\n")

    play_tic_tac_toe(p1, p2)

    return
