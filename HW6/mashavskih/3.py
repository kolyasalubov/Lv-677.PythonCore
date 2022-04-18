def calc_numbers_characters(str):
    dict_of_characters = {}
    for character in str:
        dict_keys = dict_of_characters.keys()
        if character in dict_keys:
            dict_of_characters[character] += 1
        else:
            dict_of_characters[character] = 1
    return dict_of_characters
print(calc_numbers_characters(input("Write word or sentences: \n")))
