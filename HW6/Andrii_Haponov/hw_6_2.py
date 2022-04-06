# Task2. Write a program that calculates the area of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, 
# and call them in the main program depending on the user's choice).

# Задача2. Написать программу, вычисляющую площадь прямоугольника, треугольника и круга
# (напишите три функции для вычисления квадрата,
# и вызывать их в основной программе в зависимости от выбора пользователя).

import math

def erea_rectangle(a, b):
    p_rectangle = a*b
    return p_rectangle

def erea_triangle(c, h):
    p_triangle = c * h * 0.5
    return p_triangle

def erea_circle(r):
    p_circle = math.pi * r**2
    return p_circle

figure = int(input(
                "Enter 1 if calculates  the area of a rectangle,\
                2 if calculates the area of a triangle and \
                3 if calculates the area of a circle : "
                ))

if figure == 1:
    print(erea_rectangle(int(input("Enter the side 1: ")), int(input("Enter the side 1: "))))
elif figure == 2 :
    print(erea_triangle(int(input("Enter the triangle height: ")), int(input("Enter the base of a triangle: "))))
elif figure == 3:
    print(erea_circle(int(input("Enter the circle radius: "))))
else:
    print("Error you do not enter a valid number!!!")
    