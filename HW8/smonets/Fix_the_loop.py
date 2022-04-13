def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    print(list)
    
animals = [ 'dog', 'cat', 'elephant' ]

list_animals(animals)