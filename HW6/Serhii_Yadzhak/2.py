def area_of_a_rectangle(a, b):
    return a * b
def area_of_a_triangle(a, h):
    return 1/2*a*h
def area_of_a_circle(r):
    from math import pi
    return pi*r**2
print('1-rectangle, 2-triangle, 3-circle')
figure = int(input('Choose a figure: '))
if figure == 1:
    width = float(input('Enter a width: '))
    lenght = float(input('Enter a lenght: '))
    print(area_of_a_rectangle(width, lenght))
elif figure == 2:
    side = float(input('Enter a side: '))
    height = float(input('Enter a height: '))
    print(area_of_a_triangle(side, height))
else:
    radius = float(input('Enter a radius: '))
    print(area_of_a_circle(radius))
