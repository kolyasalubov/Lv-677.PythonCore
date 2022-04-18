# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

# Задача2. Напишите скрипт, проверяющий логин, который вводит пользователь.
# Если логин «Первый», то приветствуйте пользователей. Если логин другой, отправьте сообщение об ошибке.
# (необходимо использовать цикл while)
       

login = input("Enter login : ")  
while login != "First":
    print("Error")
    login = input("Enter login : ")
else:
    print("Hello First!")


