import random

hand = ("rock", "paper", "scissors")

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
elif player_hand == "scissors" and mummy_hand == "paper":
    print("You win!")
elif player_hand == "paper" and mummy_hand == "rock":
    print("You win!")
else:
    print("You lose!")