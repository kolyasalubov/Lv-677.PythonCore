class Polygon:
    def __init__(self, num_sides):
        self.num = num_sides
        self.sides = [0 for i in range(num_sides)]
    def inputsides(self):
        self.sides = [float(input(f'Enter sides: ')) for i in range(self.num)]
    def outputsides(self):
        for i in range(self.num):
            print (f'Side {self.sides[i]}')
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)
    def squarerectangle(self):
        a, b = self.sides
        area = a* b 
        print(f'The area of rectangle: ',area)


