import hw_7_1

figure = int(input(
                "Enter 1 if calculates  the area of a rectangle,\
                2 if calculates the area of a triangle and \
                3 if calculates the area of a circle : "
                ))
while True:
    
    if figure == 1:
        print(hw_7_1.erea_rectangle(int(input("Enter the side 1: ")), int(input("Enter the side 1: "))))
        break
    elif figure == 2 :
        print(hw_7_1.erea_triangle(int(input("Enter the triangle height: ")), int(input("Enter the base of a triangle: "))))
        break
    elif figure == 3:
        print(hw_7_1.erea_circle(int(input("Enter the circle radius: "))))
        break
    else:
        print("Error you do not enter a valid number!!!")
        figure = int(input(
                "Enter 1 if calculates  the area of a rectangle,\
                2 if calculates the area of a triangle and \
                3 if calculates the area of a circle : "
                ))
        