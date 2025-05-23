import random

computer=random.randint(1,100)
attempt=0

while True:
    user=int(input("enter any number between (1,100): "))
    attempt+=1
    if(user>100 or user<1):
        print("please enter number between (1,100)")
    elif user>computer:
        print("To High.Try again")
    elif user<computer:
        print("To Low.Try again")
    elif user==computer:
        print(f"Congrulation,You found the number at {attempt} attempt:")
        break
    else:
        print("invalid number")