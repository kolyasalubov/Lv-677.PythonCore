# 8

class Polygon():
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides_value = [0 for i in range(num_of_sides)]
    def inputSides(self):
        self.sides_value = [float(input('Enter side'+str(i+1)+' : ')) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    def rectArea(self):
        length_rect, width_rect = self.sides_value
        rect_area = length_rect * width_rect
        print(f"Rectangle area is {rect_area}")

r1 = Rectangle()
r1.inputSides()
r1.rectArea()
