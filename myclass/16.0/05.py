# 16.5
# 随机文件读写实例
import os

f = open(r'd:\pythonpa\test.dat', "w+b")
f.seek(0)
f.write(b"hello")
f.write(b"world")
f.seek(-5, os.SEEK_END)
b = f.read(5)
print(b)
