#Task1. Write a script that will calculate the factorial 
#of the entered number without using recursion.

from math import factorial
number = int(input('Enter your number:'))
factorial_number = 1
for n in range(1, number + 1):
    factorial_number *= n
print(f'Factorial this number is: {factorial_number}')