# 16.20
# 对象JSON格式反序列化示例
import json
with open(r"d:\pythonpa\test.json", "r") as f:
    urls = json.load(f)
    print(urls)
