import random
import time
start_time = time.time()
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0, next time")
        quit()
else:
    print("please type a number next time. ")
    quit()
random_number = random.randint(0, top_of_range)

attempts = 0

while True: 
    attempts += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please print a number next time!")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > top_of_range:
        print("Enter a smaller Number!")
    else:
        print("Enter a larger Number!")

end_time = time.time()
duration = end_time - start_time
print(f"You completed the game in {duration:.1f} seconds.")
print("It took you", attempts, "attempts")