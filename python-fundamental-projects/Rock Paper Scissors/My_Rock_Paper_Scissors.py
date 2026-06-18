# Rock Paper Scissors
#
# A simple command-line implementation of the classic
# Rock, Paper, Scissors game.
#
# Rules:
# - Rock beats Scissors.
# - Scissors beats Paper.
# - Paper beats Rock.
# - Matching choices result in a tie.
#
# This project was built to practice:
# - Lists
# - Conditionals
# - Random number generation
# - User input
# - Game logic

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Store the ASCII art options in a list for easy access
options = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))

# Validate user input before starting the game
if user >= 0 and user <= 2:

    # Generate the computer's choice randomly
    computer = random.randint(0, 2)

    print(f"You chose {options[user]}")
    print(f"Computer chose {options[computer]}")

    # Determine the winner based on the game rules
    if user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
        print("You Lose")
    elif user == computer:
        print("Its a Tie")
    else:
        print("You Win")

else:
    print("Invalid command inserted")