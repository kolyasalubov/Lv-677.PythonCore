def list_animals(animals):
    my_list = ''
    for i in range(len(animals)):
        my_list += str(i + 1) + '. ' + animals[i] + '\n'
    return my_list