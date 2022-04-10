import re

password = input("Enter your password: ")
if re.fullmatch(r'[A-Za-z0-9$#@]{6,16}', password):
    print ("Welcome! Your password is correct")
else:
    print ('Please try again. Your password should contain: \n',
        '1. At least 1 letter between [a-z] and 1 letter between [A-Z].\n',
        '2. At least 1 number between [0-9].\n',
        '3. At least 1 character from [$#@].\n',
        '4. Minimum length 6 characters.\n',
        '5. Maximum length 16 characters.')