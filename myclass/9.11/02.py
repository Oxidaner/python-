import math


class MyMath:

    def __init__(self, r):
        self.r = r

    def perimeter_round(self):
        return 2 * math.pi * self.r

    def area_round(self):
        return math.pi * self.r * self.r

    def area_ball(self):
        return 4 * math.pi * self.r**2

    def volume_ball(self):
        return 4 / 3 * math.pi * self.r**3


if __name__ == '__main__':
    n = float(input("请输入半径："))
    m = MyMath(n)
    print("圆的周长 = {0:.2f}\n圆的面积 = {1:.2f}\n球的表面积 = {2:.2f}\n球的体积 = {3:.2f}".
          format(m.perimeter_round(), m.area_round(), m.area_ball(),
                 m.volume_ball()))
