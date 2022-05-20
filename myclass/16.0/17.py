# 16.17
# 对象序列化示例
import pickle
with open(r"d:\pythonpa\test.dat", "wb") as f:
    s1 = "hello"
    c1 = 1 + 2j
    t1 = (1, 2, 3)
    d1 = dict(name="zhangsan", age=20)
    pickle.dump(s1, f)
    pickle.dump(c1, f)
    pickle.dump(t1, f)
    pickle.dump(d1, f)
