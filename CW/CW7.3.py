def solution(number):
    suma = 0
    for i in range(2,number):
        if i < 0:
            return 0
        elif i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma