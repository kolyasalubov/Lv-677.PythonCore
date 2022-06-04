# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides_size = [0 for i in range(n_of_sides)]

    def inputSides(self):
        self.sides_size = [float(input(f"Enter size of side {i+1}: ")) for i in range(self.n)]

    def sizeSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides_size[i]}")

class Quadrate(Polygon):
    def __init__(self):
        super().__init__(1)

    def findSquare(self):
        a = self.sides_size[0]
        square = a ** 2
        print(f"The rectangle squere is {square}")

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findSquare(self):
        a, b = self.sides_size
        square = a * b
        print(f"The rectangle squere is {square}")

r = Rectangle()
r.inputSides()
r.sizeSides()
r.findSquare()

# q = Quadrate()
# q.inputSides()
# q.sizeSides()
# q.findSquare()
