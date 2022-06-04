########## 1
#Grasshopper - Summation
# def summation(num):
#     for i in range(num):
#         num += i
#     return num


########## 2
#Fix the loop!
# def list_animals(animals):
#     list = ''
#     for i in range(len(animals)):
#         list += str(i + 1) + '. ' + animals[i] + '\n'
#     return list


########## 3
#Double Char
def double_char(s):
    double_string = ''
    for i in s:
        double_string += i*2
    return double_string
