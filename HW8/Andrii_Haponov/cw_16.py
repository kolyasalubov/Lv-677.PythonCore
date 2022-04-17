def list_animals(animals):
    l = ""
    count = 0
    for i in animals:
        l += str(count + 1) + '. ' + i + '\n'
        count += 1
    return l

# animals = ['dog', 'cat', 'elephant']
# print(list_animals(animals))
