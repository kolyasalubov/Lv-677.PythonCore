# Task1. In the range from 1 to 10 determine 
# even_numbers that are divisible by 2,
# odd_numbers, which are divisible by 3,
# numbers_that_are_not_divisible_by_2_and_3.

# Задание 1. В пределах от 1 до 10 определите
# четные числа, которые делятся на 2,
# нечетные числа, которые делятся на 3,
# числа, которые не делятся на 2 и 3.

# even_numbers = []
# for i in range(1,11):
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)

# odd_numbers = []
# for i in range (1, 11):
#     if i % 2 != 0 and i % 3 == 0:
#         odd_numbers.append(i)
# print(odd_numbers)

# numbers_that_are_not_divisible_by_2_and_3 = []
# for i in range(1,11):
#     if i % 2 != 0 and i % 3 != 0:
#         numbers_that_are_not_divisible_by_2_and_3.append(i)
# print(numbers_that_are_not_divisible_by_2_and_3)

# even_numbers = []
# odd_numbers = []
# numbers_that_are_not_divisible_by_2_and_3 = []
# for i in range (1, 11):
#     if i % 2 == 0:
#         even_numbers.append(i)
#     elif i % 2 != 0 and i % 3 == 0:
#         odd_numbers.append(i)
#     else:
#         numbers_that_are_not_divisible_by_2_and_3.append(i)
# print(even_numbers, odd_numbers, numbers_that_are_not_divisible_by_2_and_3)

even_numbers = [i for i in range(1,11) if i%2 == 0]
odd_numbers = [i for i in range(1,11) if i % 2 != 0 and i % 3 == 0]
numbers_that_are_not_divisible_by_2_and_3 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]

print(even_numbers, odd_numbers, numbers_that_are_not_divisible_by_2_and_3)



    

