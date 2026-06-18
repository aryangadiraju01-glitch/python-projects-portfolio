# Blackjack Game
#
# Rules implemented:
# - Player and dealer are each dealt two starting cards.
# - The player may choose to draw additional cards ("hit") or stop ("stand").
# - Once the player stands, the dealer automatically draws until reaching a score of at least 17.
# - A score above 21 results in a bust.
# - The highest score at or below 21 wins.
#
# Assumptions:
# - Face cards (Jack, Queen, King) are represented as 10.
# - An Ace is currently always treated as 11.
# - Ace adjustment logic (switching an Ace from 11 to 1 to prevent a bust)
#   has not been implemented in this version.
#
# This project was built to practice:
# - Lists
# - Loops
# - Conditionals
# - Functions
# - Random number generation
# - Basic game logic

import random
from art import logo

print(logo)

# Determines the winner based on the final scores
def calculate_score(score_of_player, score_of_computer):
    if score_of_player > 21:
        print("Player busts. Dealer WINS!")
    elif score_of_computer > 21:
        print("Dealer busts. Player WINS!")
    elif score_of_player > score_of_computer:
        print("Player WINS!")
    elif score_of_player < score_of_computer:
        print("Dealer WINS!")
    else:
        print("DRAW")


# Standard Blackjack card values (Ace is currently always treated as 11)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deal two starting cards to both player and dealer
player_card1 = random.choice(cards)
player_card2 = random.choice(cards)

player_score = player_card1 + player_card2

computer_card1 = random.choice(cards)
computer_card2 = random.choice(cards)

computer_score = computer_card1 + computer_card2

# Store hands in lists for display and future card additions
player = [player_card1, player_card2]
computer = [computer_card1, computer_card2]

print(f"Your cards {player}, current score: {player_score}")
print(f"Computer's first card: {computer_card1}")

# Check for an immediate Blackjack before gameplay begins
if player_score == 21 and computer_score == 21:
    print("DRAW")
elif player_score == 21:
    print("You won!")
elif computer_score == 21:
    print("Computer won!")

else:

    # Player continues taking turns until they stand or bust
    while player_score < 21:

        hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")

        # Draw a new card and update the player's score
        if hit_or_pass == 'y':
            player_cards = random.choice(cards)
            player.append(player_cards)
            player_score += player_cards

            print(f"Your cards: {player}, current score: {player_score}")

        elif hit_or_pass == "n":
            print(f"Computer full hand: {computer}")

            # Dealer draws cards until reaching a score of at least 17
            while computer_score < 17:
                computer_cards = random.choice(cards)
                computer.append(computer_cards)
                computer_score += computer_cards

            break

# Display final results and determine the winner
print(f"Your final hand: {player}, final score: {player_score}")
print(f"Computers final hand {computer}, {computer_score}")
calculate_score(player_score, computer_score)