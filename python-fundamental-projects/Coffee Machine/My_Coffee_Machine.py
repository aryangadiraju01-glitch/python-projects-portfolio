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



resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

balance = 0


def are_resources_sufficient(user_ingredients):
    for ingredient in user_ingredients:
        if user_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


def process_coins():
    total = 0
    total += float(input("Enter quarters: ")) * 0.25
    total += float(input("Enter dimes: ")) * 0.10
    total += float(input("Enter nickels: ")) * 0.05
    total += float(input("Enter pennies: ")) * 0.01

    return total


def successful_transaction(paid, cost_of_drink):
    if paid >= cost_of_drink:
        change = round(paid - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]

    print(f"Here is your {drink_name} ☕")


not_off = True

while not_off:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user == "off":
        not_off = False

    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${balance}")

    elif user in MENU:
        drink = MENU[user]

        if are_resources_sufficient(drink["ingredients"]):
            payment = process_coins()

            if successful_transaction(payment, drink["cost"]):
                balance += drink["cost"]
                make_coffee(user, drink["ingredients"])

    else:
        print("Invalid choice.")