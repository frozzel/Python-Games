from wonderwords import RandomWord

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
lives = 6
display = ""

while lives > 0:
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
        
        else:
            display += "_"
    print(display)
     
