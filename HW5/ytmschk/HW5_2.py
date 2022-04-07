dict_keys = ['First', 'Second', 'Third']
login_pass = dict.fromkeys(dict_keys, 0)

login = input('Enter your login: ')

while login not in login_pass:
    if login not in login_pass:
        print ('Please try again')
        print (input('Enter your login: '))
    print ("Nice to see you again!")
    break
