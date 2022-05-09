username = input("Enter your username: ")
while username:
    if username != "First":
        print("Wrong username\n")
        username = input("Enter your username again: ")
    else:
        print(f"Hello, {username}")
        break
input()