# 矩形快
for i in range(1, 10):
    s = ""
    for j in range(1, 10):
        s += str.format("%d * %d = %02d  " % (i, j, i * j))
    print(s)
# 下三角
for i in range(1, 10):
    s = ""
    for j in range(1, i + 1):
        s += str.format("%d * %d = %02d  " % (i, j, i * j))
    print(s)
# 上三角
for i in range(1, 10):
    s = ""
    for k in range(1, i):
        s += ""
    for j in range(i, 10):
        s += str.format("%d * %d = %02d  " % (i, j, i * j))
    print(s)
