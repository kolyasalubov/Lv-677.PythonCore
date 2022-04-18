def solution(number):
    sum = 0
    for x in range(1,number):
        if x % 3 == 0:
            sum +=x
        elif x % 5 == 0:
            sum +=x
        elif x % 3 and x % 5 == 0:
            continue
    return sum