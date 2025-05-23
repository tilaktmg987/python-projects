# Implementing a feature that limits the number of guesses a player can make. If
# the player runs out of attempts, the game should end, and the correct number
# should be revealed. 


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
limit=2
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
        guess=False
        break
    else:
        print("Invalid number")
        print(f"Chances left: {limit}")

if guess:
    print("No more chances available. Better luck next time!")
    print(f"Number was:{computer}")