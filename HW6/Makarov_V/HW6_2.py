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
    circle_area = 3.14 * radius**2
    return circle_area


choice = input("Which geometric figure?\n"
               "Choose rectangle, triangle or circle: ")

while choice:
    if choice == "rectangle":
        width = float(input("Enter the width of rectangle: "))
        height = float(input("Enter the height of rectangle: "))
        rectangle_area = area_of_rectangle(width, height)
        print(f"The area of rectangle is {rectangle_area}")
        break
    elif choice == "triangle":
        leg_1 = float(input("Enter the first leg of triangle: "))
        leg_2 = float(input("Enter the second leg of triangle: "))
        triangle_area = area_of_triangle(leg_1, leg_2)
        print(f"The area of triangle is {triangle_area}")
        break
    elif choice == "circle":
        radius = float(input("Enter the radius of the circle: "))
        circle_area = area_of_circle(radius)
        print(f"The area of circle is {circle_area}")
        break
    else:
        print("You chose the wrong figure")
        choice = input("Choose the proper figure: ")
