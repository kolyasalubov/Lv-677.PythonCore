# CodeWars Multiples of 3 and 5

def solution(number):
    count = 0
    for i in range(1, number):
        if i % 3 == 0:
            count += i
        elif i % 5 == 0:
            count += i
        elif i % 3 == 0 and i % 5 == 0:
            continue
    return count
