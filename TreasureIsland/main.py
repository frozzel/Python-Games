with open("treasure.txt") as file:
    contents = file.read()
    print(contents)
    print("\nWelcome to Treasure Island")
    print("Your mission is to find the treasure.")
    first_direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
    if first_direction.lower() == "left":
        second_direction = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
        if second_direction.lower() == "wait":
            third_direction = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
            if third_direction.lower() == "red":
                print("It's a room full of fire. 🔥🔥🔥 Game Over.")
            elif third_direction.lower() == "yellow":
                print("💰 You found the treasure! 💰 You Win!")
            elif third_direction.lower() == "blue":
                print("You enter a room of beasts. 🧌  Game Over.")
            else:
                print("You chose a door that doesn't exist. 👽 aliens kill you! Game Over.")
        else:
            print("You get attacked by an angry shark. 🦈 Game Over.")
    else:
        print("You fell into a hole. 🕳️  Game Over.")