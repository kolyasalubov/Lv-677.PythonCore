########## 1
#Grasshopper - Summation
# def summation(num):
#     for i in range(num):
#         num += i
#     return num


########## 2
#Fix the loop!
def list_animals(animals):
    list = ''
    for i in range(animals):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list
animalsi = ['asdsaf', 'asdas', 'afaf']
print(list_animals(animalsi))


########## 3
