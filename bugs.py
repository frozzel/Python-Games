# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You win!") # This line will never be printed because the loop stops at 19
            
# my_function()

# from random import randint

# dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# dice_num = randint(0, 5) # This will generate a number between 0 and 6 that is more than the length of the list
# print(dice_images[dice_num])

# year = int(input("Whats your year of birth? "))
# if year > 1980 and year <= 1994: # by adding the equal sign, the code will include 1994 as a millenial
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# elif year <= 1980 and year > 1965:
#     print("You are a Gen X.")
# else:
#     print("Boomer") 

# try: 
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You have entered an invalid input. Please enter a number. Example: 25")
#     age = int(input("How old are you? "))
    
# if age > 18:
#     print(f"You can drive at age {age}.")

# word_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page = int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
    
# print(odd_or_even(3)) # This will print "This is an odd number."
# print(odd_or_even(4)) # This will print "This is an even number."

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

            
fizz_buzz(100) # This will print FizzBuzz, Fizz, Buzz, or the number depending on the conditions met.