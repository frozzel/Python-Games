def format_name(f_name, l_name):
    """This function takes in a first name and a last name and returns a formatted full name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("dennis", "mugambi"))

def is_leap_year(year):
    """This function checks if a year is a leap year or not.
    A leap year is a year that is divisible by 4 but not by 100 unless it is divisible
    by 400. For example 2000 is a leap year but 2100 is not a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(is_leap_year(2020))
