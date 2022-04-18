# 52
# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle. 

# Создайте класс многоугольника и класс прямоугольника
# который наследуется от класса многоугольника и находит площадь прямоугольника.


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)  #super().__init__(3) 

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

class Rectangle(Polygon):
    def __init__(self):
        # Polygon.__init__(self,2)  
        super().__init__(2) 

    def findAreaRect(self):
        a, b = self.sides
        area = a * b
        print(f'The area of the rectangle is {round(area,2)}')



class Square(Polygon):
    def __init__(self):
        # Polygon.__init__(self,1)  
        super().__init__(1) 

    def findAreaSquars(self):
        a =  self.sides[0]
        area = a ** 2
        print(f"The area of the square is {round(area,2)}")

t = Square()
t.inputSides()
t = t.findAreaSquars()

# print(Square.__mro__)