import random

roller=-1   #this is to know no of times you have roll 

while(True):
    user=input("Roll the dice?(y/n): ")
    roller+=1   #in each loop it is increase by 1 
    if(user=="n" or user=="N"):
        print("Thanks for playing")
        print(f"You have rolled {roller} times") #here that increased number will be print after the program is terminated
        break
    elif(user=="y" or user=="Y"):
        print(f"({random.randint(1,6)},{random.randint(1,6)})")
    else:
        print("invalid choice!")

# Modifing the program so the user can specify how many dice they want to roll. 

# user1=int(input("enter the number of times you want to roll the dice: "))

# for i in range(1,user1+1):
#     user=input("Roll the dice?(y): ")
#     if(user=="y" or user=="Y"):
#         print(f"({random.randint(1,6)},{random.randint(1,6)})")
#     else:
#         print("invalid choice!")
# print("Thanks for playing")
