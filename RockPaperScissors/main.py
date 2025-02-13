import random
import rps

print(rps.paper)
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)
if user_choice == "0":
    print(rps.rock)
    if computer_choice == 0:
        print("Computer chose: ")
        print(rps.rock)
        print("It's a draw")
    elif computer_choice == 1:
        print("Computer chose: ")
        print(rps.paper)
        print("You lose")
    else:
        print("Computer chose: ")
        print(rps.scissors)
        print("You win")
elif user_choice == "1":
    print(rps.paper)
    if computer_choice == 0:
        print("Computer chose: ")
        print(rps.rock)
        print("You win")
    elif computer_choice == 1:
        print("Computer chose: ")
        print(rps.paper)
        print("It's a draw")
    else:
        print("Computer chose: ")
        print(rps.scissors)
        print("You lose")
elif user_choice == "2":
    print(rps.scissors)
    if computer_choice == 0:
        print("Computer chose: ")
        print(rps.rock)
        print("You lose")
    elif computer_choice == 1:
        print("Computer chose: ")
        print(rps.paper)
        print("You win")
    else:
        print("Computer chose: ")
        print(rps.scissors)
        print("It's a draw")
else:
    print("Please enter a valid number")