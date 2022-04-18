number = 2355
num_str = str(number) #task 1
dobutok_num = int(num_str[0]) * int(num_str[1]) * int(num_str[2]) * int(num_str[3])
print('Dobutok numbers:', dobutok_num)

num_list = list(num_str) #task 2
num_list.reverse()
number_reverse = "".join(num_list)
print('Reverse number:', number_reverse)

num_list = list(num_str) #task 3
sort_list = sorted(num_list)
print('Sorted numbers in this number:', sort_list) #exampe 1
print(f"Sorted numbers in this number: {sort_list}") #exampe 2
