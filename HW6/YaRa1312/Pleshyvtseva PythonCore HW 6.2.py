# 6.2
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
    trian_area = 1/2*a*h
    return(f"The triangle area is {trian_area}")

def circle_area(r):
    '''
    The function calculates a circle area
    based on user parameter (length of radius).
    Pi is written to within 11 characters
    after the comma.
    '''
    circ_area = 3.14159265359 * r * r
    return(f"The circle area is {circ_area}")


user_choice = input("Enter a geometrical figure which area you would like to count. Choose between rectangle, triangle and circle: ")
if user_choice == "rectangle" or user_choice == "Rectangle":
    a = int(input("Enter length value: "))
    b = int(input("Enter width value: "))
    print(rectangle_area(a, b))
elif user_choice == "triangle" or user_choice == "Triangle":
    a = int(input("Enter length value of a side to which the high is drawn: "))
    h = int(input("Enter a length value of a high that is drawn to the side 'a': "))
    print(triangle_area(a, h))
elif user_choice == "circle" or user_choice == "Circle":
    r = int(input("Enter a radius value: "))
    print(circle_area(r))
else:
    print("Error, try again")
    
