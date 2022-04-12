import re

def pass_validator(your_pass):
    """
    Validates if password has:
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
    """
    
    validate = True
    if len(your_pass) > 16 or len(your_pass) < 6:
        validate = False
    elif not re.findall("[a-z]", your_pass) and not re.findall("[A-Z]", your_pass):
        validate = False
    elif not re.findall("[1-9]", your_pass):
        validate = False
    elif not re.findall("[$, @, #]", your_pass):
        validate = False
    
    
    if validate:
        print("Your password is validated ! ")
    else:
        print("Your password is not validated ! ")
        
        
yourpass = str(input("Enter your password: "))

pass_validator(yourpass)