import math

a = float(input("请输入三角形的直角边a:"))
b = float(input("请输入三角形的直角边b:"))

c = math.sqrt(a * a + b * b)  # 斜边
m = a + b + c  # 周长
s = 0.5 * a * b  # 面积

print("直角三角形的三边为: a = {0}, b = {1}, c = {2}".format(a, b, c))
print("三角形周长为: {0:1.1f}, 面积为:{1:1.1f}".format(m, s))
sina = a / c
sinb = b / c

a_degree = round(math.asin(sina) * 180 / math.pi, 0)
b_degree = round(math.asin(sinb) * 180 / math.pi, 0)

print("三角形两个锐角的度数分别为: {0}, {1}".format(a_degree, b_degree))
