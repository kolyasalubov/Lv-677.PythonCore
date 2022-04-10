# import re
# pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
# password = input("Enter string to test: ")
# result = re.findall(pattern, password)
# if (result):
#     print("Valid password")
# else:
#     print("Password not valid")

# import re
# password = input("Enter your password: ")
# if re.fullmatch(r'[A-Za-z0-9$#@]{6,16}', password):
#     print ("Welcome! Your password is correct")
# else:
print ('Please try again.\n',
    'At least 1 letter between [a-z] and 1 letter between [A-Z].\n',
    'At least 1 number between [0-9].\n',
    'At least 1 character from [$#@].\n',
    'Minimum length 6 characters.\n',
    'Maximum length 16 characters.')