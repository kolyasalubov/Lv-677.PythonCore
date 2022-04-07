
def figure_square():
    """
    This function calculates the area of ​​a rectangle, 
    triangle and circle depending on the user's choice.
    """
    figure_number = int(input("Enter square of what figure do you want to calculate.\n"
        "Print 1 for rectangle, 2 for triangle and 3 for circle: "))
    
    if figure_number == 1:
        first_side = int(input('Enter lenght of the first side: '))
        second_side = int(input('Enter lenght of the second side: '))
        rectangle_square = lambda a, b: a * b
        print("Square of rectangle is:", rectangle_square(first_side, second_side))

    elif figure_number == 2:
        base = int(input('Enter lenght of base: '))
        vertical_height = int(input('Enter lenght of the vertical_height: '))
        triangle_square = lambda a, b: (a * b)/2
        print("Square of triangle is:", triangle_square(base, vertical_height))

    elif figure_number == 3:
        radius = int(input('Enter radius of circle: '))
        circle_square = lambda a: a**2 * 3.14
        print("Square of circle is:", circle_square(radius))

    else:
        print('The number should be 1, 2 or 3. Please try again')