from math import pi
from math import pow


def rectangle_area(a, b):
    '''
    The function calculates a rectangle area
    based on user length and width parameters.
    It can also calculate a quadrant area.
    '''
    rect_area = a * b
    return(f"The rectangle area is {rect_area}")
 
def triangle_area(a, h):
    '''
    The function calculates a triangle area
    based on user parameteres (length value
    of a side and a length value of a high
    that is drawn to the mentioned side).
    '''
    trian_area = 0.5*a*h
    return(f"The triangle area is {trian_area}")
        
def circle_area(r):
    '''
    The function calculates a circle area
    based on user parameter (length of radius).
    '''
    circ_area = pi * pow(r, 2)
    return(f"The circle area is {circ_area}")
