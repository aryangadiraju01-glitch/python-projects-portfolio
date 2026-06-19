# Number Guessing Game
#
#
# What I learned:
# - Breaking a program into functions
# - Returning values from functions
# - Passing arguments between functions
# - Using while loops to control game flow
# - Generating random numbers with the random module
# - Managing attempts and win/loss conditions

import random

from art import logo

print(logo)


def play_game():

    # Generate a random number between 1 and 100
    def choose_number():
        number = random.randint(1, 100)
        return number

    answer = choose_number()

    # Set the number of attempts based on difficulty
    def set_difficulty():

        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid Choice")

    attempts = set_difficulty()

    # Compare the user's guess to the secret number
    def get_and_check_guess(right_number):

        user_guess = int(input("Make a guess: "))

        if user_guess > 100 or user_guess < 1:
            print("Please enter a number between 1 and 100.")
            return False


        elif user_guess > right_number:
            print("Too High")
            return False

        elif user_guess == right_number:
            print("Correct!")
            return True

        else:
            print("Too Low")
            return False

    # Main game loop
    while attempts > 0:

        print(f"You have {attempts} attempts left")

        correct = get_and_check_guess(answer)

        attempts -= 1

        if correct:
            print("You win")
            break

        elif attempts == 0:
            print(f"You've run out of guesses, You Lose. The number was {answer}")


play_game()