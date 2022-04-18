class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides_size = [0 for i in range(n_of_sides)]

    def inputSides(self):
        self.sides_size = [float(input(f"Enter size of side {i+1}: ")) for i in range(self.n)]

    def sizeSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides_size[i]}")


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def findSquare(self):
        a, b = self.sides_size
        square = a * b
        print(f"The rectangle squere is {square}")


area = Rectangle()
area.inputSides()
area.sizeSides()
area.findSquare()

