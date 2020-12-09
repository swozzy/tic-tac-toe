# Imports
from Player import Player
from random import randint
import logging
import logging.handlers
import os
from datetime import datetime

# Sets either Player 1 or Player 2 be first
# The player not chosen first goes second
def choose_first(p1, p2):

    log = logging.getLogger("main")
  #  logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y:%m:%d %I:%M:%S %p')
  #  handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE","app-log.log"))
   # handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
   # log.addHandler(handler)
   # log.setLevel(logging.INFO)

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
        log.info("** " + p1.get_name() + " will go first and " + p2.get_name() + " will go second **222")
    #elif p2.get_turn() == "first":
    else:
        print("** " + p2.get_name() + " will go first and " + p1.get_name() + " will go second **")
        log.info("** " + p2.get_name() + " will go first and " + p1.get_name() + " will go second **111")

