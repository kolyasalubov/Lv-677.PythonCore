#https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

def count_sheeps(sheep):
    how_many = 0
    for i in range(len(sheep)):
        if sheep[i] == True: how_many += 1
    return how_many

#def count_sheeps(sheep):
#    return sheep.count(True)
