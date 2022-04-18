# Task2. Create a list that contains elements of integer type,
# then use the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

element = [2, 5, 16, 45, 87, 129, 4332, 99, 303]
element_nubmer = len(element)
for n in range(element_nubmer):
    element[n] = float(element[n])
print(element)
