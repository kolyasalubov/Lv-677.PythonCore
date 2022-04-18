input = int(input('Input last element of Fibonacci range\n'))
list = []

for n in range(input+1):
    if list:
        next_element = list[-1] + int(n)
        if next_element < input+1:
            list.append(next_element)
        else:
            break
    else:
        list.append(n)
    
print(list)
