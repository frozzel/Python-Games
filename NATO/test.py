import random
import pandas as pd

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_range = [n * 2 for n in range(1, 5)]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_uppercase_names = [name.upper() for name in names if len(name) > 5]

print(long_uppercase_names)
print(short_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

with open("file1.txt") as file1:
    file1_data = ((file1.read()).split("\n"))
    print(file1_data)
    
with open("file2.txt") as file2:
    file2_data = ((file2.read()).split("\n"))
    print(file2_data)
    
    
result = [int(n) for n in file1_data if n in file2_data]
print(result)

new_dict = {n: n * 2 for n in range(1, 5)}
print(new_dict)


new_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in new_names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score > 60}
print(passed_students)

pd_frame = pd.DataFrame(passed_students.items(), columns=["Student", "Score"])
print(pd_frame)

# pd_frame.to_json("students.json")

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data = pd.DataFrame(student_dict)
print(student_data)