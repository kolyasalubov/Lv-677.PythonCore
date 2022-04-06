# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


# Напишите программу на Python для проверки правильности пароля (вводимого пользователями).

# Проверка :
# Минимум 1 буква между [a-z] и 1 буква между [A-Z].
# По крайней мере 1 число между [0-9].
# Хотя бы 1 символ из [$#@].
# Минимальная длина 6 символов.
# Максимальная длина 16 символов.

import re

login = input("Enter login : ")  

while True:
    pattern = login
    v_1 = re.findall("[$, #, @]", pattern)
    v_2 = re.findall("[0-9]", pattern)
    v_3 = re.findall("[a-z]", pattern)
    v_4 = re.findall("[A-Z]", pattern)
    if len(login) >= 6 and len(login) <= 16\
        and len(v_1) >= 1 and len(v_2) >= 1\
        and len(v_3) >= 1 and len(v_4) >= 1:
        print(f"Hello {login}!")
        break
    else:
        print("Enter correct login!")
        login = input("Enter login : ")
            






        