def number_of_charachters(your_string):
    """
    Function creates dictionary where key is an element of a string
    and value counts how many times does an element included to a string 
    """
    return {x: your_string.count(x) for x in your_string}
