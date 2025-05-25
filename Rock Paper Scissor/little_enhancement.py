import random

C_point = 0
U_point = 0

print("🎮 GAME: BEST OF THREE 🎮\n")

for i in range(1, 4):
    print(f"Round {i}:")
    computer = random.choice(["r", "p", "s"])
    user = input("Rock, paper, or scissors? (r/p/s or q to quit): ").lower()

    if user == "q":
        print("\nThanks for playing! 👋")
        break

    if computer == "r" and user == "r":
        print("You chose 🪨")
        print("Computer chose 🪨")
        print("Result: Draw!\n")
    elif computer == "p" and user == "r":
        print("You chose 🪨")
        print("Computer chose 📄")
        print("Result: You lose!\n")
        C_point += 1
    elif computer == "s" and user == "r":
        print("You chose 🪨")
        print("Computer chose ✂️")
        print("Result: You win!\n")
        U_point += 1
    elif computer == "r" and user == "p":
        print("You chose 📄")
        print("Computer chose 🪨")
        print("Result: You win!\n")
        U_point += 1
    elif computer == "p" and user == "p":
        print("You chose 📄")
        print("Computer chose 📄")
        print("Result: Draw!\n")
    elif computer == "s" and user == "p":
        print("You chose 📄")
        print("Computer chose ✂️")
        print("Result: You lose!\n")
        C_point += 1
    elif computer == "r" and user == "s":
        print("You chose ✂️")
        print("Computer chose 🪨")
        print("Result: You lose!\n")
        C_point += 1
    elif computer == "p" and user == "s":
        print("You chose ✂️")
        print("Computer chose 📄")
        print("Result: You win!\n")
        U_point += 1
    elif computer == "s" and user == "s":
        print("You chose ✂️")
        print("Computer chose ✂️")
        print("Result: Draw!\n")
    else:
        print("❌ Invalid input. Please choose r, p, or s.\n")

print("\n🏁 FINAL RESULT - BEST OF 3 🏁\n")
print(f"User Score: {U_point}")
print(f"Computer Score: {C_point}\n")

if U_point == C_point:
    print("🤝 It's a draw!")
elif U_point > C_point:
    print("🎉 You are the overall winner!")
else:
    print("💻 Computer is the overall winner!")