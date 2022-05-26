from math import pi

def square_rectangle():
    '''
    Function returns square of rectangle
    '''
    a = float(input('Entered width: '))
    b = float(input('Entered height: '))
    return 'Square of rectangle is = {}'.format(round((a * b), 2))

def square_triangle():
    '''
    Function returns square of tritangle
    '''
    a = float(input('Entered basis: '))
    b = float(input('Entered height: '))
    return 'Square of triangle is = {}'.format(round((0.5 * a * b), 2))

def square_circle():
    '''
    Function returns square of circle
    '''
    r = float(input('Entered radius: '))
    return 'Square of circle is = {}'.format(round((pi * r ** 2), 2))

def figure_definition():
    '''
    The function allows you to select a figure
    '''
    while True:
        figure = input('Choose 1,2 or 3(1 - rectangle, 2 - triangle, 3 - circle): ')
        if figure == '1':
            return square_rectangle()
        elif figure == '2':
            return square_triangle()
        elif figure == '3':
            return square_circle()
        print("Input is invalid")

print(figure_definition())
