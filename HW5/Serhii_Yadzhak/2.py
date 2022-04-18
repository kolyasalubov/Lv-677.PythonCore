login = input('Enter login: ')
while login != 'First':
    print('Access denied')
    login = input('Enter login again: ')
else: 
        print('Access granted')