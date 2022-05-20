# tuple

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple)
print(tuple[0:3])
print(tuple[1:4:2])
tuple = (1, 2, 3, 4, 5, (1, 2))
print(tuple[5][1])  # 多级索引
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple = ("a", "b", "c")
print(max(tuple))
print("================================================")

# list
list1 = [1, 2, 3]
print(list1)
list1 = list(tuple)

print(len(list1))
list1.append('end')
print(list1)
list2 = list1.copy()
print(list2)
list1.extend((1, 2))
list2.insert(0, (1, 3))
list1.remove(1)
list2.pop()  # 默认弹出最后一个数 返回值也是最后一个数
list1.reverse()
# list1.sort() 存在不同类型无法排序
print(list1, id(list1))
print(list2, id(list2))
print("================================================")

list1 = [1, 2, 3]
for item in list1:
    print(item)
for item in range(5):
    print(item)
print(range(5))

print("================================================")

ls = [[1, 2, 3], [[4, 5], 6], [7, 8]]
print(len(ls))
print("============")
listV = list(range(5))
print(2 in listV)
print("============")
s = [1, 2, 3, 4, 5, 6]
s[:1] = []
s[:2] = 'a'
s[2:] = 'b'  # [a,4,b]
s[2:3] = ['x', 'y']  # [a,4,x,y]
del s[:1]
print(s)

data = [12.04, 11.15, 13.47, 13.58, 12.04, 12.04, 11.15, 12.58, 11.15]
print(len(data))
print(data.count(12.04))
print(min(data))
data.remove(min(data))
print(data)
