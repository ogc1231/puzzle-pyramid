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
print("You finally arrive in Cario, after hours of being cramped up in a small")
print("taxi with four others, some of whom looked and smelled as if they hadn't washed in weeks.\n")

print("Luckily there was still some time to prep before venturing to the")
print("Pyramid tomorrow morning, even though the sun was getting low in the sky.\n")


while True:
    shop = input("Go shopping for items? ")

    if shop not in ["yes", "no"]:
        print("Invalid: enter 'yes or no' ")
        continue
    elif shop == "no":
        print("You find your hotel and go straight to bed ")
        exit()
    else:
        print("You head to the shop to buy some items for the morning")
        break

os.system('cls||clear')