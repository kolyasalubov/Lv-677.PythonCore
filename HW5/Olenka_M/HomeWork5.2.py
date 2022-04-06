user_login = input("Please, enter your user_login: ")

while user_login != "First":
    user_login = input(f"Sorry user_login '{user_login}' is not found. Please, try again: ")
else:
    print(f"Great! You entered right login '{user_login}'. Please, do the next step")
