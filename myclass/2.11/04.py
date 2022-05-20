years = int(input("请输入年数"))
money = int(input("请输入本金:"))
rate = float(input("请输入年利率(<1):"))


def getValue(money, rate, years):
    v = money * (rate + 1)**years
    return v


print(str.format("最终收益为: {0:2.2f}", getValue(money, rate, years)))
