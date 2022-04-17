def list_animals(animals):
    list = ''

    num = 0
    for i in animals:
        num += 1
        list += str(num) + '. ' + i + '\n'
    return list


animals = ['dog', 'cat', 'elephant']

print(list_animals(animals))

