from Board import Board
from Player import Player
from ask_move import ask_move

def play_tic_tac_toe(p1, p2):

    # Creates game board
    b = Board([], [], [1, 2, 3, 4, 5, 6, 7, 8, 9], {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, p1, p2)

    # Creates a counter to keep track of how many times a player has moved
    move_counter = 0

    # Print board for user Reference
    b.print_board()

    # If p1 is first...
    # Ask p1 where to move
    # Update the board
    # Then p2 is asked where to move
    # Update the board, etc.

    if p1.get_turn() == "first":
        while(move_counter != 9):

            # P1 SEQUENCE
            index = ask_move(p1)
            b.update_p1(p1, index)
            won_flag = b.update_board(p1, index)
            b.print_board()

            move_counter = move_counter + 1

            if (move_counter == 9):
                print("!! GAME ENDED IN TIE !!")
                return
            if won_flag:
                return

            # P2 SEQUENCE
            index = ask_move(p2)
            b.update_p2(p2, index)
            won_flag = b.update_board(p2, index)
            b.print_board()

            move_counter = move_counter + 1

            if won_flag:
                return

    else:
        while(move_counter != 9):

            # P2 SEQUENCE
            index = ask_move(p2)
            b.update_p2(p2, index)
            won_flag = b.update_board(p2, index)
            b.print_board()

            move_counter = move_counter + 1

            if (move_counter == 9):
                print("!! GAME ENDED IN TIE !!")
                return
            if won_flag:
                return

            # P1 SEQUENCE
            index = ask_move(p1)
            b.update_p1(p1, index)
            won_flag = b.update_board(p1, index)
            b.print_board()

            move_counter = move_counter + 1

            if won_flag:
                return

    return
