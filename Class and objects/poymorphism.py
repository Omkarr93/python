class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area_calcution(self):
        return self.pi * self.radius ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_calcution(self):
        return self.length * self.width


def area(shape):
    return shape.area_calcution()


circle = Circle(10)
rect = Rectangle(10, 20)

print("Area of circle:", area(circle))
print("Area of rectangle:", area(rect))
