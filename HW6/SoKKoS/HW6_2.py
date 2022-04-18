import math

def rectangle_area(x, y):
    area_rectangle = x * y
    return area_rectangle

def triangle_ares(a, b, c):
    perimetr = (a + b + c) / 2
    area_triangle = math.sqrt(perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c))
    return area_triangle


def circle_area(radius):
    return math.pi * (radius ** 2)


choice_area = int(input("Your choice 1-3\n"
                        "1. area of a rectangle\n"
                        "2. area of a triangle\n"
                        "3. area of a circle\n"))

if choice_area == 1:
    print("enter x and y rectangle")
    x = float(input('x = '))
    y = float(input('y = '))
    print(f"area of a rectangle = {rectangle_area(x, y)}")
elif choice_area == 2:
    print("enter a, b and c triangle")
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(f"area of a triangle = {triangle_ares(a, b, c)}")
elif choice_area == 3:
    print("enter radius circle")
    radius = float(input("radius = "))
    print(f"area of a circle = {circle_area(radius)}")
