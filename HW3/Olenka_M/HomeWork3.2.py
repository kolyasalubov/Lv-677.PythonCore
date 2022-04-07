print("\n--------------task 2.2---------------\n")

#Version 0

#number = 2978
#print(type(number))

#digits_of_number = str(number)
#print(digits_of_number)

# product_of_digits = (int(digits_of_number[0]) * int(digits_of_number[1]) *
# int(digits_of_number[2]) * int(digits_of_number[3]))
# print(product_of_digits)

# Version 0 end

print("\n----------------Version 1----------------\n")

# Version 1

number = 2978
digits_of_number = str(number)
product_of_digits = 1

list_of_digit = list(digits_of_number)
#print(list_of_digit)

for digit in list_of_digit:
    product_of_digits *= int(digit)
print('Product of digits:', product_of_digits)

print("----------------------------------------------\n")

reversed_number = int(digits_of_number[::-1])
print('Reversed number:', reversed_number)

print("----------------------------------------------\n")

sort_digits_of_number = int(''.join(sorted(digits_of_number)))
print('Sort digits of number:', sort_digits_of_number)

print("----------------------------------------------\n")
