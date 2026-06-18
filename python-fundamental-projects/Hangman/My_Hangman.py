import hangman_words
import random
from hangman_art import logo, stages

print(logo)

random_word = random.choice(hangman_words.word_list)

print(random_word)


lives = 6

game_over = False
guessed_letters = ""

while not game_over:

    print(f"Number of lives left : {lives}")
    guess = input("Enter a letter as your guess:\n").lower()

    if guess in guessed_letters:
        print(f"You have already guessed the letter: {guess}")

    guessed_letters += guess

    display = ""

    for letter in random_word:
        if letter in guessed_letters:
            display += letter

        else:
            display += "_"


    print(display)


    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess} which is not in the word. You Lose a Life")
        if lives == 0:
            game_over = True
            print(f"You lost the game! The word was {random_word}")



    if "_" not in display:
        game_over = True
        print("************ YOU WIN ***********")



    print(stages[lives])











