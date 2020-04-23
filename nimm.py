"""
File: nimm.py
-------------------------
Add your comments here.
"""

import random

def main():
    stones_left = 20
    player = 1

    play_against_ai = input("Would you like to play against AI? (yes/no) ")

    while stones_left > 0:
        print("\nThere are " + str(stones_left) + " stones left")
        if player == 1 or play_against_ai == "no":
            stones_to_remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
            while stones_to_remove != 1 and stones_to_remove != 2:
                stones_to_remove = int(input("Please enter 1 or 2: "))
        else:
            if stones_left == 5 or stones_left == 4 or stones_left == 2:
                stones_to_remove = 1
            elif stones_left == 3:
                stones_to_remove = 2
            else:
                stones_to_remove = random.randint(1, 2)
            print("AI removes " + str(stones_to_remove) + " stones")

        stones_left -= stones_to_remove
        if player == 1:
            player = 2
        else:
            player = 1
    print("\n\nPlayer " + str(player) + " wins!!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
