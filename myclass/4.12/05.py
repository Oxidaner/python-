salary = float(input("请输入有固定工资收入的党员的月工资："))
if salary <= 3000:
    tax = salary * 0.0005
elif salary <= 5000:
    tax = salary * 0.01
elif salary <= 10000:
    tax = salary * 0.15
else:
    tax = salary * 0.02

print("月工资 = {0}, 交纳党费 = {1}".format(salary, tax))
