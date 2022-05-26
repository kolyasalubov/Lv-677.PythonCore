#Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від
#1 до 100 і пропонує користувачу вгадати це число.

import random
from tkinter.tix import InputOnly

number = random.randint(1, 101)
input_number = int(input('Enter a number from 1 to 100 inclusive: '))

while True:
    if input_number == number:
        print('You guessed! Congratulations!')
        break
    elif input_number > number:
        input_number = int(input('Choose a smaller number: '))
    else:
        input_number < number
        input_number = int(input('Choose a larger number: '))