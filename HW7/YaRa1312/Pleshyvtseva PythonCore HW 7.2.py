#7.2

import re

user_password = input("Enter your password to check its validity: ")

def checking_password_validity(user_password):
    """
    The function checks the validity of password printed by user.
    A valid password should have 6-16 characters and contain at least 1 digit,
    at least 1 capital letter, at least 1 small letter, at least 1 character from $, #, @
    """
    red_flag = True
    while red_flag:
        if len(user_password)<6 or len(user_password)>16:
            break
        elif not re.search("[a-z]", user_password):
            break
        elif not re.search("[0-9]", user_password):
            break
        elif not re.search("[A-Z]", user_password):
            break
        elif not re.search("[$#@]", user_password):
            break
        elif re.search("\s", user_password):
            break
        else:
            return f"{user_password} is a valid password"
    if red_flag:
        return f"{user_password} is an invalid password"

print(checking_password_validity(user_password))
