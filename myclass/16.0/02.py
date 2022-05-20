# 16.2
# 文本文件的读取示例(textread.py)
with open('d:\pythonpa\data1.txt', 'r') as f:
    for s in f.readlines():
        print(s, end='')
