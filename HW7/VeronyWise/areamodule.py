import math 
from math import(pow, pi)

def rectangle_funk():
     a = float(input("Please, enter first side of rectangle: "))
     b = float(input("Please, enter second side of rectangle: "))
     return a * b
def triangle_funk():
     a = float(input("Please, enter side of triangle: "))
     h = float(input("Please, enter height of triangle: "))
     return 0.5 * a * h
def circle_funk():
     radius = float(input("Please, enter radius of circle: "))
     return round(math.pi * math.pow(radius, 2), 2)
