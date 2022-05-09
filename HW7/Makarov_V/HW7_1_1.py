from math import pi
from math import pow


def area_of_rectangle(width, height):
    """
    This function calculates the area
    of rectangle by using
    its width and height
    """
    rectangle_area = width * height
    return rectangle_area


def area_of_triangle(leg_1, leg_2):
    """
    This function calculates the area
    of right triangle by using
    the legs of it
    """
    triangle_area = (1/2)*(leg_1 * leg_2)
    return triangle_area


def area_of_circle(radius):
    """
    This function calculates the area
    of circle by using
    its radius
    """
    circle_area = round(pow(radius, 2) * pi, 2)
    return circle_area
