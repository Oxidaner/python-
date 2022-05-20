def ways02():
    n = int(input("项数："))
    total = 0
    flag = True
    for i in range(1, 2 * n, 2):
        if (flag):
            total += i
            flag = False
        else:
            total -= i
            flag = True
    print(total)


def ways01():
    n = int(input("项数："))
    total = 0
    x = 2
    for i in range(1, 2 * n, 2):
        total += pow(-1, x) * i
        x += 1
    print(total)


ways01()
