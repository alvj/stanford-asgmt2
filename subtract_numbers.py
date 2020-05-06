"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    print("This program subtracts one number from another.")
    # Get user input for both numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # Subtract both numbers
    total = num1 - num2
    # Print the total as a string
    print("The result is " + str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
