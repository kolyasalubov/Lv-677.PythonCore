x1 = []
x2 = []
x3 = []

for i in range(1,11):
    if i % 2 == 0:
        x1.append(i)
    if i % 3 == 0:
        x2.append(i)
    else:
        x3.append(i)

print(x1)
print(x2)
print(x3)