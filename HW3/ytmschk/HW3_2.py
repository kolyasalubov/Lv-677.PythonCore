input = str(input("Enter your 4-digit number: "))

if len(input) != 4:
    print ('The number should have 4 digit. Please try again.')

input_list = list(input)

numbers_multiplication = 1

for x in input_list:
    numbers_multiplication *= int(x)
print (numbers_multiplication)

reversed_order = (input_list[::-1])
reverced_integers = int("".join(reversed_order))
sorted_input = int("".join(sorted(input)))

print (reverced_integers)
print (sorted_input)