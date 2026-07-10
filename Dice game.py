import random

def roll_dice():
    input("Press Enter to roll the dice...")
    result = random.randint(1, 6)
    print(f"You rolled a: {result}")

roll_dice()
