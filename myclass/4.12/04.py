import random

a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)


def random01(a, b, c):
    maxNum = max(a, b, c)
    minNum = min(a, b, c)
    midNum = sum([a, b, c]) - minNum - maxNum
    print("方法一: {0},{1},{2}".format(minNum, midNum, maxNum))


def random02(a, b, c):
    if (a > b):
        a, b = b, a
    if (a > c):
        a, c = c, a
    if (b > c):
        b, c = c, b
    print("方法二: {0},{1},{2}".format(a, b, c))


def random03(a, b, c):
    a = [a, b, c]
    a.sort()
    print(a)


print("原始值: {0},{1},{2}".format(a, b, c))
random01(a, b, c)
random02(a, b, c)
random03(a, b, c)
