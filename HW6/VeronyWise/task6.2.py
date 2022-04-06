PI = 3.14

def rectangle_funk(a, b):
     a = float(input("Please, enter first side of rectangle: "))
     b = float(input("Please, enter second side of rectangle: "))
     return a * b
def triangle_funk(a,h):
     return 0.5 * a * h
def circle_funk(radius):
     return (PI * radius**2)

area = input("What area do you want: rectangle - 1, triangle - 2, circle - 3? ")
if area == "1":
     a = float(input("Please, enter first side of rectangle: "))
     b = float(input("Please, enter second side of rectangle: "))
     print(f"{rectangle_funk()} is area of rectangle")
elif area == "2":
     a = float(input("Please, enter side of triangle: "))
     h = float(input("Please, enter height of triangle: "))
     print(f"{triangle_funk(a,h)} is  area of triangle")
elif area == "3":
     radius = float(input("Please, enter radius of circle: "))
     print(f"{circle_funk(radius)} is area of circle")
else: 
     print("Sorry, you entered wrong number")


