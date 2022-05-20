from itertools import accumulate
import operator


# for
def function():
    a = int(input("请输入一个非负整数"))
    ans = 1
    if a < 0:
        function()
    elif a >= 0:
        for i in range(a, 0, -1):
            ans *= i
    print(ans)


# while
def function2():
    a = int(input("请输入一个非负整数"))
    ans = 1
    if a < 0:
        function2()
    while (a >= 1):
        ans *= a
        a -= 1
    print(ans)


# 迭代
def function3():
    a = int(input("请输入一个非负整数"))
    ans = 1
    if a < 0:
        function3()
    x = list(accumulate(range(1, a + 1), operator.mul))  # 迭代,累乘
    ans = x[len(x) - 1]
    print(ans)


# 递归
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def function4():
    number = int(input("请输入一个正整数:"))
    if number < 0:
        function4()
    else:
        ans = factorial(number)
        print(ans)


# function()
# function2()
# function3()
function4()
