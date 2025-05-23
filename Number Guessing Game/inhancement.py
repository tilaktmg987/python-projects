# Allowing the user to specify the minimum and maximum values for the number
# range before the game starts. This gives the player more control over the
# difficulty level. 

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

while True:
    user=int(input(f"enter any number between ({min_number},{max_number}): "))
    attempt+=1
    if(user>max_number or user<min_number):
        print(f"please enter number between ({min_number},{max_number})")
    elif user>computer:
        print("To High.Try again")
    elif user<computer:
        print("To Low.Try again")
    elif user==computer:
        print(f"Congrulation,You found the number at {attempt} attempt:")
        break
    else:
        print("invalid number")