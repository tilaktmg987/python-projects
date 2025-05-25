import random

while True:
    computer = random.choice(["r", "p", "s"])
    user = input("Rock, paper, or scissors? (r/p/s or q to quit): ").lower()

    if user == "q":
        print("Thanks for playing! 👋")
        break

    if computer == "r" and user == "r":
        print("You chose 🪨")
        print("Computer chose 🪨")
        print("Draw!")
    elif computer == "p" and user == "r":
        print("You chose 🪨")
        print("Computer chose 📄")
        print("You lose!")
    elif computer == "s" and user == "r":
        print("You chose 🪨")
        print("Computer chose ✂️")
        print("You win!")
    elif computer == "r" and user == "p":
        print("You chose 📄")
        print("Computer chose 🪨")
        print("You win!")
    elif computer == "p" and user == "p":
        print("You chose 📄")
        print("Computer chose 📄")
        print("Draw!")
    elif computer == "s" and user == "p":
        print("You chose 📄")
        print("Computer chose ✂️")
        print("You lose!")
    elif computer == "r" and user == "s":
        print("You chose ✂️")
        print("Computer chose 🪨")
        print("You lose!")
    elif computer == "p" and user == "s":
        print("You chose ✂️")
        print("Computer chose 📄")
        print("You win!")
    elif computer == "s" and user == "s":
        print("You chose ✂️")
        print("Computer chose ✂️")
        print("Draw!")
    else:
        print("Invalid input. Please choose r, p, or s.")
