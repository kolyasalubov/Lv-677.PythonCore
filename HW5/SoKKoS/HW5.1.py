number_1_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_2 = []
number_3 = []
number_not_23 = []

for i in number_1_10:
    if i % 2 == 0:
        number_2.append(i)
    elif i % 3 == 0:
        number_3.append(i)
    else:
        number_not_23.append(i)


print(number_2)
print(number_3)
print(number_not_23)