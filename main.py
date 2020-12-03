from initialization import initialization
from play_again import play_again
import logging
import logging.handlers
import os
from datetime import datetime

def main():

    log = logging.getLogger("main")
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y:%m:%d %I:%M:%S %p')
    logging.basicConfig(level=os.environ.get("LOGLEVEL","INFO"))
    handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE","game-log.log"))
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info("Game start")



    initialization()

    flag = play_again()

    # CHANGE THIS SO IT DOESN'T PRINT TWICE

    if not flag:
        print("\n** THANK YOU FOR PLAYING !! **")

    while flag:
        initialization()
        flag = play_again()

    print("\n** THANK YOU FOR PLAYING !! **")

main()
