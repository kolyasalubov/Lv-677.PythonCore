# Task1. Write a script that will calculate the factorial 
# of the entered number  without using recursion.


# Напишите скрипт, который будет вычислять
# факториал введенного числа
# без использования рекурсии.

from math import factorial


enter_number = int(input("Enter number  : "))
factorial_enter_number = 1
for i in range(1, enter_number + 1):
    factorial_enter_number *= i
print(f"Factorial this number is : {factorial_enter_number}")