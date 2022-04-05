import re

print('* Password verification *')
user_password = ""

def check_validity(user_password):
    while True:
        user_password = input('Enter your password to check it is validity: ')
        if len(user_password) < 6 or len(user_password) > 16:
            print('Not valid! The password must consist of:\n - Minimum length 6 characters; \n - Maximum length 16 characters. \nTry again!')
            continue
        elif not re.search('[a-z]', user_password):
            print('Not valid! The password must consist of at least 1 letter between [a-z]. \nTry again!')
            continue
        elif not re.search('[A-Z]', user_password):
            print('Not valid! The password must consist of at least 1 letter between [A-Z]. \nTry again!')
            continue
        elif not re.search('[0-9]', user_password):
            print('Not valid! The password must consist of at least 1 number between [0-9]. \nTry again!')
            continue
        elif not re.search('[$#@]', user_password):
            print('Not valid! The password must consist of at least 1 character from [$#@]. \nTry again!')
            continue
        else:
            print(f'Your password - {user_password} - valid!')
            break
check_validity(user_password)