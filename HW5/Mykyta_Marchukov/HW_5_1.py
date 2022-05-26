#Task1. In the range from 1 to 10 determine 
#even numbers that are divisible by 2,
#odd numbers, which are divisible by 3,
#numbers that are not divisible by 2 and 3.

div_list_2 = []
div_list_3 = []
div_list_not_2_3 = []

for i in range(1,11):
    if i % 2 == 0:
        div_list_2.append(i)
    elif i % 3 == 0:
        div_list_3.append(i)
    else:
        div_list_not_2_3.append(i)

print(f'Numbers divisible by 2: {div_list_2}')
print(f'Numbers divisible by 3: {div_list_3}')
print(f'Not divisible by 2 and 3: {div_list_not_2_3}')
