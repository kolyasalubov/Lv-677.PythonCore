# # Var 1 - Спроби вводу логіну необмежені.
print('Write correct Username to continue ->')
count = 0
while count < 1:
    user_nume = input('Enter Username:\n')
    if user_nume=='First':
        print(f"Hello, you are the {user_nume}!")
        break
    else:
        print('Login is not correct! Pleace try again...')
        count-=1
# # Var 2 - Обмеження - тільки логін First є корректним.
print('Write correct Username to continue ->')
user_nume = input('Enter Username:\n')
while True:
    if user_nume == 'First':
        print(f"Hello, you are the {user_nume}!")
        break
    else:
        print('Login is not correct!')
        break
# Var 1 - 3 спроби  на введення корректного логіну.
print('Write correct Username to continue ->')
count = 0
while count < 3:
    user_nume = input('Enter Username:\n')
    if user_nume=='First':
        print(f"Hello, you are the {user_nume}!")
        break
    else:
        print('Login is not correct! Pleace try again...')
        count+=1