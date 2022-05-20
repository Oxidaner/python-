# 16.19
# 对象JSON格式序列化示例
import json

urls = {'baidu': 'www.baidu.com', 'google': 'www.google.com'}
with open(r"d:\pythonpa\test.json", "w") as f:
    json.dump(urls, f)
