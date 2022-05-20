from cmath import sqrt

a = int(input("请输入公式二次项系数"))
b = int(input("请输入公式一次项系数"))
c = int(input("请输入公式常数项系数"))


def equation(a, b, c):
    x = (-b + sqrt(b**2 - 4 * a * c)) / 2 * a
    y = (-b - sqrt(b**2 - 4 * a * c)) / 2 * a
    print(str.format("得数为:{0:2.2f},{1:2.2f}", x, y))
    print("{0},{1}".format(x, y))
    print("得数为:", x, y)
    print("%s and %s" % (x, y))


equation(a, b, c)
