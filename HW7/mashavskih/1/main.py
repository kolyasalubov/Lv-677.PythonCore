import scrypt

print('Calculate square of area shape:\n 1 -> Rectangle;\n 2 -> Triangle;\n 3 -> Circle')
choice= int(input('Enter the number of shape whose area you want to find: '))

if choice == 1:
    lenght_rectangle = int(input('Enter lenght of rectangle:\n'))
    breadth_rectangle = int(input('Enter breadth of rectangle:\n'))
    print(f'The area of rectangle is {scrypt.rectangle(lenght_rectangle, breadth_rectangle)}.')
elif choice == 2:
    base_triangle = int(input('Enter base of triangle:\n'))
    height_triangle = int(input('Enter heighr of triangle:\n')) 
    print(f'The area of triangle is {scrypt.triangle(base_triangle, height_triangle)}.')
elif choice == 3:
    radius_squared = float(input('Enter radius squared of circle:\n'))
    print(f'The area of circle is {scrypt.circle(radius_squared)}.')
else:
    print('This number not available!')
    