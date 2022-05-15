def area_rectangle (a,b):
    area_r = a*b
    print("Area of rectangle with provided data of lenght and width is ", area_r, "square metres")
    return(area_r)

def area_triangle (b,h):
    area_t = (h*b)/2
    print("Area of triangle with provided data of base and heigh is ", area_t, "square metres")
    return(area_t)

def area_circle (r):
    area_c = 3.141592653589793238*r**2
    print("Area of circle with provided data of radius is ", area_c, "square metres")
    return(area_c)

area_rectangle(45,23)
area_triangle(34,45)
area_circle(65)

# Task2. 
# Write a program that calculates the area of ​​a rectangle, triangle and circle
# (write three functions to calculate the area, and call them in the main program depending on the user's choice).

