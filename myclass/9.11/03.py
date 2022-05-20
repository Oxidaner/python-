class Temperature:

    def __init__(self, degree):
        self.degree = degree

    def toFahrenheit(self):
        return self.degree * 9 / 5 + 32

    def toCelsius(self):
        return (self.degree - 32) * 5 / 9


if __name__ == '__main__':
    n1 = float(input("请输入摄氏温度："))
    t1 = Temperature(n1)
    print("摄氏温度 = {0:.2f}, 华氏温度 = {1:.2f}".format(n1, t1.toFahrenheit()))
    n2 = float(input("请输入华氏温度："))
    t2 = Temperature(n2)
    print("摄氏温度 = {0:.2f}, 华氏温度 = {1:.2f}".format(t2.toCelsius(), n2))
