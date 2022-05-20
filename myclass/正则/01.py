import re

# 1.匹配出0-99之间的数字
strA = '123456789'
ptr = r'[1-9]?[0-9]{1}'
result1 = re.findall(ptr, strA)

# 2.匹配1-100之间的数。


# 邮箱
strA = '123456789'
ptr = r'\w{4,20}@\w+[.]\w'
result1 = re.findall(ptr, strA)
