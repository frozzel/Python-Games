#FizzBuzz Algorithm Testing
# sum = 0

# for number in range(1, 101):
#     sum += number
 
# print(sum)  
total_fizz = 0
total_buzz = 0
total_fizzbuzz = 0

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        total_fizzbuzz += 1
        print("FizzBuzz")
    elif number % 3 == 0:
        total_fizz += 1
        print("Fizz")
    elif number % 5 == 0:
        total_buzz += 1
        print("Buzz")
    else:
        print(number)
        
print(f"Total Fizz: {total_fizz}")
print(f"Total Buzz: {total_buzz}")
print(f"Total FizzBuzz: {total_fizzbuzz}")