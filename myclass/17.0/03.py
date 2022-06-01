import sqlite3
# 打开SQLite数据库E:\software\SQLiteStudio\database\test.db
con = sqlite3.connect(r'E:\software\SQLiteStudio\database\test.db')
# 查询数据库表的记录内容
cur = con.execute("SELECT id,name FROM REGION")
for row in cur:  # 循环输出结果集
    print("ID = ", row[0])
    print("NAME = ", row[1])