programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# Retrieving items from dictionary.

# print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Variable"] = "A placeholder for data."

# editing items in dictionary.

programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary["Bug"])


# Loop through a dictionary.

# for key in programming_dictionary:
#     # print(key)
#     print(key+":", programming_dictionary[key])


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for grade in student_scores:
    if student_scores[grade] >= 91:
        student_grades[grade] = "Outstanding"
    elif student_scores[grade] >= 81:
        student_grades[grade] = "Exceeds Expectations"
    elif student_scores[grade] >= 71:
        student_grades[grade] = "Acceptable"
    else:
        student_grades[grade] = "Fail"
        
# print(student_grades)

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# print(travel_log["France"][1])
# print(travel_log["Germany"]["cities_visited"][0])
# print(travel_log["Germany"]["total_visits"])

nested_list = ["a", "b",  ["c", "d"]]
# print(nested_list[2][1])