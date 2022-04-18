login_of_user = input('Enter your Login:')

while login_of_user != 'First':
    login_of_user = input('Error: Enter your Login:')

else:
    print('Welcome to your apps', login_of_user)
