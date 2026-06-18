from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

calculating = True

print(logo)


def calculator():
    number1 = int(input("Enter the first number: "))

    while calculating:

        op = input("Enter your required operation: ")
        number2 = int(input("Enter the second number: "))

        if op in operations:
            print(operations[op](number1, number2))

            continue_calc = input("Do you want to continue calculating? Type 'y' for yes and 'n' for no\n").lower()

            if continue_calc == "y":
                number1 = operations[op](number1, number2)
                continue
            elif continue_calc == "n":
                calculator()
                return
            else:
                print("Invalid Instruction")

        else:
            print("Invalid Operation.")


calculator()