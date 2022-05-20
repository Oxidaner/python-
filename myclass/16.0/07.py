# 16.7
# 内存二进制文件读写示例
from io import BytesIO

f = BytesIO()
f.write("中文".encode("utf-8"))
f.seek(0)
b = f.read()
print(b)
print(f.getvalue())
