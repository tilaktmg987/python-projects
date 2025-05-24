# Add a feature that keeps track of the fewest attempts it took to guess the
# number correctly. The program should display this "best score" at the end of
# each game. 


import random

while True:
    min_number=int(input("enter minimun number: "))
    max_number=int(input("enter maximum number: "))

    if(min_number>=max_number):
        print(f"sorry {min_number} should be smaller than {max_number}")
    else:
        break

computer=random.randint(min_number,max_number)
attempt=0
limit=50
guess=True


for i in range(1,limit+1):
    user=int(input(f"enter any number between ({min_number},{max_number}): "))
    attempt+=1
    limit-=1
    if(user>max_number or user<min_number):
        print(f"please enter number between ({min_number},{max_number})")
        print(f"Chances left: {limit}")
    elif user>computer:
        print("To High.Try again")
        print(f"Chances left: {limit}")
    elif user<computer:
        print("To Low.Try again")
        print(f"Chances left: {limit}")
    elif user==computer:
        print(f"Congrulation,You found the number at {attempt} attempt:")


        with open("best-score.txt") as f:
            best_score = f.read()  

            if(best_score==""):
                best_score= 100
            else:
                best_score=int (best_score)

            if attempt < best_score:
                with open("best-score.txt", "w") as f:
                    f.write(str(attempt))
                    print("🔥 New Best Score!")
        with open("best-score.txt") as f:
            best_score = f.read()
            print(f"Best-score to find in minimum attempt: {best_score}")
        guess=False
        break
    else:
        print("Invalid number")
        print(f"Chances left: {limit}")

if guess:
    print("No more chances available. Better luck next time!")
    print(f"Number was:{computer}")