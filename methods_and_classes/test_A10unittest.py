#################
# I M P O R T S #
#################

import unittest
# import choose_random
import play_tic_tac_toe
import choose_first
import initialization
from ask_symbol import ask_symbol
from random import randint
from Player import Player
from Board import Board

#This class implements and runs 1.b: Test random; 1.c: Test Winner; 1.d: Test Valid Input

class Test_TestTicTacToe(unittest.TestCase): #extending testcase class

    ##########################
    # TEST 1B) -- RANDOMIZER #
    ##########################

    def test_run_mult_times_1(self):
        rand = randint(0, 1)
        p1=Player("","","")
        p2=Player("","","")
        counter_p1=0
        counter_p2=0
        while (counter_p1+counter_p2) < 1001:
            rand = randint(0, 1)
            if rand:
                p1.set_turn("first")
                p2.set_turn("second")
                counter_p1 = counter_p1 + 1
            else:
                p1.set_turn("second")
                p2.set_turn("first")
                counter_p2 = counter_p2 + 1

        temp=counter_p1/1001
        print("the chance of player 1 being the first player is  " + str(temp))
        flag=False
        if temp>0.4 and temp<0.6:
            flag=True

        self.assertEqual(flag,True)
            
   
    ###########################
    # TEST 1C) -- WIN-CHECKER #
    ###########################
    
    def test_winner(self):
        p1=Player("p1","first","X")
        p2=Player("p2","second","O")
        temp=Board([],[],[],{},p1,p2)
        
        # HORIZONTAL WINNING
        temp.p1_moves=[1,2,3]
        temp.p2_moves=[4,7,8]

        self.assertEqual(temp.win_check(), True)
        
        temp.p1_moves=[9,2,3]
        temp.p2_moves=[4,5,6]
        
        self.assertEqual(temp.win_check(), True)
        
        # VERTICAL WINNING
        
        temp.p1_moves=[1,4,7]
        temp.p2_moves=[2,5,6]
        
        self.assertEqual(temp.win_check(), True)
        
        temp.p1_moves=[1,4,7]
        temp.p2_moves=[3,6,9]
        
        self.assertEqual(temp.win_check(), True)
        
        # DIAGONAL WINNING
        
        temp.p1_moves=[1,5,9]
        temp.p2_moves=[2,4,6]
        
        self.assertEqual(temp.win_check(), True)
        
        temp.p1_moves=[2,8,1]
        temp.p2_moves=[7,5,3]
        
        self.assertEqual(temp.win_check(), True)
    
    ###############################
    # TEST 1D) -- CHOOSING SYMBOL #
    ###############################
    
    def test_validinput(self):
    #I implement the logic that's used in our project
        user_input = "X" #suppose this is the input from user
        user_input = user_input.lower()
        accpt_in = ["x", "o", "0"]
        self.assertEqual(user_input in accpt_in, True)
        
        user_input = "O"
        user_input = user_input.lower()
        self.assertEqual(user_input in accpt_in, True)
        
        user_input = "0"
        user_input = user_input.lower()
        self.assertEqual(user_input in accpt_in, True)

if __name__ == "__main__":
    unittest.main()
