# Imports
import os
import sys

# Variables
ITEM = None

# Functions
def clear():

    """
    Clear function to clean-up the terminal, to increase readability.
    """
    os.system("cls" if os.name == "nt" else "clear")

def exit_game():

    """
    Function exit game fully and not just current loop.
    """
    sys.exit()

def validate_choice(user_input, choices):
    try:
        if user_input not in choices:
            raise ValueError
    except ValueError:
        clear()
        print(f"Invalid: {user_input} is not valid.")
        input("Press enter to continue ")
        return False

    return True


def title():
    """
     Prints Puzzle Pyramid ASCII text.
    """
    print("""
 _____               _        _____                           _     _ 
|  __ \             | |      |  __ \                         (_)   | |
| |__) |   _ _______| | ___  | |__) |   _ _ __ __ _ _ __ ___  _  __| |
|  ___/ | | |_  /_  / |/ _ \ |  ___/ | | | '__/ _` | '_ ` _ \| |/ _` |
| |   | |_| |/ / / /| |  __/ | |   | |_| | | | (_| | | | | | | | (_| |
|_|    \__,_/___/___|_|\___| |_|    \__, |_|  \__,_|_| |_| |_|_|\__,_|
                                     __/ |                            
                                     |___/                             
    """)


# Game intro text
def game_intro():
    print("You finally arrive in Cario, after hours of being cramped up in a ")
    print("small taxi with four others, some of whom looked and smelled as if ")
    print("they hadn't washed in weeks.\n ")

    print("Luckily there was still some time to prep before venturing to the ")
    print("Pyramid tomorrow morning.\n ")

title()

while True:
    player_name = input("What is your name? ").capitalize()
    if player_name.isalpha():
        break
    else:
        print("Invalid: Enter a name containing letters only! ")
        continue

def enter_pyramid():

    """
    Function to start game or exit game.
    """
    while True:
        clear()
        start_game = input(f"Do wish to enter the Pyramid, {player_name}? [yes/no] ").lower()
        choices = ["yes", "no"]
        if validate_choice(start_game, choices):
            if start_game == "yes":
                clear()
                game_intro()
                
                break
            else:
                print("Thanks for playing. Goodbye!")
                exit_game()
                break
            
enter_pyramid()

def game_shop():

    """
    Function to go to the shop in game.
    """
    print("You weave your way down the narrow twisty alleys way of Cairo ")
    print("until you find the tiny shop you were looking for, excalty the same ")
    print("as the last time you were in town.\n")

    print("The shop was jammed full of everything any type of adventruer could ")
    print("dream of; ropes, torches, chisels, hammers and bizare knick-knacks. ")
    print("After browsing you head over to the shopkeeper at the counter.\n ")

    print("'So your heading to the Pyramid' says the shopkeeper. 'In that case ")
    print("only three things will be useful but you can only take one. Do you want ")
    print("the rope, the torch or the ankh?'\n ")

def game_main():

    """
    Function to start main game.
    """
    print("You wake up before the sun ready for action, after gathering all your ")
    print("you are ready to ventrure forth. You hail a taxi which brings you to ")
    print("the desert, where two men dressed in white sand robes are waiting.\n ")

    print("You finally mount the bad-tempered camel and start the slow journey ")
    print("to the Pyramid. You arrive just after midday as the heat of the sun ")
    print("is starting to get unbearable. The guides lead to the entrance and ")
    print("one of them wishes you luck, while the other warns that most who enter")
    print("are never seen again.\n ")

def shopping():

    """
    Function to choose to go shopping or not.
    """
    while True:
        shop = input("Go shopping for items? [yes/no] ").lower()
        choices = ["yes", "no"]
        if validate_choice(shop, choices):
            if shop == "no":
                clear()
                print("You find your hotel and go straight to bed.\n ")
                game_main()
                break
            else:
                clear()
                print("You head to the shop to buy some items for the morning.\n ")
                game_shop()
                break
shopping()

def ITEM_choice():

    """
    Function to choose ITEM from shop.
    """
    while True:
        ITEM = input("Choose one of the options: rope, torch or ankh? ")
        choices = ["rope", "torch", "ankh"]
        if validate_choice(ITEM, choices):
            if ITEM == "rope":
                clear()
                print(f"You have chosen the {ITEM}!\n ")
                print("After shopping you find your way back to the hotel.\n ")
                game_main()
                break
            elif ITEM == "torch":
                clear()
                print(f"You have chosen the {ITEM}!\n ")
                print("After shopping you find your way back to the hotel.\n ")
                game_main()
                break
            else:
                clear()
                print(f"You have chosen the {ITEM}!\n ")
                print("After shopping you find your way back to the hotel.\n ")
                game_main()
                break

ITEM_choice()

def entrance_open():

    """
    Function after correct answer is entered
    """
    clear()
    print("The doors open with a low rumble, throwning red dust into the air.")
    print("You hesitantly walk ing, letting your eye adjust to the gloomy ")
    print("light inside. You come to a juction with a path lead left and")
    print("another leading to the right. There is also a high ledge with")
    print("a hook above it, maybe some sort of tool would be useful here?\n ")


def game_0():

    """
    Function to call game_0
    """
    print("As you approach the entrance you hear voice inside your head. To open")
    print("this door you must first answer this questions.\n ")

    while True:
        entrance_q = input("What creature has a human head and body of a lion? ").lower()
        choices = ["sphinx"]
        if validate_choice(entrance_q, choices):
            if entrance_q == "sphinx":
                clear()
                entrance_open()
                break

game_0()

def level_1():

    """
    Function after correct answer is entered at entrance door
    """
    while True:
        direction1 = input("Use rope or go left or right [rope/left/right] ").lower()
        choices = ["rope", "left", "right"]
        if validate_choice(direction1, choices):
            if  ITEM == "rope":
                print("You mange to loop the rope around the hook and pull yourself up! ")
                # game1()
                break
            elif direction1 == "left":
                print("You walk down the left corrider getting a face full of acient")
                print("cobwebs. After wiping your face you see human bones and skulls")
                print("You reluctantly move forward, you put down your foot and hear")
                print("a soft click. Bolts shoot out from the both sides.")
                print("You died!")
                entrance_open()
                break
            else:
                print("You walk down the right corrider, it seems to clear.")
                print("You continue on coming to another junction")
                while True:
                    direction2 = input("Go left, right! [left/right]").lower()
                    choices = ["left", "right"]
                    if validate_choice(direction2, choices):
                        if direction2 == "left":
                            print("At the end of corrider there is a set of stairs which you")
                            print("climb, bringing you up to the next floor.")
                            # game1()
                            break
                        else:
                            print("You walk down the right corrider, which seems be getting")
                            print("narrower and lower as you go. You eventually have to")
                            print("continue on your hands and knee and then crawling on your")
                            print("stomach. You see light on the end of the tunnel and press")
                            print("on, however after a few minutes you realise you are stuck")
                            print("just a few metres away from the exit. No amount of")
                            print("seems to help. You start to scream for help but no one can")
                            print("hear you!")
                            print("You died!")
                            entrance_open()
                            break

level_1()




# Game 1 - Rock, paper, scissors with MUMMY

# Game 2 - Mutiple choice quiz to pass Jackal-headed guards

# Game 3 - Noughts and crosses with Anubis