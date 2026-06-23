import art
import random
from game_data import data

print(art.logo)

# Stores the two current accounts being compared.
selections = []

# Keeps track of the player's score.
score = 0


def make_selections(dataset):
    """Select two random accounts from the dataset."""
    for index in range(2):
        random_selections = random.randint(0, len(dataset) - 1)
        selections.append(dataset[random_selections])

    return selections


selected = make_selections(data)


def prompt_user(current_list):
    """Display both accounts and ask the user for a choice."""
    print(f"Compare A: {selected[0]['name']}, a {selected[0]['description']} from, {selected[0]['country']}")

    print(art.vs)

    print(f"Against B: {selected[1]['name']}, a {selected[1]['description']} from, {selected[1]['country']}")

    user_choice = input("Who has more followers on instagram? Type 'A' or 'B': ").upper()

    return user_choice


def compare(points, dataset):
    """Main game loop that handles scoring and comparisons."""

    not_lost = True

    while not_lost:

        # Prevent the same account from being compared against itself.
        while selected[0]["name"] == selected[1]["name"]:
            selected[1] = random.choice(dataset)

        choice = prompt_user(selected)

        # Exit the game if the user enters an invalid option.
        if choice != "A" and choice != "B":
            print("Input Violation!. Program has exited")
            return

        # User correctly chose account A.
        elif choice == "A" and selected[0]["follower_count"] > selected[1]["follower_count"]:
            points += 1
            print(f"You're Right! Current score: {points}")

            # Remove the losing account and replace it with a new one.
            loser = selected[1]
            selected.remove(loser)
            dataset.remove(loser)

            random_selections = random.randint(0, len(dataset) - 1)
            selections.append(dataset[random_selections])

        # User correctly chose account B.
        elif choice == "B" and selected[0]["follower_count"] < selected[1]["follower_count"]:
            points += 1
            print(f"You're Right! Current score: {points}")

            # Remove the losing account and replace it with a new one.
            loser = selected[0]
            selected.remove(loser)
            dataset.remove(loser)

            random_selections = random.randint(0, len(dataset) - 1)
            selections.append(dataset[random_selections])

        # User guessed incorrectly.
        else:
            print("Wrong")
            not_lost = False

    print(f"You Lost! Your total streak was {points}")


compare(score, data)