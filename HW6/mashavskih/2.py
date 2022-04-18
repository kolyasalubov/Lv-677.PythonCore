import math

def rectangle(lenght_rectangle, breadth_rectangle):
    area_rectangle = lenght_rectangle*breadth_rectangle
    print(f'The area of rectangle is {area_rectangle}.')
def triangle(base_triangle, height_triangle):
    area_triangle = 0.5 * base_triangle * height_triangle
    print(f'The area of triangle is {area_triangle}.')
def circle(radius_squared):
    area_circle = math.pi * math.pow(radius_squared, 2)
    print(f'The area of circle is {area_circle}.')  
          
def calc_area(choice):
        if choice == 1:
            lenght_rectangle = int(input('Enter lenght of rectangle:\n'))
            breadth_rectangle = int(input('Enter breadth of rectangle:\n'))
            return rectangle(lenght_rectangle, breadth_rectangle)
        elif choice == 2:
            base_triangle = int(input('Enter base of triangle:\n'))
            height_triangle = int(input('Enter heighr of triangle:\n')) 
            return triangle(base_triangle, height_triangle)
        elif choice == 3:
            radius_squared = float(input('Enter radius squared of circle:\n'))
            return circle(radius_squared)
        else:
            print('This number not available!')

if __name__ == "__main__" :
    print('Calculate square of area shape:\n 1 -> Rectangle;\n 2 -> Triangle;\n 3 -> Circle')
    choice= int(input('Enter the number of shape whose area you want to find: '))
    calc_area(choice)   
