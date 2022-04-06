# Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 
# і пропонує користувачу вгадати це число. 

# Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане 
# число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, 
# тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

import random

random_number = random.randint(1, 100)


usrere_number = int(input("Enteк a number from 1 to 100: "))

while usrere_number != random_number:
    if usrere_number > random_number:
        print("Your number is more!")
        usrere_number = int(input("Enter a number less: "))
    elif usrere_number < random_number:
        print("Your number is less!")
        usrere_number = int(input("Enter a number more: "))
else:
    print(f"Congratulations, you guessed the correct number {random_number} !")