# print("""
#   _____               _        _____                           _     _ 
#  |  __ \             | |      |  __ \                         (_)   | |
#  | |__) |   _ _______| | ___  | |__) |   _ _ __ __ _ _ __ ___  _  __| |
#  |  ___/ | | |_  /_  / |/ _ \ |  ___/ | | | '__/ _` | '_ ` _ \| |/ _` |
#  | |   | |_| |/ / / /| |  __/ | |   | |_| | | | (_| | | | | | | | (_| |
#  |_|    \__,_/___/___|_|\___| |_|    \__, |_|  \__,_|_| |_| |_|_|\__,_|
#                                       __/ |                            
#                                      |___/                             
# """)

import os
os.system('cls||clear')

player_name = input("What is your name? ").capitalize()

while True:
    play = input(f"Do wish to enter the Pyramid, {player_name}? ").lower()

    if play not in ["yes", "no"]:
        print("Invalid: enter 'yes or no' ")
        continue
    elif play == "no":
        print("Thanks for playing, goodbye! ")
        exit()
    else:
        break

os.system('cls||clear')

# Intro section
print("You finally arrive in Cario, after hours of being cramped up in a ")
print("small taxi with four others, some of whom looked and smelled as if ")
print("they hadn't washed in weeks.\n ")

print("Luckily there was still some time to prep before venturing to the ")
print("Pyramid tomorrow morning, even though the sun was getting low ")
print("in the sky.\n ")


while True:
    shop = input("Go shopping for items? ")

    if shop not in ["yes", "no"]:
        print("Invalid: enter 'yes or no' ")
        continue
    elif shop == "no":
        print("You find your hotel and go straight to bed. ")
        # define game-------
    else:
        print("You head to the shop to buy some items for the morning. ")
        break

os.system('cls||clear')

# define shop-------
print("You weave your way down the narrow twisty alleys way of Cairo ")
print("until you find the tiny shop you were looking for, excalty the same ")
print("as the last time you were in town.\n")

print("The shop was jammed full of everything any type of adventruer could ")
print("dream of; ropes, torches, chisels, hammers and bizare knick-knacks. ")
print("After browsing you head over to the shopkeeper at the counter.\n ")

print("'So your heading to the Pyramid' says the shopkeeper. 'In that case ")
print("only three things will be useful but can only take one. Do you want ")
print("the rope, the torch or the ankh?'\n ")

while True:
    item_choosen = input("Choose one of the options: rope, torch or ankh? ")

    if item_choosen not in ("rope", "torch", "ankh"):
        print("Invalid: enter 'rope', 'torch' or 'ankh' ")
        continue
    elif item_choosen == "rope":
        print("You have choosen the rope! ")
        # Start game-------
    elif item_choosen == "torch":
        print("You have choosen the torch! ")
        # Start game-------
    else:
        print("You have choosen the ankh! ")
        # Start game-------

    break


os.system('cls||clear')


# Start Game -----------------------------
print("You wake up befre the sun ready for action, after gathering all your ")
print("you are ready to ventrure forth. You hail a taxi which brings you to ")
print("the desert, where two men dressed in white sand robes are waiting.\n ")

print("You finally mount the bad-tempered camel and start the slow journey ")
print("to the Pyramid. You arrive just after midday as the heat of the sun ")
print("is starting to get unbearable. The guides lead to the entrance and ")
print("one of them wishes you luck, while the other warns that most who enter")
print("are never seen again.")

os.system('cls||clear')

# Game 0 - Answer question to open entrance doors




# Game 1 - Rock, paper, scissors with MUMMY

# Game 2 - Mutiple choice quiz to pass Jackal-headed guards

# Game 3 - Noughts and crosses with Anubis