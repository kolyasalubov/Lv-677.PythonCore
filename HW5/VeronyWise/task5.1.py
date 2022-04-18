#____version 0____
even_num = [number for number in range(1,11) if number % 2 == 0]
print(f"{even_num} is even numbers")

odd_num = [number for number in range(1,11) if number % 3 == 0 and number % 2 != 0]
print(f"{odd_num} is odd numbers")

another_num = [number for number in range(1,11) if number % 2 !=0 and number % 3 != 0]
print(f"{another_num} numbers that are not divisible by 2 and 3.")

#____version 1____
even_number = []
odd_number = []
another_number = []
for i in range(1,11):
    if i % 2 == 0:
        even_number.append(i)
    elif i % 3 == 0 and i % 2 != 0:
        odd_number.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        another_number.append(i)
print(f"{even_number} is even number, \n\
{odd_number} is odd number, \n\
{another_number} numbers that are not divisible by 2 and 3.")
