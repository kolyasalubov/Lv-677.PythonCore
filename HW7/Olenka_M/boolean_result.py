def bool_to_word(boolean):
    return "Yes" if boolean else "No" 

#Below is an interesting solution from codewars, that I added to my memory
def bool_to_word(bool):
    return ['No', 'Yes'][bool]