from datetime import datetime

Name = str(input("请输入您的姓名:"))
birthday = int(input("请输入您的出生年份:"))
age = datetime.today().year - birthday
print("您好! {0} 您今年 {1}".format(Name, age))
