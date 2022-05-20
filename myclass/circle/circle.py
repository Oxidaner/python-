import math


class Dimension:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):  # 基类的方法
        pass


class Circle(Dimension):

    count = 0

    def __init__(self, r):
        Dimension.__init__(self, r, 0)
        Circle.count += 1

    def area(self):
        return self.x * self.x * math.pi

    def perimeter(self):
        return 2 * math.pi * self.x

    def __str__(self):
        return 'Circle(%s)' % self.x

    # def __new__(self, r):
    #     Circle.count += 1

    def __del__(self):
        Circle.count -= 1

    def __eq__(self, other):
        if (self.x == other.x):
            print('equal')
        elif (self.x > other.x):
            print("self.x > other.x")
        else:
            print("self.x < other.x")


class Rectangle(Dimension):

    def __init__(self, w, h):
        Dimension.__init__(self, w, h)

    def area(self):
        return self.x * self.y

    def __eq__(self, other):
        if (self.area() == other.area()):
            print('equal')
        elif (self.area() > other.area()):
            print("self.area() > other.area()")
        else:
            print("self.area() < other.area()")


class square(Dimension):

    def __init__(self, w):
        Dimension.__init__(self, w, 0)

    def area(self):
        return self.x * self.x

    def perimeter(self):
        return 4 * self.x

    def __str__(self):
        return 'square(%s)' % self.x

    def __eq__(self, other):
        if (self.area() == other.area()):
            print('equal')
        elif (self.area() > other.area()):
            print("self.area() > other.area()")
        else:
            print("self.area() < other.area()")


d1 = Circle(2.0)
d2 = Rectangle(2.0, 4.0)
print(d1.area(), d2.area(), d1.__str__())
