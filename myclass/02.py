dic1 = {'张三': 80, '李四': 90}

dic1 = {'张三': 70, '李四': 90}

print(dic1.items())
print(dic1.keys())
print(dic1.get('张三'))
print(dic1['张三'])

print(dic1.pop('张三'))

dic2 = {'zc': 70}
dic1.update(dic2)
print(dic1)

dic1.popitem()
print(dic1)

dic2 = dict([('z3', 8)])
print(dic2)
# dic3 = dict('z3' =9)

set1 = {}
set1 = {1, 2, 3}
print(set1)

# 并交补运算
set2 = {2, 4, 6}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)
print("==============")
print(set1.difference(set2))
print(set1.union(set2))  # 并集
print(set1.intersection(set2))  # 交集
print(set1.issubset(set2))  # 子集
print(set1.issuperset(set2))  # 超集

# 字节系列
print("======================")
bytes1 = b'123'
print(bytes1)

dict4 = {(1, 2, 3): "uestc"}
print(dict4.values())

x = {'a': 'b', 'c': 'd'}
print('b' in x.values())

x = {1: 2, 2: 3}
print(x.get(3, 4))  # 相当于if else 如果没有键3返回4
print(x.get(2, 4))

a = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(sum(a))

stu = {
    "张琳": 58,
    "孙治平": 70,
    "徐小伟": 89,
    "徐丽萍": 69,
    "童万丽": 90,
    "钱志敏": 84,
    "赵虚余": 64
}
print(stu)  # 显示原有字典
stu1 = {"晋宇浩": "缺考"}  # 在字典中添加姓名为晋宇浩的同学，成绩显示为"缺考"
stu.update(stu1)
print(stu)
stu['张琳'] = 60  # 张琳的成绩改为60
print(stu)
stu.pop('徐小伟')  # 删除徐小伟以及她的成绩
print(stu)  # 现有字典；
print(len(stu))  # 统计当前总人数
keyname = str(input("输入一个同学姓名"))  # 从键盘输入一个同学的姓名
name = stu.get(keyname)
if name is None:
    print("没找到该同学")  # 如字典中无此同学显示“没找到该同学”
else:
    print(name)  # 显示该同学的成绩，
