#https://www.codewars.com/kata/fix-the-loop/train/python

def list_animals(animals):
    list = ''
    i = 0
    for item in animals:
        i += 1
        list += f"{i}. {item}\n"
    return list

