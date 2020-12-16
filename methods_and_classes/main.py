from initialization import initialization
from play_again import play_again

# Logging imports
import logging
import logging.handlers
import os
from datetime import datetime

def main():


    logging.basicConfig(filename='game_log.log',level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M',)
    logging.info('Logs for tik tak toe game:')


    print("** WELCOME TO TIC-TAC-TOE!! **")

    initialization()

    flag = play_again()

    while flag:
        initialization()
        flag = play_again()

    print("** THANK YOU FOR PLAYING !! **")

main()
