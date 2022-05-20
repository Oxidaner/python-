# 16.14
# Dialect类实例
import csv


def writecsv4(csvfilepath):
    headers = ["name", "age", "", "", ""]
    rows = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 30}]
    with open(csvfilepath, "w", newline="") as f:
        f_csv = csv.DictWriter(f, 'mydialect')
        f_csv.writeheader(headers)
        f_csv.writerows(rows)


if __name__ == "__main__":
    writecsv4(r"E:\python工作文件\test.csv")
