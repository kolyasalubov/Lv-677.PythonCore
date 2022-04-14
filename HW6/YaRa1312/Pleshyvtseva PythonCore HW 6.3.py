# 6.3

def characters_number_calculation(user_string):
    '''
    The function calculates characters in the string
    entered by a user and give the quality of usage of each
    character in a dict where {character: quality of usage}
    '''
    result = {}
    for i in user_string:
        if i in result:
            continue
        else:
            result.update({str(i): user_string.count(i)})
    return result

user_string = input("Enter a string to calculate the number of its characters: ")
print(characters_number_calculation(user_string))
