from initialization import initialization
from play_again import play_again

def main():

    initialization()

    flag = play_again()

    if not flag:
        print("\n** THANK YOU FOR PLAYING !! **")

    while flag:
        initialization()
        flag = play_again()

    print("\n** THANK YOU FOR PLAYING !! **")

main()
