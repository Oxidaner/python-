# 16.1
# 文本文件的写入示例(textwriter.py)
with open(r'd:\pythonpa\data1.txt', 'w') as f:
    f.write('123\n')  # 写入字符串
    f.write('abc\n')  # 写入字符串
    f.writelines(['456\n', 'def\n'])  # 写入列表
