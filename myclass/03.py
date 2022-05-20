mark = int(input("请输入成绩:"))
if (mark >= 60):
    grade = "及格"
else:
    grade = "不及格"
if (mark >= 70):
    grade = "中等"
if (mark >= 80):
    grade = "良好"
if (mark >= 90):
    grade = "优秀"
print(grade)
