def min_n(a, b, *c):
    min_number = a if (a < b) else b
    for n in c:
        if n < min_number:
            min_number = n
    return min_number


print(min_n(8, 2))
print(min_n(16, 1, 7, 4, 15))
