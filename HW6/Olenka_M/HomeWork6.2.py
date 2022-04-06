def rectangle_square(side_a: float, side_b: float) -> float:
    """
    Function returns square of rectangle if we have two adjacent sides of one, 
    which are measured in the same units
    """
    return side_a*side_b

def triangle_square(side_a: float, height_a: float) -> float:
    """
    Function returns square of triangle if we have side of one and height drawn to this side, 
    which are measured in the same units.
    The first argument is the side.
    The second argument is the height.
    """
    return 1/2*(side_a*height_a)

def circle_square(radius: float) -> float:
    """Function returns square of circle if we radius, rounted to 2 points"""
    return round(radius**2*3.141592653589793, 2)

user_choice = input("Please, enter number 1, if you want to get rectangle sqaure;\n\
enter number 2, if you want to get triangle sqaure;\n\
enter number 3, if you want to get circle sqaure.\n\
Please, do your choice: ")

if user_choice == "1":
    side_a = float(input("Please, enter first side of rectangle: "))
    side_b = float(input("Please, enter second side of rectangle. Which is adjacent of first side \
and measured in the same units: "))
    print(f"Rectangle sqaere is: {rectangle_square(side_a, side_b)}")
elif user_choice == "2":
    side_a = float(input("Please, enter side of triangle: "))
    height_a = float(input("Please, enter height of triangle which drawn to side that you entered and \n\
which measured in the same units: "))
    print(f"Triangle square is {triangle_square(side_a, height_a)}")
elif user_choice == "3":
    radius = float(input("Please, enter radius of circle: "))
    print(f"Circle square is {circle_square(radius)}")    
else: ("Sorry, you entered wrong number")
