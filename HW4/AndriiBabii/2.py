

element = [1, 234, 662, 19, 1213, 73, 77]
number_of_elements = len(element)

# Варіант ручного заповнення списку
# number_of_elements = int(input("Input number of elements: "))
# for i in range(number_of_elements):
#     element.append(int(input(f"inpute {i} element: ")))




for i in range(number_of_elements):
    element[i] = float(element[i])

print(element)

