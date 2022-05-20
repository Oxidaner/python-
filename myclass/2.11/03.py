from cmath import pi

r = float(input("请输入半径:"))
area = 4 * pi * r**2
volume = 4 / 3 * pi * r**3
print(str.format("表面积为: {0:2.2f}" + "体积为: {1:2.2f}", area, volume))
