import math

def rectangle(lenght_rectangle, breadth_rectangle):
    area_rectangle = lenght_rectangle * breadth_rectangle
    return area_rectangle
def triangle(base_triangle, height_triangle):
    area_triangle = 0.5 * base_triangle * height_triangle
    return area_triangle
def circle(radius_squared):
    area_circle = math.pi * math.pow(radius_squared, 2)
    return area_circle
    