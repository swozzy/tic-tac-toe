from Player import Player
from ask_symbol import ask_symbol
import logging
import os
from datetime import datetime

def choose_symbols(p1, p2):

    # If p1 is first, they choose symbol first
    if p1.get_turn() == "first":

        p1_symb = ask_symbol(p1)

        # If p1 chooses 'x', p2 gets 'o'
        if p1_symb == "x":
            p1.set_symbol("x")
            p2.set_symbol("o")

        # If p1 chooses 'o', p2 gets 'x'
        if p1_symb == "o":
            p1.set_symbol("o")
            p2.set_symbol("x")

    # Otherwise, p2 chooses symbol first
    else:
        p2_symb = ask_symbol(p2)

        # If p2 chooses 'x', p1 gets 'o'
        if p2_symb == "x":
            p1.set_symbol("o")
            p2.set_symbol("x")

        # If p2 chooses 'o', p1 gets 'x'
        if p2_symb == "o":
            p1.set_symbol("x")
            p2.set_symbol("o")

    # Prints users' symbols for clarification
    logging.info("** " + p1.get_name() + " has the symbol  " + p1.get_symbol().upper() + " and " + p2.get_name() + " has the symbol  " + p2.get_symbol().upper()+" **")
    print("\n" + p1.get_name() + " is '" + p1.get_symbol().upper() + "' and " + p2.get_name() + " will be '" + p2.get_symbol().upper() + "'")
