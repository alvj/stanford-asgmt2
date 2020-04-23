"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

PROBLEMS_CORRECT_NEEDED = 3
MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    # Define the variable that will count the answers correct in a row
    correct_in_row = 0

    # Loop the whole program until the user has as many correct answers in a row as PROBLEMS_CORRECT_NEEDED
    while correct_in_row < PROBLEMS_CORRECT_NEEDED:
        # Generate two random numbers between MIN_RANDOM and MAX_RANDOM
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        # Calculate the correct answer
        total = num1 + num2

        # Print the operation and get the user input
        print ("What is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input("Your answer: "))

        # Check if the user answer is the same as the correct answer
        if answer == total:
            # If the answer is correct, add 1 to the count of problems correct in a row
            correct_in_row += 1
            # Print to the user that their answer is correct and how many problems correct in a row they have.
            print("Correct!   "  + "You've gotten " + str(correct_in_row) + " correct in a row." + "\n")
        else:
            # If the answer was not correct, reset the correct in a row count
            correct_in_row = 0
            # And let the user know their answer was incorrect. Print what the correct answer is.
            print ("Incorrect.   " + "The expected answer is " + str(total) + "\n")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
