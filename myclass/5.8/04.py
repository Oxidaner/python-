# 内置函数
s = [9, 7, 8, 3, 2, 1, 55, 6]
print("元素个数：{0}，最大值：{1}，最小值：{2}，和：{3}，平均值：{4}".format(len(s), max(s), min(s),
                                                      sum(s),
                                                      sum(s) / len(s)))
# 直接访问
sum = 0
max = s[0]
min = s[0]
length = 0
for i in s:
    sum += i
    length += 1
    if (i > max):
        max = i
    if (i < min):
        min = i

print("元素个数：{0}，最大值：{1}，最小值：{2}，和：{3}，平均值：{4}".format(length, max, min, sum,
                                                      sum / length))

# 间接访问
s = [9, 7, 8, 3, 2, 1, 55, 6]
sum = 0
max = s[0]
min = s[0]
length = len(s)
for i in range(0, length):
    sum += s[i]
    if (s[i] > max):
        max = s[i]
    if (s[i] < min):
        min = s[i]

print("元素个数：{0}，最大值：{1}，最小值：{2}，和：{3}，平均值：{4}".format(length, max, min, sum,
                                                      sum / length))

# 正序访问
s = [9, 7, 8, 3, 2, 1, 55, 6]

sum = 0
max = s[0]
min = s[0]
length = len(s)

i = 0
while (i < length):
    sum += s[i]
    if (s[i] > max):
        max = s[i]
    if (s[i] < min):
        min = s[i]
    i += 1

print("元素个数：{0}，最大值：{1}，最小值：{2}，和：{3}，平均值：{4}".format(length, max, min, sum,
                                                      sum / length))
# 反序访问
s = [9, 7, 8, 3, 2, 1, 55, 6]

sum = 0
max = s[0]
min = s[0]
length = len(s)

i = length - 1
while (i >= 0):
    sum += s[i]
    if (s[i] > max):
        max = s[i]
    if (s[i] < min):
        min = s[i]
    i -= 1

print("元素个数：{0}，最大值：{1}，最小值：{2}，和：{3}，平均值：{4}".format(length, max, min, sum,
                                                      sum / length))

# true break
s = [9, 7, 8, 3, 2, 1, 55, 6]

sum = 0
max = s[0]
min = s[0]
length = len(s)

i = 0
while (True):
    if (i > length - 1):
        break
    sum += s[i]
    if (s[i] > max):
        max = s[i]
    if (s[i] < min):
        min = s[i]
    i += 1

print("元素个数：{0}，最大值：{1}，最小值：{2}，和：{3}，平均值：{4}".format(length, max, min, sum,
                                                      sum / length))
