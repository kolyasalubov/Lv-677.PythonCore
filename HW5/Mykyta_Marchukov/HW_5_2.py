#Task2. Write a script that checks the login that the user enters. 
#If the login is "First", then greet the users. If the login is different, send an error message. 
#(need to use loop while)

while True:
    login = input('Enter login: ')
    if login == 'First':
        print(f'Hello, {login}.')
        break
    print('Login is invalid, please try again.')
