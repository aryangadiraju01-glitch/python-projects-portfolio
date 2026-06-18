print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("""You're at a cross road, Where do you want to go?
        Type "left" or "right" \n""")

if direction.lower() == "left":
    swim_or_wait = input("""You've come to a lake. There is an island in the middle of the lake.
        Type "wait" to wait for a boat. Type "swim" to swim across\n""")

    if swim_or_wait.lower() == "wait":

        door = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, which color do you choose? \n""").lower()

        if door == "blue" or door == "red":
            print("YOU LOST THE GAME! There were monsters waiting for you behind the door")


        elif door == "yellow":
            print("YOU WIN THE GAME")

        else:
            print("You chose a non-existent door. Game Over!")

    else:
        print("You chose to serve yourself as a buffet to 50 hungry Great Whites! Game Over!")


else:
    print("You fell into a Hole!. Game Over!")