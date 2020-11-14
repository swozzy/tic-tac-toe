#The code for win_check is in Board.py
import unittest
from Player import Player
import play_tic_tac_toe
from Board import Board
import ask_symbol

#This class implements and runs 1.b: Test random; 1.c: Test Winner; 1.d: Test Valid Input

class Test_TestTicTacToe(unittest.TestCase): #extending testcase class

    #1.b Test random





    #1.c Test winner
    def test_winner(self):
        p1=Player("p1","first","X")
        p2=Player("p2","second","O")
        temp=Board([],[],[],{},p1,p2)
        temp.p1_moves=[1,2,3]
        temp.p2_moves=[4,7,8]

        self.assertEqual(temp.win_check(),True)
        
    #1.d Test Valid Input





        

if __name__ == "__main__":
    unittest.main()