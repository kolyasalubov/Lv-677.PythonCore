from math import pow
from math import pi

def area_circle(r):
    return round(pi*pow(r,2), 2)

def area_triangle(a,h):
    return 0.5*a*h

def area_rectangle(a,b):
    return a*b
