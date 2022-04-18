import home_worka
choise = {1: "Rectangle", 2: "Circle", 3: "Triangle"}

print("What u want ot calculate: 1: Rectangle, 2: Triangle or 3: Circle " )
while True:
    math = (input())
    if math == choise[1]:
        num_1 = int(input("Enter length: "))
        num_2 = int(input("Enter width: "))
        print ("The area of rectangle is: ", home_worka.rectangle(num_1, num_2))
        break
    elif math == choise[2]:
        print ("The area of a circle is the product of the square of the radius times pi.")
        num_1 = int(input("Enter your radius: "))
        print ("The area of circle: ", home_worka.circle(num_1))
        break
    elif math == choise[3]:
        num_1 = int(input("The length of a side: "))
        num_2 = int(input("The length of the altitude drawn to that side: "))
        print ("The area of triangle: ", home_worka.triangle(num_1, num_2))
        break
    else:
        print("Try again")