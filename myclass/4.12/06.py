a = float(input("请输入操作数（左）："))
b = float(input("请输入操作数（右）："))
operator = input("请输入操作符(+、-、*、/、%):")
if (b == 0 and (operator == '/' or operator == '%')):
    print("分母异常")
else:
    if (operator == '+'):
        res = a + b
    if (operator == '-'):
        res = a - b
    if (operator == '*'):
        res = a * b
    if (operator == '/'):
        res = a / b
    if (operator == '%'):
        res = a % b
print("{0} {1} {2} = {3}".format(a, operator, b, res))
