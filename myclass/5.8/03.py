li = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
# 方法一
s = set(li)
li = list(s)
print(li)


# 方法二
def deleteDuplicatedElementFromList(list):
    list.sort()  # 排序
    print("sorted list:%s" % list)
    length = len(list)  # 列表长度
    lastItem = list[length - 1]  # 尾指针
    for i in range(length - 2, -1, -1):  # 从后向前遍历
        currentItem = list[i]
        if currentItem == lastItem:  # 如果相等 调整尾指针
            list.remove(currentItem)
        else:
            lastItem = currentItem
    return list


li = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
print(deleteDuplicatedElementFromList(li))


# 方法三
def deleteDuplicatedElementFromList2(list):
    resultList = []
    for item in list:
        if item not in resultList:
            resultList.append(item)
    return resultList
