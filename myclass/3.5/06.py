from calendar import isleap

for y in range(2000, 3001):
    if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        print(y, end=' ')

for y in range(2000, 3001):
    if (isleap(y)):
        print(y, end=" ")
