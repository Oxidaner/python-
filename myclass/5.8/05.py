m = [9, 7, 8, 3, 2, 1, 5, 6]

for i, value in enumerate(m):
    if (value % 2 == 0):
        m[i] = value**2

print(m)
