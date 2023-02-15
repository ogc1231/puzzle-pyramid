# Imports
import os
import sys
import random

# Variables
ITEM = None
PLAYER = None

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
    """) # noqa


# Game intro text
def game_intro():
    print("You finally arrive in Cario, after hours of being cramped up in a ")
    print("small taxi with four others, some of whom looked and smelled as if ")
    print("they hadn't washed in weeks.\n ")

    print("Luckily there was still some time to prep before venturing to the ")
    print("Pyramid tomorrow morning.\n ")

    shopping()

def player_name():
    
    """
    Function input player's name.
    """

    global PLAYER
    while True:
        PLAYER = input("What is your name? ").capitalize()
        if PLAYER.isalpha() and len(PLAYER) >= 2:
            break
        else:
            clear()
            title()
            print("Invalid: Enter a name containing at least 2 letters!")
            continue

def enter_pyramid():

    """
    Function to start game or exit game.
    """
    global PLAYER
    while True:
        clear()
        start_game = input(
            f"Do wish to enter the Pyramid, {PLAYER}? [yes/no] "
        ).lower()
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

    item_choice()

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

    game_0()

def shopping():

    """
    Function to choose to go shopping or not.
    """
    while True:
        shop = input("Go shopping for items? [yes/no] ").lower()
        choices = ["yes", "no"]
        if validate_choice(shop, choices):
            break

    if shop == "no":
        clear()
        print("You find your hotel and go straight to bed.\n ")
        game_main()
    else:
        clear()
        print("You head to the shop to buy some items for the morning.\n ")
        game_shop()

def item_choice():

    """
    Function to choose ITEM from shop.
    """
    global ITEM
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

def level_1():
    """
    Function after correct answer is entered at entrance door
    """
    global ITEM
    while True:
        if ITEM is not None and ITEM == "rope":
            direction1 = input("Use rope or go left or right [rope/left/right] ").lower()
            choices = ["rope", "left", "right"]
        else:
            direction1 = input("Go left or right [left/right] ").lower()
            choices = ["left", "right"]
        if validate_choice(direction1, choices):
            break

    if ITEM is not None and ITEM == "rope":
        clear()
        print("You mange to loop the rope around the hook and pull yourself up!\n")
        game_1()
    elif direction1 == "left":
        clear()
        print("You walk down the left corrider getting a face full of acient")
        print("cobwebs. After wiping your face you see human bones and skulls")
        print("You reluctantly move forward, you put down your foot and hear")
        print("a soft click. Bolts shoot out from the both sides.")
        print("\nYou died!")
        exit_game()
    else:
        clear()
        print("You walk down the right corrider, it seems to clear.")
        print("You continue on coming to another junction")
        while True:
            direction2 = input("Go left, right! [left/right] ").lower()
            choices = ["left", "right"]
            if validate_choice(direction2, choices):
                break

        if direction2 == "left":
            clear()
            print("At the end of corrider there is a set of stairs which you")
            print("climb, bringing you up to the next floor.\n ")
            game_1()
        else:
            clear()
            print("You walk down the right corrider, which seems be getting")
            print("narrower and lower as you go. You eventually have to")
            print("continue on your hands and knee and then crawling on your")
            print("stomach. You see light on the end of the tunnel and press")
            print("on, however after a few minutes you realise you are stuck")
            print("just a few metres away from the exit. No amount of")
            print("seems to help. You start to scream for help but no one can")
            print("hear you!")
            print("\nYou died!")
            exit_game()

def entrance_open():

    """
    Function after correct answer is entered
    """
    clear()
    print("The doors open with a low rumble, throwing red dust into the air.")
    print("You hesitantly walk ing, letting your eye adjust to the gloomy ")
    print("light inside. You come to a junction with a path lead left and")
    print("another leading to the right. There is also a high ledge with")
    print("a hook above it, maybe some sort of tool would be useful here?\n ")

    level_1()


def game_0():

    """
    Function to call game_0
    """
    clear()
    print("As you approach the entrance you hear voice inside your head. To open")
    print("this door you must first answer this questions.\n ")

    while True:
        entrance_q = input("What creature has a human head and body of a lion? ").lower()
        choices = ["sphinx"]
        if validate_choice(entrance_q, choices):
            clear()
            entrance_open()
            break

def game_1():

    """
    Function to run first game: rock, paper, scissors.
    """
    print("You enter a lower chamber with a low ceiling. At the sound of your")
    print("footsteps a MUMMY turns arounding grinning it's rotten teeth at you ")
    print("MUMMY: Ah another victim, good as I was getting hungry. I will")
    print("however give you a chance, beat me at my favoutite game and")
    print("will let you live, but if you lose you will never leave this room.")
    print("READY!\n ")

    hand = ("rock", "paper", "scissors")
    player_wins = 0
    mummy_wins = 0

    while mummy_wins < 3 and player_wins < 3:
        player_hand = None
        mummy_hand = random.choice(hand)

        print(f"Your Score: {player_wins}")
        print(f"Mummy Score: {mummy_wins}")

        while player_hand not in hand:
            player_hand = input("Choose a hand (rock, paper or scissors): ").lower()

        clear()
        print(f"You chose {player_hand}! ")
        print(f"The Mummy chose {mummy_hand}!")

        if player_hand == mummy_hand:
            print("It's a tie, again human!\n")
        elif player_hand == "rock" and mummy_hand == "scissors":
            print("You win!")
            player_wins += 1
            print("Mummy: You're better than you look!\n")
        elif player_hand == "scissors" and mummy_hand == "paper":
            print("You win!")
            player_wins += 1
            print("Mummy: Arrhh, not possible\n")
        elif player_hand == "paper" and mummy_hand == "rock":
            print("You win!")
            player_wins += 1
            print("Mummy: How did you beat me!")
        else:
            print("Mummy: Bahahaha! I won that round. Let's try another.\n")
            mummy_wins += 1

    if mummy_wins == 3:
        clear()
        print(f"Your Score: {player_wins}")
        print(f"Mummy Score: {mummy_wins}")
        print("\nUnfortunately the mummy beat you. Game Over!")
        exit_game()
    elif player_wins == 3:
        clear()
        print(f"Your Score: {player_wins}")
        print(f"Mummy Score: {mummy_wins}")
        input("proceed to next room/game")


if __name__ == "__main__":
    clear()
    title()
    player_name()
    enter_pyramid()











# Game 1 - Rock, paper, scissors with MUMMY

# Game 2 - Mutiple choice quiz to pass Jackal-headed guards

# Game 3 - Noughts and crosses with Anubis