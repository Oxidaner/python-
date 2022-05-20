import sys  # 目的是为了调用exit()中途退出程序

print("——————————————本系统用于输出某一天的下一天日期——————————————")
tmp = 1
while tmp:
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入是这个月的第几天："))

    if month < 12 and month > 0 and day <= 31 and day > -1:
        tmp = 0
    else:
        print("非法输入！请重新输入")

if day == 31:  # 当day为31
    if month in [1, 3, 5, 7, 8, 10]:  # 大月 月份+1, day = 1
        month += 1
        day = 1
    elif month == 12:  # 12月 年份+1, 月份 = 1, day = 1
        year += 1
        month = 1
        day = 1
    else:  # 其他月份： 非法
        print("非法输入！")
        sys.exit()  # 结束程序

elif day == 30:  # 当day为30
    if month in [1, 3, 5, 7, 8, 10, 12]:  # 大月：day + 1
        day += 1
    elif month in [4, 6, 9, 11]:  # 小月：月份+1, day = 1
        month += 1
        day = 1
    else:  # 2月：非法
        print("非法输入！")
        sys.exit()

elif day == 29:  # 当day为29
    if month == 2 and (not (year % 4) and
                       year % 100) or not (year % 400):  # 2月闰年：月+1， day = 1
        month += 1
        day = 1
    elif month == 2:  # 二月平年：非法
        print("非法输入！")
        sys.exit()
    else:  # 其他月份
        day += 1
#
elif day == 28:  # day 为28
    if month == 2 and not ((not (year % 4) and year % 100)
                           or not (year % 400)):  # 2月平年：月+1，  day = 1
        month += 1
        day = 1
    else:  # 2月平年之外的其他日期
        day += 1
# ————除了特殊的三天之外的其他日期————
else:
    day += 1
print("当前日期的下一天是：", year, "年", month, "月", day, "日")
