divided_by_2 = []
divided_by_3 = []
not_divided_by_2_3 = []
for value in range(1,11):
    if value%2==0:
        divided_by_2.append(value)
    elif value%3==0:
        divided_by_3.append(value)
    else:
        not_divided_by_2_3.append(value)


print("Even numbers that are divisible by 2: ", divided_by_2)
print("Even numbers that are divisible by 3: ", divided_by_3)
print("Numbers that are not divisible by 2 and 3: ", not_divided_by_2_3)


# Task1. 
# In the range from 1 to 10 determine:
# *even numbers that are divisible by 2,
# *odd numbers, which are divisible by 3,
# *numbers that are not divisible by 2 and 3.