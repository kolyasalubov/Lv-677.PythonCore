def number_of_characters(text):
    dict = {}
    for letter in text:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict