# sqlite3模块连接和操作SQLite数据库

import sqlite3  # 导入sqlite3模块

conn = sqlite3.connect('test.db')  # 调用sqlite3模块的connect（）方法创建/打开数据库
cur = conn.cursor()  # 利用返回的连接对象创建一个cursor对象
sql0 = 'create table gdp_ranking(no int primary key, name text, gdp_value real, increment real)'

# 使用cursor对象的execute()方法来创建表
sql0 = "create table gdp_ranking(no int primary key, name text, gdp_value real, increment real)"

cur.execute(sql0)

# 往表里插入记录

sql1 = "insert into gdp_ranking(no,name,gdp_value,increment) values(?,?,?,?)"
data = [
    (1, 'shanghai', 434214.85, 8.1),
    (2, 'beijing', 40269.6, 8.5),
    (3, 'shenzhen', 30664.85, 6.7),
    (4, 'guangzhou', 28231.97, 8.1),
    (5, 'chongqing', 27894.02, 8.3),
    (6, 'suzhou', 22718.34, 8.7),
]
cur.executemany(sql1, data)

# 如果调用了DML(数据库操作语言)语句，必须使用连接对象执行commit()/rollback()方法提交/回滚事务
conn.commit()

# 关闭数据库连接
conn.close()

# 修改数据表的记录、
# sql2 = 'update gdp_ranking set name= "SH" where no>=5'
# cur.execute(sql2)

# 删除数据表记录
# sql3 = 'delete from gdp_ranking where no >=5'
# cur.execute(sql3)

# 查询数据表的记录（升序）
# sql4 = 'select * from gdp_ranking order by gdp_value asc'
# cur.execute(sql4)