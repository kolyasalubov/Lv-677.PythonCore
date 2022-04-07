devisible_by_two = []
devisible_by_three = []
not_devisible = []

for x in range(11):
    if x % 2 == 0:
        devisible_by_two.append(x)
    elif x % 3 == 0:
        devisible_by_three.append(x)
    else:
        not_devisible.append(x)

print ('Numbers devisible by two:', devisible_by_two, "\n",
    'Numbers devisible by three:', devisible_by_three, "\n",
    'Numbers not devisible by three and two:', not_devisible)
