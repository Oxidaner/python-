str = input("请输入字符串:")
word = 0
num = 0
space = 0
other = 0
for i in str:
    if i.isalpha():  # 是否字母
        word += 1
    elif i.isdigit():  # 是否数字
        num += 1
    elif i.isspace():  # 是否是空格
        space += 1
    else:
        other += 1
print("所有字母的总数为:{0}".format(len(str)))
print("英文字母出现的次数为:{0}".format(word))
print("数字出现的次数为:{0}".format(num))
print("空格出现的次数为:{0}".format(space))
print("其他字符出现的次数为:{0}".format(other))
