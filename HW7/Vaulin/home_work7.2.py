# Task1.
# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

def check_pass(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*(\$|#|@)).{6,16}$')
    pass_search = pattern.search(password)
    while pass_search is not None:
        return True
    else:
        return False
# a = (input("asdasda: "))
# print(check_pass(a))