#Task1. Write a script that will calculate the factorial 
#of the entered number without using recursion.

number = int(input('Enter your number:'))
factorial_number = 1

if number == 1 or number == 0:
    print(f'Factorial this number is: {factorial_number}')
elif number < 0:
    print("Factorial non pisitive number don't exist!")
else:
    for n in range(1, number + 1):
        factorial_number *= n
    print(f'Factorial this number is: {factorial_number}')
