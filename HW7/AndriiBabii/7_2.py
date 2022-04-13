# Task1.
# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re


def checking_pass(user_pass: str):
    if len(user_pass) < 6: return "Minimum length 6 characters"
    elif len(user_pass) > 16: return "Maximum length 16 characters"
    elif re.findall("[a-z]", user_pass) == []: return "At least 1 letter between [a-z]"
    elif re.findall("[A-Z]", user_pass) == []: return "At least 1 letter between [A-Z]"
    elif re.findall("[0-9]", user_pass) == []: return "At least 1 number between [1-9]"
    elif re.findall("[!,@,#,$,%,^,&,*]", user_pass) == []: return "At least 1 character from [$#@]"
    else: return True


print("""
# Enter password, password must contain:
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
""")
while True:
    validation = checking_pass(input("Enter password: "))
    if validation == True:
        print("Password is valid")
        break
    else: print("Try again...", validation)

