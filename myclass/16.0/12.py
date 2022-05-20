# 16.12
# 使用csv.DictWriter对象写入csv文件
import csv


def writecsv2(csvfilepath):
    headers = ["name", "age", "", "", ""]
    rows = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 30}]
    with open(csvfilepath, "w", newline="") as f:
        f_csv = csv.DictWriter(f, fieldnames=headers)
        f_csv.writeheader(headers)
        f_csv.writerows(rows)


if __name__ == "__main__":
    writecsv2(r"d:\pythonpa\test.csv")
