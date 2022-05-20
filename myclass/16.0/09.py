# 16.9
# 使用csv.reader对象读取csv文件
import csv


def readcsv1(csvfilepath):
    with open(csvfilepath, nawline="") as f:
        f_csv = csv.reader(f)
        beaders = next(f_csv)
        print(beaders)
        for row in f_csv:
            print(row)


if __name__ == "__main__":
    readcsv1(r"d:\pythonpa\test.csv")
