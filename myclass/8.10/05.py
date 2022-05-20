def func(n):
    return (max(n), min(n), len(n))


s1 = [9, 7, 8, 3, 1, 55, 6]
s2 = ["apple", 'pear', 'melon', 'kiwi']
print(s1)
s3 = "TheQuickBrownFox"
for i in (s1, s2, s3):
    t = func(i)
    print("最大? = {0}, 最小? = {1}, 元素个数 = {2}".format(t[0], t[1], t[2]))
