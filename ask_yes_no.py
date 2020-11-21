# Asks user a yes-no question and returns True if the answer was a 'yes' and False if it was a 'no'.
# Comes with built-in error detection. Will keep asking user to input a valid input if they did not enter
# 'yes' or 'no'.

def ask_yes_no(question):

    # question = "Would you like to know the rules of the game? (Y/N): "

    user_in = input(question).lower()
    #user_in = user_in.lower()

    # Array filled with "yes" answers
    yes_ans = ["yes", "ye", "y", "ya", "yea", "yeah", "yup"]
    # Array filled with "no" answers
    no_ans = ["no", "n", "nah", "na", "nop", "nope"]

    # Array filled with "yes" and "no" answers
    both_ans = []
    both_ans.extend(yes_ans)
    both_ans.extend(no_ans)

    # Check to see if user_in is in either yes_ans or no_ans (by checking both_ans)

    # If it is YES/NO, skip input loop
    if user_in in both_ans:
        pass

    # Else, tell user their input was invalid.
    # Repeats until a valid input (a value in yes_ans or no_ans) is entered
    else:
        while user_in not in both_ans:
            print("\n!! INVALID INPUT !!")
            print("Please enter 'yes' or 'no'.\n")
            user_in = input(question).lower()
            print()

    if user_in in yes_ans:
        return True
    else:
        return False
