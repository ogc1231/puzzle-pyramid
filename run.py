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
        print("let's go")
        break

os.system('cls||clear')
print("You finally arrive in Cario after hours of being cramped up in a small taxi with four others,")
print("some of which looked and smelled as if they hadn't washed in weeks.")
print("Luckily you arrive in time to gather a few items before venturing to the Pyramid tommorrow morning")
input("")