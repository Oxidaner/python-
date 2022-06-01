import sqlite3
# 创建SQLite数据库
con = sqlite3.connect(r'E:\software\SQLiteStudio\database\test.db')
# 创建表包含两个列,即id和name
con.execute("CREATE TABLE REGION(id PRIMARY KEY, name)")
