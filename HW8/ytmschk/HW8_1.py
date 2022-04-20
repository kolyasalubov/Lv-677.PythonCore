
class Polygon():
    
    def __init__(self, n_of_sides):
        self.n_of_sides = n_of_sides
        self.sides = [i for i in range(n_of_sides)]
    
    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i+1) + " : ")) for i in range(self.n_of_sides)] 

class Triangle(Polygon):
    
    def __init__(self):
        super().__init__(3)
        print('Triangle created')
    
    def triangle_sqaure(self):
        a, b, c = self.sides
        p = (a + b + c)/2
        triangle_square = round((p*(p-a)*(p-b)*(p-c)) ** 0.5, 2)
        print('Triangle square is {}'.format(triangle_square))

trr = Triangle()
trr.input_sides()
trr.triangle_sqaure()
