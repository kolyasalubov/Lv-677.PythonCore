def solution(number):
    summ_nuvm = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            summ_nuvm += i
        else:
            continue
    return summ_nuvm
    # return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
# print(solution(10))