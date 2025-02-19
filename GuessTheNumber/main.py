import logo
import random

# Functions for the game

def check_answer(guess, number, attempts):
    """Check answer against guess. Return the number of attempts remaining."""
    if guess == number:
        print(f"🌟🌟 You got it! The answer was {number}. 🌟🌟")
        return 100
    elif guess > number:
        print("\033[35mToo high.\033[0m")
    else:
        print("\033[35mToo low.\033[0m")
    return attempts - 1

def set_difficulty():
    """Set the difficulty level for the game."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid input. Please try again.")
        return 0
# start the game
print(f"\033[35m{logo.logo}\033[0m")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = set_difficulty()

attempts = difficulty
    
number = random.randint(1, 100)

# logic for the game

while attempts > 0:
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, number, attempts)
    if attempts == 0:
        print(f"💀💀 You've run out of guesses. The number was {number}. 💀💀")
        break
    if attempts == 100:
        break
    print("Guess again.")
    print(f"You have \033[35m{attempts}\033[0m attempts remaining to guess the number.")
