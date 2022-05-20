money = int(input("请输入本金:"))
rate = int(input("请输入年利率:"))
years = int(input("请输入年数:"))
amount = money*((1+rate/100)**years)
print(str.format("本金利率和为:{0:2.2f}", amount))
# 右边的参数大佬讲“冒号右面的第一个数字是修饰符,不影响结果的,只是对输出格式有影响,有多种方式，默认是不填的
