# 导入random模块
import random
# 生成随机数,并赋值给num变量
num = random.randint(1, 101)
# 定义guessNum变量,初始化猜的次数
guess_num = 5
print("您只有" + guess_num + "次猜的机会")
# 循环输入次数
for i in range(1, guess_num + 1):
    print("请输入第" + str(i) + "次猜的数字")
    str1 = input()
    if str1 == "q":
        print("您已退出游戏")
        break
    else:
        num1 = int(str1)
        if num == num1:
            print("您猜对了")
            break
        if num < num1:
            print("您输入的数字太大了,您还有%d次输入的机会,请重新输入!" % (guess_num - i))
        if num > num1:
            print("您输入的数字太小了,您还有%d次输入的机会,请重新输入!" % (guess_num - i))
        if i == guess_num:
            print("您已经猜了5次,游戏结束")
            break
