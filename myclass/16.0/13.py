# 16.13
# csv文件格式化参数示例
import csv


def writecsv3(csvfilepath):
    headers = ["name", "age", "", "", ""]
    rows = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 30}]
    with open(csvfilepath, "w", newline="") as f:
        f_csv = csv.DictWriter(f, delimiter=":", quoting=csv.QUOTE_ALL)
        f_csv.writeheader(headers)
        f_csv.writerows(rows)


if __name__ == "__main__":
    writecsv3(r"d:\pythonpa\test.csv")
