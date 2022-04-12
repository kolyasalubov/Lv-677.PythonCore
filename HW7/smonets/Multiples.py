def solution(number):
    solution = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            solution += i
    return solution

solution(10)