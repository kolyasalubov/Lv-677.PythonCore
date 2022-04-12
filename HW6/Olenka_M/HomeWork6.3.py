# def calculate_characters(some_string: str) -> dict:
#     """ 
#     Function calculates the number of characters included in a given string 
#     and returns dict where keys are unique characters of given string
#     and values are number of relevant character of given string
#     """
#     return {item: some_string.count(item) for item in some_string}

def calculate_characters(some_string: str) -> dict:
    """ 
    Function calculates the number of characters included in a given string 
    and returns dict where keys are unique characters of given string
    and values are number of relevant character of given string
    """
    result = {}
    for item in some_string:
        if item in result:
            continue
        else:
           result[item] = some_string.count(item)
    return result



# calculate_characters("gfvgcvxdx kjhjv 1n43!")
print(calculate_characters("gfvgcvxdx kjhjv 1n43!"))
