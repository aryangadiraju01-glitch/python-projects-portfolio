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

options = [rock,paper,scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))

if user >=1 and user <= 3:

    computer = random.randint(0,2)

    print(f"You chose {options[user]}")

    print(f"Computer chose {options[computer]}")

    if user == 0 and computer == 1 or user == 1 and computer == 3 or user == 3 and computer == 1:
        print("You Lose")
    elif user == computer:
        print("Its a Tie")
    else:
        print("You Win")



else:
    print("Invalid command inserted")






