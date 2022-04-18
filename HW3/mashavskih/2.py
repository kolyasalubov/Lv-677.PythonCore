four_digit_number = input('Print four-digit number:\n')  #product of numbers of the four-digit number
t = int(four_digit_number[0])
h = int(four_digit_number[1])
d = int(four_digit_number[2])
o = int(four_digit_number[3])
product_of_numbers = t * h * d * o

#Revers of numbers of four-digit number

list_of_numbers = list (four_digit_number)
list_of_numbers.reverse()
revers_list_of_numbers = "".join(list_of_numbers)

#Sort numbers of the four-digit number
list_of_numbers.sort()
sort_of_numbers = "".join(list_of_numbers) 

print(f'The product of the digits of this number: {product_of_numbers}')
print(f'Revers of numbers of four-digit number: {revers_list_of_numbers}')
print(f'Sort numbers of four-digit number: {sort_of_numbers}')
