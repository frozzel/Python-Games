PI = 3.14159
GOOGLE_URL = "https://www.google.com"


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        print(i, number)
        if number % i == 0:
            print("Not prime")
            return False
    return True

print(is_prime(10))