import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letter =  [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number_of_symbols = int(input(f"How many symbols would you like in your password? max: {len(symbols)}\n"))
number_of_numbers = int(input(f"How many numbers would you like in your password? max: {len(numbers)}\n"))
number_of_lowercase_letters = int(input(f"How many lowercase letters would you like in your password? max: {len(lowercase_letters)}\n"))
number_of_uppercase_letters = int(input(f"How many uppercase letters would you like in your password? max: {len(uppercase_letter)}\n"))

password = []

random_symbol = random.sample(symbols, number_of_symbols)
random_number = random.sample(numbers, number_of_numbers)
random_lowercase_letter = random.sample(lowercase_letters, number_of_lowercase_letters)
random_uppercase_letter = random.sample(uppercase_letter, number_of_uppercase_letters)

password.extend(random_symbol)
password.extend(random_number)
password.extend(random_lowercase_letter)
password.extend(random_uppercase_letter)

random.shuffle(password)
password = ''.join(password)
print(f'Your password is: {password}')