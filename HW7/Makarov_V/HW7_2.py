import re


def validation(password: str):
    """
    This function checks the validity of password
    which must contain:
    At least 1 lowercase and 1 uppercase letters
    At least 1 number [0-9] and 1 symbol [$#@]
    The minimum length must be 6 characters.
    Maximum length available is 16 characters.
    """
    validity = True
    if len(password) < 6 or len(password) > 16:
        validity = False
    elif not re.search("[a-z]", password):
        validity = False
    elif not re.search("[A-Z]", password):
        validity = False
    elif not re.search("[0-9]", password):
        validity = False
    elif not re.search("[@#$]", password):
        validity = False

    if validity:
        print("Your password is correct.")
    else:
        print("Your password does not meet the requirements")


print("Your password must contain at least 1 lowercase and 1 "
      "uppercase letter.\n"
      "As well as at least 1 number [0-9] and 1 symbol [$#@].\n"
      "The minimum length must be 6 characters.\n"
      "Maximum length available is 16 characters.")
password = str(input("Please put your password: "))
validation(password)
