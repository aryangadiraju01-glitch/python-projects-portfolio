# Python Calculator
#
# A command-line calculator that performs basic arithmetic operations.
#
# Supported operations:
# - Addition
# - Subtraction
# - Multiplication
# - Division
#
# This project was built to practice:
# - Functions
# - Dictionaries
# - Loops
# - User input
# - Function calls as dictionary values

from art import logo

# Basic arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Dictionary maps operation symbols to their matching functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculating = True

print(logo)


def calculator():
    number1 = int(input("Enter the first number: "))

    while calculating:

        op = input("Enter your required operation: ")
        number2 = int(input("Enter the second number: "))

        if op in operations:
            result = operations[op](number1, number2)
            print(result)

            continue_calc = input("Do you want to continue calculating? Type 'y' for yes and 'n' for no\n").lower()

            # Continue calculating using the previous result
            if continue_calc == "y":
                number1 = result
                continue

            # Restart calculator with a new first number
            elif continue_calc == "n":
                calculator()
                return

            else:
                print("Invalid Instruction")

        else:
            print("Invalid Operation.")


calculator()