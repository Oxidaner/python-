a = float(input("请输入三角形的边a:"))
b = float(input("请输入三角形的边b:"))
c = float(input("请输入三角形的边c:"))

if (a > b):
    a, b = b, a
if (a > c):
    a, c = c, a
if (b > c):
    b, c = c, b

result = "三角形"
if (not (a > 0 and b > 0 and c > 0 and a + b > c)):
    result = '此三边无法构成三角形'
else:
    if a == b == c:
        result = '等边三角形'
    elif (a == b or a == c or b == c):
        result = '等腰三角形'
    elif (a * a + b * b == c * c):
        result = '直角三角形'

print(result)
