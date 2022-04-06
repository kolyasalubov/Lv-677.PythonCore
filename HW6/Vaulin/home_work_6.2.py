# Task2. Write a program that calculates the area of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).
def rect(a , b):
    return a * b
def triang(a, b):
    return 0.5 * a * b
def circle(b):
    return 3.14 * (b**2)
choise = {1: "Rectangle", 2: "Circle", 3: "Triangle"}

print("What u want ot calculate: 1: Rectangle, 2: Triangle or 3: Circle " )
while True:
    math = (input())
    if math == choise[1]:
        num_1 = int(input("Enter length: "))
        num_2 = int(input("Enter width: "))
        print ("The area of rectangle is: ", rect(num_1, num_2))
        break
    elif math == choise[2]:
        print ("The area of a circle is the product of the square of the radius times pi.")
        num_1 = int(input("Enter your radius: "))
        print ("The area of circle: ", circle(num_1))
        break
    elif math == choise[3]:
        num_1 = int(input("The length of a side: "))
        num_2 = int(input("The length of the altitude drawn to that side: "))
        print ("The area of triangle: ", triang(num_1, num_2))
        break
    else:
        print("Try again")