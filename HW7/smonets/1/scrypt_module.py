import math

def area_rectangle(a, b):
    """ 
    calculates the area of a rectangle
    where:
    a = side1
    b = side2
    """
    
    return a * b

def area_triangle(a, h):
    """ 
    calculates the area of a triangle
    where: 
    a = base of triangle
    h = height of triangle
    """
    
    return 0.5 * a * h

def area_circle(r):
    """ 
    calculates the area of circle
    where:
    r = radius of circle
    """
    
    return  math.pi * (math.pow(r, 2))

