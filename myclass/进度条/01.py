import time

scale = 50
print("执行开始".center(scale // 2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start  # 返回一个cpu级别的精确时间计时 差值才有意义
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)  # 休眠时间
print("执行结束".center(scale // 2, "-"))
