import re

def valid_pass(password_user):
    print(password_user)
    if re.match('((?=.*[a-z])(?=.*[$#@])(?=.*[A-Z]).{6})', password_user) and len(password_user) <= 16:
        return False
    else:
        return True