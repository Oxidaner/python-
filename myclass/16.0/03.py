# 16.3
# 二进制文件写入实例
with open(r'd:\pythonpa\test.dat', "wb") as f:
    f.write(b"123")
    f.write(b"abc")
