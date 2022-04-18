write_first_login = input("Write your login: ")

while write_first_login != "First":
     print("Erro. Write the correct login")
     break
else:
     print(f"Congratulations! Your login is: {write_first_login}")

