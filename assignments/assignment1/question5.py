class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        print("The area of Shape is 0")


class Square(Shape):
    def area(self):
        result = (self.length, self.length, self.length*self.length)
        print("The area of square is %d * %d: %d" % result)



sq = Square(10)
sq.area()
sh = Shape(5)
sh.area()
