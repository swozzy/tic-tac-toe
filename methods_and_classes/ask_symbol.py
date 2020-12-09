def ask_symbol(player):

    # Asks user if they'll be X or O
    print()
    user_in = input(str(player.get_name() + ", will you be X or O? (X/O): ")).lower()

    # Accepted inputs
    accpt_in = ["x", "o", "0"]

    # Changes "0" to an 'o' for consistency
    if user_in == "0": user_in = "o"

    # If user enters an unnacepted input
    while user_in not in accpt_in:
        print("\n!! INVALID INPUT !!")
        print("Please enter an 'X' or an 'O'.\n")
        user_in = input(player.get_name() + ", will you be X or O? (X/O): ").lower()

    # Returns
    return user_in
