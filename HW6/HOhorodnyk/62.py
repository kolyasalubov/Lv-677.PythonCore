def area_rectangle():
    width_rectangle = float(input("Enter width:"))
    lengh_rectangle = float(input("Enter lengh:"))
    return "Area of a rectangle is {}".format(width_rectangle*lengh_rectangle)

def area_triange():
    basis_triange = float(input("Enter basis:"))
    height_triange = float(input("Enter height:"))
    return "Area of a triangle is {}".format(0.5 * basis_triange * height_triange)

def area_circle():
    PI = 3.14
    radius_circle = float(input("Enter radius:"))
    return "Area of a circle is {}".format(PI * radius_circle**2)

figure = input("1 -area_rectangle,2 - area_triange ,3-area_circle: ")

if figure == '1':
    print(area_rectangle())
elif figure == '2':
    print(area_triange())
elif figure == '3':
    print(area_circle())