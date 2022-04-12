def num_char(my_str):
    """ calculates the number of characters in string """
    
    result = {}
    for i in my_str:
        result[i] = my_str.count(i)
    return result

my_str = input("Enter string to calculate char: ")
print(num_char(my_str))
