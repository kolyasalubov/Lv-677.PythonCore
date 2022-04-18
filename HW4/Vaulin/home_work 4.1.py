# Lv-677.PythonCore

## Home Work 3.13
#Task1 - Write a script that will calculate the factorial of the entered number  without using recursion.
number = int(input("Enter your number :"))
factorial = 1
if number > 0:
    for n in range(1, number +1):
        factorial = n * factorial
    print (f'!{number} is {factorial}')
else:
    print ("Your number is less or equal to zero. Try again. ")

# Time to practice №1

# x1 = int(input("Write first number: "))
# x2 = int(input("Write second number: "))
# variant = ('Первое число {x1} больше или равно {x2}' if x1>=x2 else 'Первое число {x1} меньше или равно {x2}')
# print(variant)

# ## Time to practice №2:

# x1 = int(input("Write your number: "))
# if x1 % 2 == 0:
#     print (f'{x1} is even number')
# else:
#     print (f'{x2} is odd number')