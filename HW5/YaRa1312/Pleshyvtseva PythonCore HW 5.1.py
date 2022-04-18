# 5.1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_divisible_by_2 = []
numbers_divisible_by_3 = []
numbers_not_divisible_by_2_and_3 = []


for i in numbers:
    if i % 2 == 0:
        numbers_divisible_by_2.append(i)
    elif i % 3 == 0:
        numbers_divisible_by_3.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        numbers_not_divisible_by_2_and_3.append(i)

print(numbers_divisible_by_2)
print(numbers_divisible_by_3)
print(numbers_not_divisible_by_2_and_3)
