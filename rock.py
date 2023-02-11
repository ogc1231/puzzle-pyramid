import random

hand = ("rock", "paper", "scissors")

mummy_hand = random.choice(hand)
player_hand = input("Choose a hand (rock, paper or scissors) ")


print(f"You chose {player_hand}! ")
print(f"The Mummy chose {mummy_hand}!")