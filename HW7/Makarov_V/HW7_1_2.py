import HW7_1_1 as my_square

choice = input("Which geometric figure?\n"
               "Choose rectangle, triangle or circle: ")

while choice:
    if choice == "rectangle":
        width = float(input("Enter the width of rectangle: "))
        height = float(input("Enter the height of rectangle: "))
        print(f"The area of rectangle is {my_square.area_of_rectangle(width, height)}")
        break
    elif choice == "triangle":
        leg_1 = float(input("Enter the first leg of triangle: "))
        leg_2 = float(input("Enter the second leg of triangle: "))
        print(f"The area of triangle is {my_square.area_of_triangle(leg_1, leg_2)}")
        break
    elif choice == "circle":
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of circle is {my_square.area_of_circle(radius)}")
        break
    else:
        print("You chose the wrong figure")
        choice = input("Choose the proper figure: ")
