"""
    In the range from 1 to 10 determine
    * even numbers that are divisible by 2,
    * odd numbers, which are divisible by 3,
    * numbers that are not divisible by 2 and 3.

"""

##########################################################################

divisible_2_list = []
divisible_3_list = []
divisible_not_2_3 = []
for number in range(1, 11):
    if number % 2 == 0:
        divisible_2_list.append(number)
    elif number % 3 == 0:
        divisible_3_list.append(number)
    else:
        divisible_not_2_3.append(number)
    # elif number % 2 != 0 or i % 3 != 0:
    #     div_not_2_3.append(number)
print(f"Numbers divisible by 2:  {divisible_2_list}")
print(f"Numbers divisible by 3: {divisible_3_list}")
print(f"Non-divisible numbers: {divisible_not_2_3}")

