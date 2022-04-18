"""
    Write a script that checks the login that the user enters.
    If the login is "First", then greet the users.
    If the login is different, send an error message.
    (need to use loop while)
"""
##################################################################################################################
user_name = 1
while user_name == 1:
    name = input("Enter you login: ")
    if name == "First":
        print(f"Congratulations on entering the correct login: {name}")
        break
    else:
        print("It's not the right login, please enter a valid login")
