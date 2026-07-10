import random

def play_hangman():
    words = ["python", "blockchain", "developer", "coding", "algorithm"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        display = "".join([char if char in guessed_letters else "_" for char in word])
        print(f"\nWord: {display}")
        
        if "_" not in display:
            print("Congratulations, you won!")
            return
            
        guess = input(f"Attempts left: {attempts}. Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Wrong!")
            
    print(f"Game over! The word was: {word}")

play_hangman()