from areamodule import *

area = input("What area do you want: rectangle - 1, triangle - 2, circle - 3? ")

if area == "1":
     print(f"{rectangle_funk()} is area of rectangle")
elif area == "2":
     print(f"{triangle_funk()} is  area of triangle")
elif area == "3":
     print(f"{circle_funk()} is area of circle")
else: 
     print("Sorry, you entered wrong number")
