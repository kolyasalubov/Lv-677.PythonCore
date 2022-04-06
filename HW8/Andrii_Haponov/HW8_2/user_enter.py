# Написати скрипт- calculator.py, в якому створюєте функції додавання, віднімання, множення, ділення,
#  а в іншому модулі запитуєте користувача, яку дію він хоче виконати і з якими числами.

import calculator

action = float(input("What action do you choose :\
                    1 - addition\
                    2 - subtraction\
                    3 - multiplication\
                    4 - division ?"))
while True:
    if  1<= action <= 4: 
        a = float(input("Enter a number 1: "))
        b = float(input("Enter a number 2: "))
        break
    else:
        print("Error! Enter a correct number!")
        action = float(input("Enter a correct number, please! - "))


if action == 1:
    print(calculator.addition(a, b))
elif action == 2:
    print(calculator.subtraction(a, b))
elif action == 3:
    print(calculator.multiplication(a, b))
elif action == 4:
    print(calculator.division(a, b))
