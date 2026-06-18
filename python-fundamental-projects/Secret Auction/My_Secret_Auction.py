# Secret Auction
#
# Collects bids from multiple participants and determines
# the highest bidder at the end of the auction.
#
# Rules:
# - Each bidder enters their name and bid amount.
# - Additional bidders may continue entering bids.
# - The highest bid wins the auction.
#
# This project was built to practice:
# - Dictionaries
# - Functions
# - Loops
# - User input
# - Finding maximum values

import art

print(art.logo)

# Determine the bidder with the highest bid
def find_winner(bidspecs):
    largest = 0
    winner = ""

    for key in bidspecs:
        if bidspecs[key] > largest:
            winner = key
            largest = bidspecs[key]

    print(f"The winner is {winner} with a bid of ${largest}")


more_bidders = True

# Store bidder names and bid amounts
bidspecs = {}

while more_bidders:
    print("Welcome to the Secret Auction Program")

    bidder_names = input("What is your name? : \n")
    bidder_quotes = int(input("What is your bid? : \n"))

    # Add the bidder and their bid to the dictionary
    bidspecs[bidder_names] = bidder_quotes

    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no' : \n")

    # Clear the screen by printing blank lines
    print("\n" * 100)

    if any_other_bidders == "no":
        more_bidders = False

        # Determine and display the winning bidder
        find_winner(bidspecs)