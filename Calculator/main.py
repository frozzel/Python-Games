import logo

print(f"\033[35m{logo.logo}\033[0m")

def calculate(first_number, second_number, operation):
    """This function takes in two numbers and an operation and returns the result of the operation.
    """
    if operation == "+":
        total = first_number + second_number
        return f"\033[35m{first_number} + {second_number} = {total}"
    elif operation == "-":
        total = first_number - second_number
        return f"\033[35m{first_number} - {second_number} = {total}"
    elif operation == "*":
        total = first_number * second_number
        return f"\033[35m{first_number} * {second_number} = {total}"
    elif operation == "/":
        total = first_number / second_number
        return f"\033[35m{first_number} / {second_number} = {total}"
    else:
        return "\033[35mInvalid operation"

f_number = input("Enter the first number: ")
equation = input("Enter the operation you want to perform: '+ - * /' ")
s_number = input("Enter the second number: ")

result = calculate(int(f_number), int(s_number), equation)
print(result)