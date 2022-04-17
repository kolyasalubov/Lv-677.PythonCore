def double_char(s):
    new_list = ""
    for i in s:
        new_list += i + i
    return new_list


str_double = input('enter the string - ')

print(double_char(str_double))

