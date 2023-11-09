import math

class shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class triangle(shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

circle1 = circle(5)
rectangle1 = rectangle(5, 10)
triangle1 = triangle(3, 4, 5)

print("Circle area: ", circle1.area())
print("Circle perimeter: ", circle1.perimeter())
print("Rectangle area: ", rectangle1.area())
print("Rectangle perimeter: ", rectangle1.perimeter())
print("Triangle area: ", triangle1.area())
print("Triangle perimeter: ", triangle1.perimeter())