import math
def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return a * h * 0.5
    
def circle_area(r):
    return math.pi * pow(r, 2)
    
def main():
    while True:
        action = input('Input the number of action that you want to do.\n' +
        '1 - count rectangle area\n' +
        '2 - count triangle area\n' +
        '3 - count circle area\n')
        if action == '1':
            a = int(input('Input first side: \n'))
            b = int(input('Input second side: \n'))
            print(f'Count of rectangle area is = {rectangle_area(a, b)}')
        elif action == '2':
            a = int(input('Input bottom side: \n'))
            h = int(input('Input height: \n'))
            print(f'Count of triangle area is = {triangle_area(a, h)}')
        elif action == '3':
            r = int(input('Input radius: \n'))
            print(f'Count of circle area is = {circle_area(r)}')
        else:
            break
    print('end')
    
if __name__ == '__main__':
    main()
