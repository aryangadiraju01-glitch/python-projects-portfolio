import random
from art import logo

print(logo)

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




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card1 = random.choice(cards)
player_card2 = random.choice(cards)

player_score = player_card1 + player_card2

computer_card1 = random.choice(cards)
computer_card2 = random.choice(cards)

computer_score = computer_card1 + computer_card2

player = [player_card1,player_card2]
computer = [computer_card1,computer_card2]




print(f"Your cards {player}, current score: {player_score}")
print(f"Computer's first card: {computer_card1}")

if player_score == 21 and computer_score == 21:
    print("DRAW")
elif player_score == 21:
    print("You won!")
elif computer_score == 21:
    print("Computer won!")

else:

    while player_score < 21:

        hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit_or_pass == 'y':
            player_cards = random.choice(cards)
            player.append(player_cards)
            player_score += player_cards

            print(f"Your cards: {player}, current score: {player_score}")


        elif hit_or_pass == "n":
            print(f"Computer full hand: {computer}")
            while computer_score < 17:
                computer_cards = random.choice(cards)
                computer.append(computer_cards)
                computer_score += computer_cards


            break



print(f"Your final hand: {player}, final score: {player_score}")
print(f"Computers final hand {computer}, {computer_score}")
calculate_score(player_score,computer_score)















