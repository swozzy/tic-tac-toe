# Imports
from random import randint
import os

# I took the original method's logic and simplified it so that
# I can check its validity more easily in a testing environment

def choose_first():

    rand = randint(0, 1)

    if rand:
        return 1
    return 0

def run_mult_times():

    # Counter for randomizer
    c = 0

    # Run above method a bunch of times
    for i in range(10000000):
        c = c + choose_first()
        i = i + 1

    print(c/100000)

    # Returns a percentage (~50%)
    return c/100000

if __name__ == "__main__":

    run_mult_times()
