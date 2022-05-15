# Task1.
# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z] - done
# At least 1 number between [0-9] - done.
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters

# CODE

import re

password_input = input("Please input password: ")

def password_validate(password_input):

    warning = True

    while warning:

        if len(password_input)>6 or len(password_input)<16:
            break
        elif not re.search("[a-z]", password_input):
            break
        elif not re.search("[0-9]", password_input):
            break
        elif not re.search("[A-Z]", password_input):
            break
        elif not re.search("[$#@]", password_input):
            break
        elif not re.search("\s", password_input):
            break
        else:
            return f"{password_input} is valid password"
            warning = False
            break
        
    if warning:
            return f"{password_input} is invalid password. Please try again."

print(password_validate(password_input))
