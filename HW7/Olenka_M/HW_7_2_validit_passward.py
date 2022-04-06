def check_validity_password(password: str) -> str:
    """
    Function check whether password is relevant the next 
    requirements:
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
    """
    import re
    
    if not 6 <= len(password) <= 16:
        print("Password lenght must be not less than 6 and not more than 16")
    elif not re.findall("[$#@]", password):
        print("For validity password, please, create password using at least one of the next symbals $, #, @")
    elif not re.findall("[0-9]", password):
        print("For validity password, please, create password using at least one of the digit 0-9")
    elif not re.findall("[A-Z]", password):
        print("For validity password, please, create password using at least one capital letter A-Z")
    elif not re.findall("[a-z]", password):
        print("For validity password, please, create password using at least one normal letter a-z")
    else:
        print("Great! Your password has maximum reliability")
        return 1

my_password = input("Please, create your password: ")

while check_validity_password(my_password) is None:
    my_password = input("Please, create your password: ")
