import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    
    return True

def validate_email(email):
    if not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    return True

def validate_website(website):
    # if not re.search(r"^(http|https)://", website):
    #     return False
    # if not re.search(r"\.", website):
    #     return False
    # if not re.search(r"((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+(\.[a-z]{2,}){1,3}(#?\/?[a-zA-Z0-9#]+)*\/?(\?[a-zA-Z0-9-_]+=[a-zA-Z0-9-%]+&?)?$/", website):
    #     return False
    if not re.search(r"^((https|http)://)?(www.)?[a-z0-9]+\.+[a-z0-9]", website):
        return False
    return True