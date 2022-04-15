def list_animals(animals: list) -> str:
    list = ''
    for i in range(len(animals)):
        list += str(i+1) + '. ' + animals[i] + '\n'
    return list


# The version below is worse, because someone can pass list with duplicates in function, and we will get bad numeration
def list_animals(animals: list) -> str:
    list = ''
    for pet in animals:
        list += str(animals.index(pet) + 1) + '. ' + pet + '\n'
    return list


#I copied the version below from codewars for bettter remember it
def list_animals(animals: list) -> str:
    return ''.join(f'{i}. {x}\n' for (i, x) in enumerate(animals, 1))
