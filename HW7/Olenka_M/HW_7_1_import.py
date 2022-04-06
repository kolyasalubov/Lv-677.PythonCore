import HW_7_1_def_sqaure as sq

user_choice = input("Please, enter number 1, if you want to get rectangle sqaure;\n\
enter number 2, if you want to get triangle sqaure;\n\
enter number 3, if you want to get circle sqaure.\n\
Please, do your choice: ")

if user_choice == "1":
    side_a = float(input("Please, enter first side of rectangle: "))
    side_b = float(input("Please, enter second side of rectangle. Which is adjacent of first side \
and measured in the same units: "))
    print(f"Rectangle sqaere is: {sq.rectangle_square(side_a, side_b)}")
elif user_choice == "2":
    side_a = float(input("Please, enter side of triangle: "))
    height_a = float(input("Please, enter height of triangle which drawn to side that you entered and \n\
which measured in the same units: "))
    print(f"Triangle square is {sq.triangle_square(side_a, height_a)}")
elif user_choice == "3":
    radius = float(input("Please, enter radius of circle: "))
    print(f"Circle square is {sq.circle_square(radius)}")    
else: ("Sorry, you entered wrong number")
