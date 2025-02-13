my_name = "Dennis"
print("Hello, " + my_name + "!")

# This variable will be used to count the number of times anyone tweets the word persnickety
persnickety_count = 4.5684846

# This code will calculate the likelihood that it will rain tomorrow
# complicated_rain_calculation_for_tomorrow()

# useful_value = old_sloppy_code()
# useful_value = new_clean_code()

# from Mary Shelley's Frankenstein
# print(f"{my_name}, there is something at work in my soul, which I do not understand. " + str(persnickety_count + 4))
# print(my_name[0])
# print(123+456)
# print(int("123456")+ 6)
# print(int(3*(3 + 3)/3 - 3))
# print(round(persnickety_count, 4))

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi > 18.5 and bmi <= 25:
    print("normal weight")
if bmi < 18.5:
    print("underweight")
elif bmi > 25:
    print("overweight")

print(bmi)
