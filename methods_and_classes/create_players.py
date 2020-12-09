from Player import Player

def create_players():

    # Creating Player 1
    p1 = Player()

    name = input("\nPlease enter Player 1's name: ").replace(" ", "")

    while not name:
        print("\n!! NOTHING WAS ENTERED !!")
        print("Please do not leave the player's name blank.\n")

        name = input("Please enter a name for Player 1: ").replace(" ", "")

    p1.set_name(name)

    # Creating Player 2
    p2 = Player()

    name = input("\nPlease enter Player 2's name: ").replace(" ", "")

    while not name:
        print("\n!! NOTHING WAS ENTERED !!")
        print("Please do not leave the player's name blank.\n")

        name = input("Please enter a name for Player 2: ").replace(" ", "")

    p2.set_name(name)

    return p1, p2
