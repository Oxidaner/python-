# 16.10
# 使用csv.writer对象写入csv文件
import csv


def writecsv1(csvfilepath):
    headers = ["name", "age", "", "", ""]
    rows = [["zhangsan", 20], ["lisi", 30]]
    with open(csvfilepath, "w", newline="") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == "__main__":
    writecsv1(r"d:\pythonpa\test.csv")
