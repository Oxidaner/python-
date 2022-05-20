# 16.8
# 使用gzip模块压缩和解压文件的示例
import gzip
import sys

filename = sys.argv[0]
filenamezip = filename + '.gz'
# gzip压缩
with gzip.open(filenamezip, "wt") as f:
    for s in open(filename, "r"):
        f.write(s)
# gzip解压 / 提取
for s in gzip.open(filenamezip, "r"):
    print(s)
