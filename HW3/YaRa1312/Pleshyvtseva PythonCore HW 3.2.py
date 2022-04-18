#3.2
user_integer = int(input("Enter a 4-digit natural number: "))
mult = 1
while user_integer > 0:
    digit = user_integer % 10
    mult = mult * digit
    user_integer = user_integer // 10
print("Product of all the digits: ", mult)

user_integer = int(input("Enter your 4-digit natural number again: "))
reversed_number = 0
while user_integer != 0:
  digit = user_integer % 10
  reversed_number = reversed_number * 10 + digit
  user_integer //= 10
print("Reversed number: ", reversed_number)

user_integer = int(input("Enter your 4-digit natural number one more time: "))
def getSortedNumber(user_integer):
    user_integer = str(user_integer)
    user_integer = ''.join(sorted(user_integer))
    user_integer = int(user_integer)
    return(user_integer)
print("Sorted number: ", getSortedNumber(user_integer))