num = int(input("Put the number: "))
str_num = str(num)
mult = 1
num_list = list(str_num)

for each_num in num_list:
    mult *= int(each_num)
print("Product of numbers = ", mult)

print("Reversed numbers: ", str_num[-1::-1])
print("Sorted numbers: ", sorted(num_list))
input()
