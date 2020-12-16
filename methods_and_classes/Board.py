# 'Board' class
import logging
import logging.handlers
import os
from datetime import datetime
class Board():

    # Initialization. Holds board, board information, and player moves
    def __init__(self, p1_moves, p2_moves, free_spots, dup_board, p1, p2):

        self.p1_moves = p1_moves
        self.p2_moves = p2_moves
        self.free_spots = free_spots
        self.dup_board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
        self.p1 = p1
        self.p2 = p2

    # Removes that free spot from free_spots
    # ... and adds it to that player's array of moves
    def update_p1(self, player, index):
        self.p1_moves.append(index)

    def update_p2(self, player, index):
        self.p2_moves.append(index)

    def get_freespots(self):
        return self.free_spots

    # Uses .formatting() to print board
    def print_board(self):
        
        print()
        row_counter = 1

        for i in self.dup_board:
            if (i%3 == 0) and (row_counter != 9):
                print(self.dup_board[i],end='')
                print("\n---------")
            else:
                if row_counter != 9:
                    print(self.dup_board[i], '| ', end='')
                else:
                    print(self.dup_board[i])

            row_counter += 1
        print()

    def check_before_update(self,player, index):
        if index in self.free_spots:
            
            return True
        else:
            return False

    def update_board(self, player, index):

        self.free_spots.remove(index)
        self.dup_board[index] = player.get_symbol().upper()

        return self.win_check()

    # Checks all winning conditions
    def win_check(self):
       # log = logging.getLogger("main")
        # For Reference
       # winning_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], \
                       #      [1, 4, 7], [2, 5, 8], [3, 6, 9], \
                        #     [1, 5, 9], [3, 5, 7]]

        if ((1 in self.p1_moves) and (2 in self.p1_moves) and (3 in self.p1_moves)) or \
        ((4 in self.p1_moves) and (5 in self.p1_moves) and (6 in self.p1_moves)) or \
        ((7 in self.p1_moves) and (8 in self.p1_moves) and (9 in self.p1_moves)) or \
        ((1 in self.p1_moves) and (4 in self.p1_moves) and (7 in self.p1_moves)) or \
        ((2 in self.p1_moves) and (5 in self.p1_moves) and (8 in self.p1_moves)) or \
        ((3 in self.p1_moves) and (6 in self.p1_moves) and (9 in self.p1_moves)) or \
        ((1 in self.p1_moves) and (5 in self.p1_moves) and (9 in self.p1_moves)) or \
        ((3 in self.p1_moves) and (5 in self.p1_moves) and (7 in self.p1_moves)):
            print("\n!! CONGRATULATIONS !!")
            print("** " + self.p1.get_name().upper() + " WON **")
            logging.info("** " + self.p1.get_name().upper() + " WON **")
            return True

        elif ((1 in self.p2_moves) and (2 in self.p2_moves) and (3 in self.p2_moves)) or \
        ((4 in self.p2_moves) and (5 in self.p2_moves) and (6 in self.p2_moves)) or \
        ((7 in self.p2_moves) and (8 in self.p2_moves) and (9 in self.p2_moves)) or \
        ((1 in self.p2_moves) and (4 in self.p2_moves) and (7 in self.p2_moves)) or \
        ((2 in self.p2_moves) and (5 in self.p2_moves) and (8 in self.p2_moves)) or \
        ((3 in self.p2_moves) and (6 in self.p2_moves) and (9 in self.p2_moves)) or \
        ((1 in self.p2_moves) and (5 in self.p2_moves) and (9 in self.p2_moves)) or \
        ((3 in self.p2_moves) and (5 in self.p2_moves) and (7 in self.p2_moves)):
            print("\n!! CONGRATULATIONS !!")
            print("** " + self.p2.get_name().upper() + " WON **")
            logging.info("** " + self.p1.get_name().upper() + " WON **")
            return True

        return False
