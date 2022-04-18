def count_sheeps(sheep):
    sum = 0
    for value in sheep:
        if value == True:
            sum += 1
    return sum