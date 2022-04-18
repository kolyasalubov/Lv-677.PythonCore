generate_list = []
number = int(input("Enter you number: "))
for num in range(number+1):
    generate_list.append(num)
print(generate_list)
generate_list2 = list(map(float, generate_list))
print(generate_list2)

#############################################

generate_list = []
number = int(input("Enter you number: "))
for num in range(1, number+1):
    generate_list.append(num)
print(generate_list)
num_list = generate_list
num_list_float = []
for num in num_list:
    num_list_float.append(float(num))
print(num_list_float)

###########################

generate_list = []
number = int(input("Enter you number: "))
for num in range(1, number+1):
    generate_list.append(num)
print(generate_list)
num_list = generate_list
result = [float(num_list) for num_list in num_list]
print(result)

######################################
