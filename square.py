class Square:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print("Area of Square =", self.a * self.b)

class Circle:

    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)

sq = Square(10, 10)
sq.area()

cr = Circle(5)
cr.area()