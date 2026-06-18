# Password Generator
#
# Generates a random password based on the number of
# letters, symbols, and numbers requested by the user.
#
# This project was built to practice:
# - Lists
# - Loops
# - Randomization
# - User input
# - String manipulation

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""EASY VERSION"""
# Generates a password in the order:
# letters -> symbols -> numbers

"""HARD VERSION"""

password = ""

# Store randomly selected characters before shuffling
characters = []

for i in range(nr_letters):
    i = random.randint(0, len(letters) - 1)
    characters.append(letters[i])

for i in range(nr_symbols):
    i = random.randint(0, len(symbols) - 1)
    characters.append(symbols[i])

for i in range(nr_numbers):
    i = random.randint(0, len(numbers) - 1)
    characters.append(numbers[i])

# Randomize character order to create a stronger password
random.shuffle(characters)

for char in characters:
    password += char

print(password)