import validation

valid_pass = True

while valid_pass:
    password_user = input("""
    enter password
    requirements:
    Validation :
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.\n""")
    valid_pass = validation.valid_pass(password_user)

print(f"correct password entered")