# 16.6
# 内存文件读写示例
from io import StringIO

f = StringIO("hello!\nhi!\nGoodbye!")
for s in f:
    print(s.strip())
