import figures
print('1-rectangle, 2-triangle, 3-circle')
figure = int(input('Choose a figure: '))
if figure == 1:
    width = float(input('Enter a width: '))
    lenght = float(input('Enter a lenght: '))
    print(f'The area of rectangle:{figures.area_of_a_rectangle(width, lenght)}')
elif figure == 2:
    side = float(input('Enter a side: '))
    height = float(input('Enter a height: '))
    print(f'The area of triangle:{figures.area_of_a_triangle(side, height)}')
elif figure == 3:
    radius = float(input('Enter a radius: '))
    print(f'The area of circle:{figures.area_of_a_circle(radius)}')
else:
    print('Something went wrong')