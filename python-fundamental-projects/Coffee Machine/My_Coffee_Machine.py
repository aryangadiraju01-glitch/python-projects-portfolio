MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Tracks the current machine resources.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Tracks the total money earned by the coffee machine.
balance = 0


def are_resources_sufficient(user_ingredients):
    """Check if the machine has enough resources for the selected drink."""
    for ingredient in user_ingredients:
        if user_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


def process_coins():
    """Calculate the total amount of money inserted by the user."""
    total = 0
    total += float(input("Enter quarters: ")) * 0.25
    total += float(input("Enter dimes: ")) * 0.10
    total += float(input("Enter nickels: ")) * 0.05
    total += float(input("Enter pennies: ")) * 0.01

    return total


def successful_transaction(paid, cost_of_drink):
    """Return True if the user inserted enough money for the drink."""
    if paid >= cost_of_drink:
        change = round(paid - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients from resources and serve the selected drink."""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]

    print(f"Here is your {drink_name} ☕")


# Main program loop. Runs until the user enters "off".
not_off = True

while not_off:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turns off the coffee machine.
    if user == "off":
        not_off = False

    # Prints a report of remaining resources and money earned.
    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${balance}")

    # Handles a valid drink order.
    elif user in MENU:
        drink = MENU[user]

        if are_resources_sufficient(drink["ingredients"]):
            payment = process_coins()

            if successful_transaction(payment, drink["cost"]):
                balance += drink["cost"]
                make_coffee(user, drink["ingredients"])

    # Handles invalid menu choices.
    else:
        print("Invalid choice.")