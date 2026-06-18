import art

print(art.logo)

def find_winner(bidspecs):
    largest = 0
    winner = ""

    for key in bidspecs:
        if bidspecs[key] > largest:
            winner = key
            largest = bidspecs[key]

    print(f"The winner is {winner} with a bid of ${largest}")


more_bidders = True
bidspecs = {}

while more_bidders:
    print("Welcome to the Secret Auction Program")

    bidder_names = input("What is your name? : \n")
    bidder_quotes = int(input("What is your bid? : \n"))

    bidspecs[bidder_names] = bidder_quotes

    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no' : \n")

    print("\n" * 100)

    if any_other_bidders == "no":
        more_bidders = False
        find_winner(bidspecs)