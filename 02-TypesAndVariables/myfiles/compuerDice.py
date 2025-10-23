import random
dice_roll = random.randint(1, 6)
user=int(input('Guess the dice roll (1-6): '))
print(f"You've guessed correctly: {user==dice_roll}")