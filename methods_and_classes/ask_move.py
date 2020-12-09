# Asks a player to choose a spot on gameboard. Returns that index
# Check if a player's move is valid
def ask_move(player):

    # Prompts user
    user_in = (input(player.get_name() + ", please choose an empty spot to move to: "))


    #This is to make sure that the user does not in put anything else but integers from 1-9
    #It handles the case where user may input letters etc.
    while user_in not in ['1','2','3','4','5','6','7','8','9']:

        print("\n!! INVALID INPUT")
        print("Please enter a number (1-9) that corresponds to a spot on the gameboard")

        user_in =(input("\n" + player.get_name() + ", please choose an empty spot to move to: "))

    
    user_in = int(user_in)


    return user_in
