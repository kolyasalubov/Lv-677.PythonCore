# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function). 

# Задание 1. Напишите функцию, которая возвращает наибольшее число из двух чисел
# (используйте строки документации DocStrings в функции).

def larg_number(num_1: int, num_2: int) -> int:
    """
    Function returns the largest number of two numbers. 
    """
    if num_1 == num_2:
        return " You entered two identical numbers"
    elif num_1 > num_2:
        return f"Numder {num_1} more"
    else:
        return f"Numder {num_2} more"

print(larg_number(input("Enter number 1 : "), input("Enter number 2 : ")))