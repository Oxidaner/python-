# 16.11
# 使用csv.DictWriter对象读取csv文件
import csv


def readcsv2(csvfilepath):
    with open(csvfilepath, "r", newline="") as f:
        f_csv = csv.DictReader(f)
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            print(row)


if __name__ == "__main__":
    readcsv2(r"d:\pythonpa\test.csv")
