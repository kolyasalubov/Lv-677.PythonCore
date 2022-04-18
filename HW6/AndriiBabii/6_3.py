# Write a function that calculates 
# the number of characters included in a given string

# input: “hello”
# output: {“h”:1, “e”:1, “l”:2, “o”:1}



def number_of_character(input_str: str):
    result_dict = {}
    for i in input_str:
        result_dict[i] = input_str.count(i)
    return result_dict

