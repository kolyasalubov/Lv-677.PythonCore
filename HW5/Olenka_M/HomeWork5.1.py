# print("\n-------------------------------------Version 0-----------------------------------\n")

divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_and_3 = []

for number in range(1,11):
    if number % 2 == 0:
        divisible_by_2.append(number)
    elif number % 3 == 0:
        divisible_by_3.append(number)
    else:
        not_divisible_by_2_and_3.append(number)

print(f'Numbers, that are divisible by 2: {divisible_by_2}.\nNumbers, that are divisible by 3: {divisible_by_3}.\n\
Rest of numbers are: {not_divisible_by_2_and_3}.')

# print("\n------------------------------------Version 1------------------------------------\n")

# divisible_by_2 = [number for number in range(1,11) if number % 2 == 0]
# divisible_by_3 = [number for number in range(1,11) if number % 3 == 0]
# not_divisible_by_2_and_3 = [number for number in range(1,11) if number % 2 != 0 and number % 3 != 0]

# print(f'Numbers, that are divisible by 2: {divisible_by_2}.\nNumbers, that are divisible by 3: {divisible_by_3}.\n\
# Rest of numbers are: {not_divisible_by_2_and_3}.')

# print("\n------------------------------------Version 2----------------------------------\n")

# divisible_by_2 = [number for number in range(1,11) if number % 2 == 0]
# divisible_by_3 = [number for number in range(1,11) if number % 3 == 0]
# not_divisible_by_2_and_3 = [number for number in range(1,11) if number not in divisible_by_2 and\
# number not in divisible_by_3]

# print(f'Numbers, that are divisible by 2: {divisible_by_2}.\nNumbers, that are divisible by 3: {divisible_by_3}.\n\
# Rest of numbers are: {not_divisible_by_2_and_3}.')
