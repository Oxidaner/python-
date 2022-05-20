from circle import Circle, square

radius = float(input('圆半径: '))
slen = float(input('正方形边长: '))
x = Circle(radius)
y = square(slen)
x2 = Circle(radius)

print(x.perimeter())
print(x.area())
print(x.__str__())
print(x.count)

x2.__del__()
print(x.count)

print(y.perimeter())
print(y.area())
print(y.__str__())
