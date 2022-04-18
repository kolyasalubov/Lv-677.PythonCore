enter_number = input("Enter a four-digit number: ")
list_number = list(enter_number)
product_of_numbers = int(list_number[0])*int(list_number[1])*int(list_number[2])*int(list_number[3])
print(product_of_numbers)

print(enter_number[::-1])

sorted_list_number = list_number
sorted_list_number.sort()
sorted_number = "".join(sorted_list_number)
print(sorted_number)