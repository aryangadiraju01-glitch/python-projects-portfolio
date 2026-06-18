# Hangman Game
#
# Rules:
# - A random word is selected from the word list.
# - The player guesses one letter at a time.
# - Correct guesses reveal all matching letters in the word.
# - Incorrect guesses cost one life.
# - The game ends when the word is guessed or all lives are lost.
#
# This project was built to practice:
# - Lists
# - Loops
# - Strings
# - Conditional statements
# - Modules and imports
# - Game logic

import hangman_words
import random
from hangman_art import logo, stages

print(logo)

# Select a random word from the word list
random_word = random.choice(hangman_words.word_list)

#print(random_word)

lives = 6

game_over = False
guessed_letters = ""

# Continue playing until the player wins or loses
while not game_over:

    print(f"Number of lives left : {lives}")
    guess = input("Enter a letter as your guess:\n").lower()

    # Prevent duplicate guesses from going unnoticed
    if guess in guessed_letters:
        print(f"You have already guessed the letter: {guess}")

    guessed_letters += guess

    display = ""

    # Build the current word display using guessed letters
    for letter in random_word:
        if letter in guessed_letters:
            display += letter

        else:
            display += "_"

    print(display)

    # Deduct a life for an incorrect guess
    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess} which is not in the word. You Lose a Life")

        if lives == 0:
            game_over = True
            print(f"You lost the game! The word was {random_word}")

    # Check if the entire word has been guessed
    if "_" not in display:
        game_over = True
        print("************ YOU WIN ***********")

    # Display the current Hangman stage
    print(stages[lives])