# Lv-677_Ivan_Vaulin
# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

user_name = input('Hello, please input your Log in:')
while user_name != 'First':
    user_name = input('Error: wrong username, please try one more time. Username:')
else:
    print('Greeting. Access granted!!!', user_name)