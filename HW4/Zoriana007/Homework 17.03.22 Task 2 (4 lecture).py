n = int(input("Please input number: "))
elements = [n-1,n,n+1]
print(elements, "- type of each element of a list is ", type(elements[0]))
print("Lets transform it to float:")
for n in [n-1,n,n+1]:
    elements[0] = float(elements[0])
    elements[1] = float(elements[1])
    elements[2] = float(elements[2])
print(elements)