import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    
    print("Welcome to Rock, Paper, Scissors! Type 'quit' to end.")
    
    while True:
        user = input("\nChoose (rock/paper/scissors): ").lower()
        if user == 'quit': break
        if user not in choices:
            print("Invalid input, try again.")
            continue
            
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        
        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1
        
        print(f"Score - You: {user_score} | Comp: {comp_score}")

play_rps()