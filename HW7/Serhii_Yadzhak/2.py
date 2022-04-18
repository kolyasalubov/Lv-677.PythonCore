import re
password = input('Enter your password: ')
x = True
while x:
    if 6 >= len(password) or len(password) >= 16:
        break
    elif not re.search('[a-z]', password):
        break
    elif not re.search('[A-Z]', password):
        break
    elif not re.search('[0-9]', password):
        break
    elif not re.search('[$,#,@]', password):
        break
    else:
        print('Password correct')
        x = False
        break
if x:
    print('Password is incorrect')