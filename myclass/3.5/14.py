import random

a = random.randint(0, 100)
b = random.randint(0, 100)
sum = a * b

print(a)  # 输出原来的a，b
print(b)

if (a < b):
    a, b = b, a

while (a % b != 0):
    a, b = b, a % b

# 最小公倍数是相乘除以最大公约数
print("最大公约数：{0}，最小公倍数：{1}".format(b, sum / b))
