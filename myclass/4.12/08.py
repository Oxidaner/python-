h = int(input("请输入总头数："))
f = int(input("请输入总脚数："))


def test01(h, f):
    r = f / 2 - h
    c = h - r
    if (r <= 0 or c <= 0):
        return '无解'
    return r, c


def test02(h, f):
    for i in range(0, h):
        if (2 * i + 4 * (h - i) == f):
            return h - i, i
    return '无解'


if (not h > 0 and not f % 2 == 0 and not f > 0):
    print("无解")
elif (test01(h, f) == '无解'):
    print("无解")
else:
    print("方法一: 鸡: {0}, 兔: {1}".format(test01(h, f)[0], test01(h, f)[1]))
    print("方法二: 鸡: {0}, 兔: {1}".format(test02(h, f)[0], test02(h, f)[1]))
