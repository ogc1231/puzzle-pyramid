import random
import sys


def game_1():

    """
    Function after correct answer is entered
    """

    hand = ("rock", "paper", "scissors")
    player_wins = 0
    mummy_wins = 0

    while mummy_wins < 3 and player_wins < 3:
        player_hand = None
        mummy_hand = random.choice(hand)

        while player_hand not in hand:
            player_hand = input("Choose a hand (rock, paper or scissors): ").lower()

        print(f"You chose {player_hand}! ")
        print(f"The Mummy chose {mummy_hand}!")

        if player_hand == mummy_hand:
            print("It's a tie!")
        elif player_hand == "rock" and mummy_hand == "scissors":
            print("You win!")
            player_wins += 1
            print("Mummy: Your better than you look!")
        elif player_hand == "scissors" and mummy_hand == "paper":
            print("You win!")
            player_wins += 1
            print("Mummy: Arrhh, not possible")
        elif player_hand == "paper" and mummy_hand == "rock":
            print("You win!")
            player_wins += 1
            print("Mummy: How did you beat me!")
        else:
            print("Mummy: Bahahaha! I won that round. Let's try another.")
            mummy_wins += 1

    if mummy_wins == 3:
        print("Unfortunately the mummy beat you. Game Over!")
        sys.exit()
    elif player_wins == 3:
        print("proceed to next room/game")


game_1()