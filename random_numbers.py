"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

# Declare constants
NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    # Loop as much times as NUM_RANDOM says,
    # printing a random number between MIN_RANDOM and MAX_RANDOM for every time.´
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
