import re

def pass_funk(password):
     while True:
          if not 6 <= len(password) <= 16:
               password = input("Your password is too short or so long! ")
          elif not re.search('[a-z]', password):
               password = input("Password don't have any letters.Add letter ")
          elif not re.search('[A-Z]', password):
               password = input("Password don't have any capital letters.Try again ")
          elif not re.search('[0-9]', password):
               password = input("Password don't have any number.Try again ")
          elif not re.search('[$#@]', password):
               password = input("Password don't have any symbols.Try again ")
          else:
               print("Good work! You have strong password!")
               break
     return 

password = input("Please, type password: ")

pass_funk(password)


