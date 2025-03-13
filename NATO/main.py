student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        # print(row.score)
        pass
        
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

with open("nato_phonetic_alphabet.csv") as file:
    data = file.readlines()
    # print(data)

phonetic_dict = {row.split(",")[0]: row.split(",")[1].strip() for row in data}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

game_is_on = True
while game_is_on:
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet please")
    else:
        print(phonetic_code)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "n":
            print("Thanks for playing!")
            game_is_on = False
        else:
            continue
    # finally:
    #     print("Game over")