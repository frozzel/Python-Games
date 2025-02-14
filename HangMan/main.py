from wonderwords import RandomWord
from test import hangman
import os

with open("hangman.txt") as file:
    content = file.read()
    print(content)

# generate a random word
def random_word():
    gen_word = RandomWord()
    word = gen_word.word()
    return word
chosen_word = random_word()

print(chosen_word)
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
        lives -= 1
        stage += 1  
    print(display)
    print(hangman[stage])
    print(f"Lives: {lives}")
    
    if lives == 0:
        print("You Lose!")
        game_over = True
        with open("death.txt") as file:
            death = file.read()
            print(death)
    if display == chosen_word:
        print("You Win!")
        game_over = True

        
     
