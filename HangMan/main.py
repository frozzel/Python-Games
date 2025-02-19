from wonderwords import RandomWord
from bugs import hangman
import os

with open("hangman.txt") as file:
    content = file.read()
    print(F"\033[35m{content}\033[0m")

# generate a random word
def random_word():
    gen_word = RandomWord()
    word = gen_word.word()
    return word
chosen_word = random_word()

# print(chosen_word)
# create placeholder

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print("Word to guess: " + placeholder)

game_over = False
lives = 6
stage = 0

correct_guess = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    
    if guess in correct_guess:
        print("You already guessed that letter")
        continue
    os.system("clear")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_" 
    if guess not in chosen_word:
        print(f"{guess} is not in the word you lose a life")
        lives -= 1
        stage += 1  
    print(display)
    print(hangman[stage])
    print(f"Lives: {lives}")
    
    if lives == 0:
        print("You Lose!")
        print(f"The word was {chosen_word}")
        game_over = True
        with open("death.txt") as file:
            death = file.read()
            print(f"\033[35m{death}\033[0m")
    if display == chosen_word:
        print("You Win!")
        game_over = True

        
     
