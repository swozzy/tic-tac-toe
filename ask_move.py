# Asks a player to choose a spot on gameboard. Returns that index
def ask_move(player):

    # Prompts user
    user_in = int(input(player.get_name() + ", please choose an empty spot to move to: "))

    # Makes sure they enter a number 1 - 9
    while user_in not in range(1, 10):
        print("\n!! INVALID INPUT !!")
        print("Please enter a number (1-9) that corresponds to a spot on the gameboard")

        # RIGHT NOW ASSUMES THAT PLAYER CORRECTLY CHOOSES SPOT
        # BREAKS IF STRING ENTERED
        user_in = int(input("\n" + player.get_name() + ", please choose an empty spot to move to: "))

    return user_in
