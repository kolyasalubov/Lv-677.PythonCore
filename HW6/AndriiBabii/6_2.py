# Write a program 
# that calculates the area of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, 
# and call them in the main program depending on the user's choice).

def area_circle(r):
    return round(3.141592*r**2, 2)

def area_triangle(a,h):
    return 0.5*a*h

# p = (a + b + c) / 2
# return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_rectangle(a,b):
    return a*b

def shape_picker(a):
    if a == 1:
        return area_circle(float(input("Input radius of circle: ")))
    elif a == 2:
        return area_triangle(
            float(input("Input side: ")), 
            float(input("Input height: ")))
    elif a == 3:
        return area_rectangle(
            float(input("Input first side: ")), 
            float(input("Input second side: ")))
    else:
        return None


print(shape_picker(int(input(
"""
Введіть:
1 - Для обчислення площі кола
2 - Для обчислення площі трикунтника
3 - Для обчислення площі прямокутника
"""))))
