"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    # Declare the countdown variable
    countdown = 10
    # Loop as many times as numbers are in the countdown
    for i in range(countdown):
        # Print the current countdown number at the start of the loop
        print(countdown)
        # Subtract 1 from the countdown
        countdown -= 1
    # Prints end message to the screen when the loop has finished
    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
