import random

hand = ("rock", "paper", "scissors")

player_hand = None
mummy_hand = random.choice(hand)

while player_hand not in hand:
    player_hand = input("Choose a hand (rock, paper or scissors): ").lower()

print(f"You chose {player_hand}! ")
print(f"The Mummy chose {mummy_hand}!")