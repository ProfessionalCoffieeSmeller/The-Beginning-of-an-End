import time
print("Welcome to my computer quiz!")

playing = input("Would you like to start the game? ")
if playing.lower() != "yes":
    quit()
#ideally what we can also do is state 
#if playing = no then quit. 
#this would ideally allow for a higher margin of error. 
score = 0
start_time = time.time()
print("Let's play!")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else: 
    print("Incorrect! Please try one more time!")
    second_answer = input("Try again: What does CPU stand for? ")
    if second_answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Next question!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score = score + 1
else: 
    print("Incorrect! Please try one more time!")
    second_answer = input("Try again: What does GPU stand for? ")
    if second_answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Next question!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else: 
    print("Incorrect! Please try one more time!")
    second_answer = input("Try again: What does RAM stand for? ")
    if second_answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Next question!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score = score + 1
else: 
    print("Incorrect! Please try one more time!")
    second_answer = input("Try again: What does PSU stand for? ")
    if second_answer.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Next question!")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score = score + 1
else: 
    print("Incorrect! Please try one more time!")
    second_answer = input("Try again: What does HDD stand for? ")
    if second_answer.lower() == "hard disk drive":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Next question!")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score = score + 1
else: 
    print("Incorrect! Please try one more time!")
    second_answer = input("Try again: What does SSD stand for? ")
    if second_answer.lower() == "solid state drive":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Next question!")
    
end_time = time.time()
duration = end_time - start_time

print("You got " + str(score) + " questions correct")
percentage = (score/6)*100
final = round(percentage, 1)
print("Congratulations! Your final score is " + str(final) + " %.")
print(f"You completed the quiz in {duration:.1f} seconds.")
if score == 0:
    print("You got 0 questions correct.")
    print("Good Luck next time!")